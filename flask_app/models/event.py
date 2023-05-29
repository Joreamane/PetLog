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
