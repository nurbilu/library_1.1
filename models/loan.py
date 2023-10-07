# models/loan.py

from app import db

class Loan(db.Model):
    cust_id = db.Column(db.Integer, db.ForeignKey('customer.id'), primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), primary_key=True)
    loan_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date, nullable=False)

    customer = db.relationship('Customer', backref=db.backref('loans', lazy=True))
    book = db.relationship('Book', backref=db.backref('loans', lazy=True))

    def __init__(self, cust_id, book_id, loan_date, return_date):
        self.cust_id = cust_id
        self.book_id = book_id
        self.loan_date = loan_date
        self.return_date = return_date
