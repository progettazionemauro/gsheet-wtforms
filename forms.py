from flask_wtf import FlaskForm
import gspread
"""Form object declaration."""
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    DateField,
    PasswordField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
    IntegerField,
    RadioField,
    BooleanField
)
from wtforms.validators import URL, DataRequired, Email, EqualTo, Length, InputRequired
from wtforms import validators
sa = gspread.service_account(filename='./service_account.json')
sh = sa.open("opensheet test")
wks = sh.worksheet("Test Sheet")
data = wks.get_all_values()

class ClubForm(FlaskForm):
    name = StringField('Club name', validators=[InputRequired(), Length(min=10, max=100)])
    description = TextAreaField('Club Description', validators=[InputRequired(), Length(max=200)])
    spaces_available = IntegerField('Spaces available', validators=[InputRequired()])

    tipo_persona = SelectField('Che tipo di persona?', 
                             choices=[index[1] for index in data], 
                             validators=[InputRequired()])
   
    """""tipo_persona = SelectField('Che tipo di persona?', 
                             choices=
                              ["agricoltore", "politico","ingegnere", "Arh"], 
                             validators=[InputRequired()]) """
  
    is_free = BooleanField('Free club', default='checked')
    submit = SubmitField("Create club")




  
