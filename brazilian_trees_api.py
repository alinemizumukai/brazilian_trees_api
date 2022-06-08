# -*- coding: utf-8 -*-
from genericpath import exists
from modules.db import create_db, get_db_connection
from routes.routes import Api
from flask import Flask, Blueprint
from flask import render_template, url_for, flash, request, redirect, Response
import sqlite3
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from models.form import LoginForm
from models.User import User

app = Flask(__name__)
app.debug=True
login_manager = LoginManager(app)
login_manager.login_view = "login"
app.config['SECRET_KEY'] = 'secret'


@login_manager.user_loader
def load_user(user_id):
   conn = get_db_connection()
   curs = conn.cursor()
   curs.execute("SELECT * from login where user_id = (?)",[user_id])
   lu = curs.fetchone()
   if lu is None:
      return None
   else:
      return User(int(lu[0]), lu[1], lu[2])

@app.route('/logout', methods=['GET', 'POST']) 
@login_required
def logout():
    logout_user()
    return redirect(url_for('login') )

@app.route("/login", methods=['GET','POST'])
def login():
  menuPath = 'back_routes.greetings.greetings'
  if current_user.is_authenticated:
     return redirect(url_for(menuPath))
  form = LoginForm()
  if form.validate_on_submit():
     conn = sqlite3.connect('database.db')
     curs = conn.cursor()
     curs.execute("SELECT * FROM login where email = (?)",    [form.email.data])
     user = list(curs.fetchone())
     Us = load_user(user[0])
     if form.email.data == Us.email and form.password.data == Us.password:
        login_user(Us, remember=form.remember.data)
        Umail = list({form.email.data})[0].split('@')[0]
        flash('Logged in successfully '+Umail)
        return redirect(url_for(menuPath))
     else:
        flash('Login Unsuccessfull.')
  return render_template('login.html',title='Login', form=form)

@app.route('/<string:nome>')
def error(nome):
   return render_template('error.html')

app.register_blueprint(Api, url_prefix='/')

if( not exists( "database.db" ) ):
    create_db()

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8080,threaded=True)