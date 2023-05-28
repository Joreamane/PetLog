from flask_bcrypt import Bcrypt
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

import os
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if not session:
        flash('Please log in first!', 'login')
        return redirect('/')
    data = {'id':session['user_id']}
    return render_template('dashboard.html', user=User.get_user(data))

@app.route('/register', methods=['post'])
def register():
    pw_hash = bcrypt.generate_password_hash(request.form['regpassword'])
    print(pw_hash)
    data = {
        'first_name' : request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash,
    }
    if not User.validate_registration(request.form):
        return redirect('/')
    user_id = User.add_user(data)
    session['user_id'] = user_id
    session['first_name'] = data['first_name']
    session['last_name'] = data['last_name']
    return redirect('/dashboard')

@app.route('/login', methods=['post'])
def login():
    data = {'email':request.form['email']}
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash('Email does not have an associated account.', 'login')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid email/password combination.', 'login')
        return redirect('/')
    session['user_id'] = user_in_db.id
    session['first_name'] = user_in_db.first_name
    session['last_name'] = user_in_db.last_name
    return redirect('/dashboard')