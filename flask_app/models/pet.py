from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app.models.user import User

class Pet:
    def __init__(self,data):
        self.id = data['id']
        self.pet_name = data['pet_name']
        self.pet_type = data['pet_type']
        self.pet_breed = data['pet_breed']
        self.user_id = session['user_id']
        #empty array for all logged events
        self.events = []