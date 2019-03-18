
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Email, Length, DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class Profile(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('male', 'Male'),('female','Female')], validators=[InputRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    location = StringField('Location', validators=[DataRequired()])
    biography = TextAreaField('Biography', validators=[DataRequired(), Length(min=10, max=1000, message="Bio should be at least 10 characters.")])
    dp = FileField('Profile Pic', validators=[FileRequired("Hey you need a picture for everyone to see"), FileAllowed(['jpg','png'], 'Images only please :)')
    ])