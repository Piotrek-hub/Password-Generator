from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class GenerateForm(FlaskForm):
    submit = SubmitField('Generate Password')