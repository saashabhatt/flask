"""Blogly application."""
from flask import Flask, request, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db, User, Post, Tag, PostTag



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
    tags = Tag.query.filter().all()
    return render_template("postform.html", user=user, tags=tags)

@app.route('/users/<int:user_id>/posts/new', methods=["POST"])
def process_form(user_id):
    user = User.query.get(user_id)
    title = request.form['title']
    content = request.form['content']
    tag_id = [int(num) for num in request.form.getlist("tags")]
    tags = Tag.query.filter(Tag.id.in_(tag_id)).all()
    
    new_post = Post(title=title, content=content, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()
    for tag in tags:
        new_post.tagslist.append(tag)
    
    db.session.commit()
    return redirect(f"/users/{user_id}")

@app.route('/posts/<int:post_id>')
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("postinfo.html", post=post)

@app.route('/posts/<int:post_id>/edit')
def edit_post(post_id):
    post = Post.query.get(post_id)
    tags = Tag.query.filter().all() 
    return render_template("editpost.html", post=post, tags=tags)

@app.route('/posts/<int:post_id>/edit', methods=["POST"])
def route_edit_post(post_id):
    post = Post.query.get(post_id)
    title = request.form['title']
    content = request.form['content']
    
    post.title = title
    post.content = content

    tags = [int(num) for num in request.form.getlist("tags")]

    for tag in tags:
        tag_add = Tag.query.get(tag)
        post.tagslist.append(tag_add)

    db.session.add(post)
    db.session.commit()
    return redirect(f"/posts/{post_id}")

@app.route('/posts/<int:post_id>/delete', methods=["POST"])
def delete_post(post_id):
    post = Post.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/users')

@app.route('/tags')
def list_tags():
    tags = Tag.query.all()
    return render_template("tagshow.html", tags=tags)

@app.route('/tags/<int:tag_id>')
def tag_detail(tag_id):
    tags = Tag.query.get_or_404(tag_id)
    posts = tags.postlist
    return render_template("tagdetail.html", tags=tags, posts=posts)

@app.route('/tags/new')
def add_tag():
    return render_template("addtag.html")

@app.route('/tags/new', methods=["POST"])
def create_tags():
    name = request.form["name"]
    new_tag = Tag(name=name)
    db.session.add(new_tag)
    db.session.commit()
    return redirect('/tags')

@app.route('/tags/<int:tag_id>/edit')
def edit_tag(tag_id):
    tag = Tag.query.get(tag_id)
    return render_template("edittag.html", tag=tag)

@app.route('/tags/<int:tag_id>/edit', methods=["POST"])
def route_edit_tag(tag_id):
    tag = Tag.query.get(tag_id)
    name = request.form['name']

    tag.name = name
    db.session.add(tag)
    db.session.commit()
    return redirect("/tags")

@app.route('/tags/<int:tag_id>/delete', methods=["POST"])
def delete_tag(tag_id):
    tag = Tag.query.get(tag_id)
    db.session.delete(tag)
    db.session.commit()
    return redirect('/tags')
