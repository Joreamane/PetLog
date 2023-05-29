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

    @classmethod
    def add_pet(cls,data):
        query = 'INSERT INTO pets (pet_name, pet_type, pet_breed, user_id, created_at, updated_at) VALUES (%(pet_name)s, %(pet_type)s, %(pet_breed)s, %(user_id)s, NOW(), NOW());'
        return connectToMySQL('pet_log').query_db(query,data)
    
    @classmethod
    def get_pets(cls,data):
        query = 'SELECT * FROM users LEFT JOIN pets ON pets.user_id = users.id WHERE users.id = %(id)s;'
        results = connectToMySQL('pet_log').query_db(query,data)
        user_pets = []
        for row in results:
            pet_data = {
                'id': row['pets.id'],
                'pet_name': row['pet_name'],
                'pet_type': row['pet_type'],
                'pet_breed': row['pet_breed'],
                'user_id': row['user_id'],
                'created_at': row['pets.created_at'],
                'updated_at': row['pets.updated_at']
            }
        user_pets.append(pet_data)
        return user_pets
    
    @classmethod
    def get_one_pet(cls,data):
        query = 'SELECT * FROM pets WHERE pets.id = %(id)s;'
        result = connectToMySQL('pet_log').query_db(query,data)
        return result
    
    