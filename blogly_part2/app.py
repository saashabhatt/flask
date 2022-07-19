"""Blogly application."""
from flask import Flask, request, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db, User, Post



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def red_to_user():
    return redirect('/users')

@app.route('/users')
def list_user():
    users = User.query.all()
    return render_template("users.html", users=users)

@app.route('/users/new')
def add_user():
    return render_template("adduser.html")

@app.route('/users/new', methods=["POST"])
def create_user():
    first_name = request.form["fname"]
    last_name = request.form["lname"]
    image_url = request.form["img_url"] or None

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/users')

@app.route('/users/<int:user_id>')
def show_user(user_id):
    user = User.query.get_or_404(user_id)
    post = Post.query.filter_by(user_id=user_id).all()
    return render_template("userinfo.html", user=user, post=post)

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    user = User.query.get(user_id)
    return render_template("edit.html", user=user)

@app.route('/users/<int:user_id>/edit', methods=["POST"])
def route_edit_user(user_id):
    user = User.query.get(user_id)
    first_name = request.form["fname"]
    last_name = request.form["lname"]
    image_url = request.form["img_url"] or None

    user.first_name = first_name
    user.last_name = last_name
    user.image_url = image_url
    db.session.add(user)
    db.session.commit()
    return redirect('/users')

@app.route('/users/<int:user_id>/delete', methods=["POST"])
def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/users')

@app.route('/users/<int:user_id>/posts/new')
def post_form(user_id):
    user = User.query.get(user_id)
    return render_template("postform.html", user=user)

@app.route('/users/<int:user_id>/posts/new', methods=["POST"])
def process_form(user_id):
    user = User.query.get(user_id)
    title = request.form['title']
    content = request.form['content']
    
    new_post = Post(title=title, content=content, user_id=user_id)
        
    db.session.add(new_post)
    db.session.commit()
    return redirect(f"/users/{user_id}")

@app.route('/posts/<int:post_id>')
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("postinfo.html", post=post)

@app.route('/posts/<int:post_id>/edit')
def edit_post(post_id):
    post = Post.query.get(post_id)
    return render_template("editpost.html", post=post)

@app.route('/posts/<int:post_id>/edit', methods=["POST"])
def route_edit_post(post_id):
    post = Post.query.get(post_id)
    title = request.form['title']
    content = request.form['content']

    post.title = title
    post.content = content

    db.session.add(post)
    db.session.commit()
    return redirect(f"/posts/{post_id}")

@app.route('/posts/<int:post_id>/delete', methods=["POST"])
def delete_post(post_id):
    post = Post.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/users')
