from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.pet import Pet

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
        'user_id': session['user_id'],
    }
    Pet.add_pet(data)
    return redirect('/dashboard')