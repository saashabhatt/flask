from flask import Flask, request, render_template, redirect, flash, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from forms import AddPetForm, EditPetForm
from wtforms import StringField, FloatField
from models import db, connect_db, Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route('/')
def homepage():
    """Route to home page"""
    pets = Pet.query.all()
    return render_template("home.html", pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pets():
    """Route to add pet form on clicking add pet"""
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.pet_name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pets = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pets)
        db.session.commit()
        return redirect('/') 
    else:    
        return render_template("addpets.html", form=form)

@app.route('/<int:pet_id>', methods=["GET", "POST"])
def edit_pets(pet_id):
    """Routes to edit pets form on clicking Edit Pet"""
    pets = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pets)

    if form.validate_on_submit():
        
        pets.photo_url = form.photo_url.data
        pets.notes = form.notes.data
        pets.available = form.available.data
        db.session.commit()
        return redirect('/') 
    else:    
        return render_template("editpets.html", form=form)