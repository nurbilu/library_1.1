from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import create_db
import os

app = Flask(__name__)
db_path = os.path.abspath("library.db")
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)
