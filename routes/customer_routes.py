# routes/customer_routes.py

from flask import Blueprint, request, jsonify
from models.customer import Customer
from app import db

customer_blueprint = Blueprint('customer_blueprint', __name__)

@customer_blueprint.route('/customers', methods=['GET'])
def get_all_customers():
    customers = Customer.query.all()
    customer_list = [{'id': customer.id, 'name': customer.name, 'city': customer.city, 'age': customer.age} for customer in customers]
    return jsonify(customer_list)

# Implement other CRUD operations (create, read, update, delete) for customers here.
