# run.py

from app import app
from routes import book_routes, customer_routes, loan_routes

app.register_blueprint(book_routes.book_blueprint)
app.register_blueprint(customer_routes.customer_blueprint)
app.register_blueprint(loan_routes.loan_blueprint)

if __name__ == '__main__':
    app.run(debug=True)

