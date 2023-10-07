# routes/loan_routes.py

from flask import Blueprint, request, jsonify
from models.loan import Loan
from app import db

loan_blueprint = Blueprint('loan_blueprint', __name__)

@loan_blueprint.route('/loans', methods=['GET'])
def get_all_loans():
    loans = Loan.query.all()
    loan_list = [{'cust_id': loan.cust_id, 'book_id': loan.book_id, 'loan_date': loan.loan_date, 'return_date': loan.return_date} for loan in loans]
    return jsonify(loan_list)

# Implement other CRUD operations (create, read, update, delete) for loans here.
