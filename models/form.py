from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from modules.db import create_db, get_db_connection

import sqlite3
class LoginForm(FlaskForm):
 email = StringField('Email',validators=[DataRequired(),Email()])
 password = PasswordField('Senha',validators=[DataRequired()])
 remember = BooleanField('Remember Me')
 submit = SubmitField('Login')
 def validate_email(self, email):
    conn = sqlite3.connect('database.db')
    curs = conn.cursor()
    curs.execute("SELECT email FROM login where email = (?)",[email.data])
    valemail = curs.fetchone()
    if valemail is None:
      raise ValidationError('Este e-mail não está cadastrado. Por favor, faça seu cadastro.')

class RegisterForm(FlaskForm):
  email = StringField('Email',validators=[DataRequired(),Email()])
  password = PasswordField('Senha',validators=[DataRequired()])
  submit = SubmitField("Registrar")
  def validate_email(self, email):
    conn = sqlite3.connect('database.db')
    curs = conn.cursor()
    curs.execute("SELECT email FROM login where email = (?)",[email.data])
    valemail = curs.fetchone()
    if valemail is not None:
      raise ValidationError('Este e-mail já possui cadastro. Faça seu login.')

