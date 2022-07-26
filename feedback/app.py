from flask import Flask, render_template, redirect, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import Feedback, connect_db, db, User
from forms import RegisterForm, LoginForm, FeedbackForm


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///feedback_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "abc123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route("/")
def homepage():
    return redirect("/login")

@app.route("/register", methods=["GET", "POST"])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
    
        new_User = User.register(username, password, email, first_name, last_name)
        db.session.add(new_User)
        db.session.commit()
        session["username"] = new_User.username
        return redirect(f"/users/{new_User.username}")
    
    else:
        return render_template("register.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login_user():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.authenticate(username, password)

        if user:
            session['username'] = user.username
            return redirect(f"/users/{username}")
        else:
            form.username.errors = ["Invalid username or password"]
    
    return render_template("login.html", form=form)

@app.route('/logout')
def logout():
    session.pop("username")
    return redirect('/')

@app.route("/users/<username>")
def display_user(username):
    if "username" not in session:
        flash("Please log in to your account")
        return redirect('/login')

    all_feedbacks = Feedback.query.filter_by(username=session["username"]).all()
    return render_template("displayuser.html", username=username, all_feedbacks=all_feedbacks)

@app.route('/users/<username>/feedback/add', methods=['GET', 'POST'])
def add_feedback(username):
    if "username" not in session or session["username"] != username:
        flash("Please log in to your account")
        return redirect('/login')

    form = FeedbackForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        new_feedback = Feedback(title=title, content=content, username=session["username"])
        db.session.add(new_feedback)
        db.session.commit()
        username = session["username"]
        return redirect(f"/users/{username}")
    
    return render_template("addfeedback.html", form=form, username=username)

@app.route("/feedback/<int:id>/update", methods=['GET', 'POST'])
def edit_feedback(id):
    feedback = Feedback.query.get(id)
    if "username" not in session or session["username"] != feedback.username:
        flash("Please log in to your account")
        return redirect('/login')

    form = FeedbackForm(obj=feedback)
    if form.validate_on_submit():
        feedback.title = form.title.data
        feedback.content = form.content.data
        db.session.commit()
        username = session["username"]
        return redirect(f"/users/{username}")
    
    return render_template("editfeedback.html", form=form, feedback=feedback)

@app.route("/users/<username>/delete", methods=["POST"])
def delete_user(username):
    if "username" not in session or session["username"] != username:
        flash("Please log in to your account")
        return redirect('/login')

    user = User.query.get(username)
    Feedback.query.filter_by(username=username).delete()
    db.session.delete(user)
    db.session.commit()
    session.pop("username")
    return redirect("/login")
    
@app.route("/feedback/<int:id>/delete", methods=["POST"])
def delete_feedback(id):
    feedback = Feedback.query.get(id)
    if "username" not in session or session["username"] != feedback.username:
        flash("Please log in to your account")
        return redirect('/login')

    db.session.delete(feedback)
    db.session.commit()
    return redirect(f"/users/{feedback.username}")
    



