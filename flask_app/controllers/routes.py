from flask_bcrypt import Bcrypt
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

import os
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('login.html')

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
