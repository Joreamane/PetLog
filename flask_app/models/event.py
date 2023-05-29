from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.pet import Pet

class Event:
    def __init__(self,data):
        self.id = data['id']
        self.category = data['category']
        self.title = data['title']
        self.date = data['date']
        self.expire = data['expire']
        self.description = data['description']
        self.link = data['link']
        self.pet_id = data['pet_id']

    @classmethod
    def add_event(cls, data):
        query = 'INSERT INTO events (category, title, date, expire, description, link, pet_id, created_at, updated_at) VALUES (%(category)s, %(title)s, %(date)s, %(expire)s, %(description)s, %(link)s, %(pet_id)s, NOW(), NOW());'
        return connectToMySQL('pet_log').query_db(query,data)
    
    @classmethod
    def get_all_events(cls,data):
        query = 'SELECT * FROM pets LEFT JOIN events ON events.pet_id = pets.id WHERE pets.id = %(pet_id)s;'
        results = connectToMySQL('pet_log').query_db(query,data)
        all_events = []
        for row in results:
            one_event = {
                'id': row['events.id'],
                'category': row['category'],
                'title': row['title'],
                'date': row['date'],
                'expire': row['expire'],
                'description': row['description'],
                'link': row['link'],
                'pet_id': row['pet_id'],
                'created_at': row['events.created_at'],
                'updated_at': row['events.updated_at']
            }
            all_events.append(one_event)
        return all_events