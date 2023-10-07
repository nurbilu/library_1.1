# models/customer.py

from app import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __init__(self, name, city, age):
        self.name = name
        self.city = city
        self.age = age
