import os
from flask_jwt_extended import JWTManager
import pymysql
from db_file import db
from flask import Flask, jsonify, request
from sqlalchemy.sql import text
import models
from server.controller.income_controller import incomeController
from server.controller.expense_controller import expenseController
from server.controller.categories_controller import categoriesController
import configparser

app = Flask(__name__)
jwt = JWTManager(app)

config = configparser.ConfigParser()
config.read('config.ini')
app.secret_key = config.get('jwt', 'secret_key')
app.config["JWT_SECRET_KEY"] = config.get('jwt', 'secret_key')
app.config['JWT_IDENTITY_CLAIM'] = 'sub'

db_user = os.getenv('DATABASE_USER', 'root')
db_password = os.getenv('DATABASE_PASSWORD', '')
db_host = os.getenv('DATABASE_HOST', 'localhost')
db_name = os.getenv('DATABASE_NAME', 'fc')

app.config['SQLALCHEMY_DATABASE_URI'] = (
    f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

from server.routes import users    
from server.routes import category
from server.routes import expenses
from server.routes import incomes

@app.route('/db')
def testdb():
    try:
        db.session.query(text('1')).from_statement(text('SELECT 1')).all()
        return '<h1>It works.</h1>'
    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text
    
@app.cli.command('init-db')
def init_db_command():
    """Create db tables."""
    with app.app_context():
        try:
            db.drop_all()
            db.create_all()
        except Exception as e:
            print(f'Error creating tables: {e}')
    print('DB initialized.')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)