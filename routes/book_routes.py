# routes/book_routes.py

from flask import Blueprint, request, jsonify
from models.book import Book
from app import db

book_blueprint = Blueprint('book_blueprint', __name__)

@book_blueprint.route('/books', methods=['GET'])
def get_all_books():
    books = Book.query.all()
    book_list = [{'id': book.id, 'name': book.name, 'author': book.author, 'year_published': book.year_published, 'book_type': book.book_type} for book in books]
    return jsonify(book_list)

# Implement other CRUD operations (create, read, update, delete) for books here.
