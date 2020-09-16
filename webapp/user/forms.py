from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("User Name", validators=[DataRequired()], render_kw={'class':"form-control"})
    password = PasswordField("Password", validators=[DataRequired()], render_kw={'class':"form-control"})
    remember_me = BooleanField('Remember Me', default=True, render_kw={'class': 'form-check-input'})
    submit = SubmitField('Sent', render_kw={'class':"btn btn-primary"})

