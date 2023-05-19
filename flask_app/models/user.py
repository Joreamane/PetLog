from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

#regex for email validation
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        #blank array to store all user's pets
        self.pets = []

    @classmethod
    def add_user(cls,data):
        query = 'INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());'
        return connectToMySQL('pet_log').query_db(query,data)
    
    @classmethod
    def get_user(cls,data):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        return connectToMySQL('pet_log').query_db(query,data)
    
    @classmethod
    def get_by_email(cls,data):
        query = 'SELECT * FROM users WHERE email = %(email)s;'
        return connectToMySQL('pet_log').query_db(query,data)
    
    @staticmethod
    def validate_registration(user):
        is_valid = True
        if not EMAIL_REGEX.match(user['email']):
            flash('Please enter a valid email address.', 'register')
            is_valid = False
        if len(user['first_name']) < 2:
            flash('First name must be at least 2 characters', 'register')
            is_valid = False
        if len(user['last_name']) < 2:
            flash('Last name must be at least 2 characters', 'register')
            is_valid = False
        if user['regpassword'] != user['confirm']:
            flash('Passwords must match', 'register')
            is_valid = False
        if len(user['regpassword']) < 8:
            flash('Password must be at least 8 characters', 'register')
            is_valid = False
        return is_valid
    
    @staticmethod
    def validate_login(user):
        is_valid = True
        if not EMAIL_REGEX.match(user['email']):
            flash('Please enter a valid email address.', 'login')
            is_valid = False
        return is_valid