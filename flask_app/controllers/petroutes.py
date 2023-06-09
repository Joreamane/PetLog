from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.pet import Pet
from werkzeug.utils import secure_filename
from flask_app import ALLOWED_EXTENSIONS

import os

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

@app.route('/newpet')
def newPet_page():
    if not session:
        flash('Please log in first!', 'login')
        return redirect('/')
    data = {'id': session['user_id']}
    return render_template('newpet.html', user=User.get_user(data))

@app.route('/newpet', methods=['POST'])
def newPet():
    data = {
        'pet_name': request.form['pet_name'],
        'pet_type': request.form['pet_type'],
        'pet_breed': request.form['pet_breed'],
        'image_path': request.form['image_path'],
        'user_id': session['user_id'],
    }
    upload_file(data.image_path)
    Pet.add_pet(data)
    return redirect('/dashboard')