from random import choices
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange, URL

class AddPetForm(FlaskForm):
    """Form to add pets to the database"""
    pet_name = StringField("Name",
                            validators=[InputRequired()])
    
    species = SelectField("Species",
                            choices= [('Cat', 'cat'), ('Dog', 'dog'), ('Porquipine', 'Pne')],
                            validators=[InputRequired()])

    photo_url = StringField("Photo URL",
                            validators=[Optional(), URL(message="Enter a valid URL")])
    
    age = IntegerField("Age",
                            validators=[Optional(), NumberRange(min=0, max=30, 
                                        message="Age must be between 0 & 30")])
    
    notes = StringField("Notes",
                            validators=[Optional()])
                
class EditPetForm(FlaskForm):
    """Form to edit pets in the db"""
    photo_url = StringField("Photo URL",
                            validators=[Optional(), URL(message="Enter a valid URL")])
    
    notes = StringField("Notes",
                            validators=[Optional()])

    available = BooleanField("Available for Adoption?",
                                validators=[Optional()])
    