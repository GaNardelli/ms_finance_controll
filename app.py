import os
import pymysql
from db_file import db
from flask import Flask, jsonify, request
from sqlalchemy.sql import text
import models
from server.controller.income_controller import incomeController
from server.controller.expense_controller import expenseController


app = Flask(__name__)

db_user = os.getenv('DATABASE_USER', 'root')
db_password = os.getenv('DATABASE_PASSWORD', '')
db_host = os.getenv('DATABASE_HOST', 'localhost')
db_name = os.getenv('DATABASE_NAME', 'fc')

app.config['SQLALCHEMY_DATABASE_URI'] = (
    f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def testdb():
    try:
        db.session.query(text('1')).from_statement(text('SELECT 1')).all()
        return '<h1>It works.</h1>'
    except Exception as e:
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

@app.route("/expense", methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_expense_list():
    if request.method == 'GET':
        expense_controller = expenseController()
        expenses = expense_controller.get_expense_list()
        response = jsonify(expenses)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 200
    if request.method == 'POST':
        expense_controller = expenseController()
        data = request.form
        result = expense_controller.create_expense(user=data.get('user_id'), value=data.get('value'), description=data.get('description'), date=data.get('date'), category=data.get('category'), is_fixed=data.get('is_fixed'))
        status_code = result.get('statusCode', 500)
        response = jsonify(result)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, status_code
    if request.method == 'PUT':
        expense_controller = expenseController()
        data = request.form
        result = expense_controller.update_expense(expense_id=data.get('expense_id'), value=data.get('value'), description=data.get('description'), date=data.get('date'), category=data.get('category'), is_fixed=data.get('is_fixed'))
        status_code = result.get('statusCode', 500)
        response = jsonify(result)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, status_code
    if request.method == 'DELETE':
        expense_controller = expenseController()
        expense_id = request.args.get('expense_id')
        result = expense_controller.remove_expense(expense_id)
        status_code = result.get('statusCode', 500)
        response = jsonify(result)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, status_code

@app.route("/income", methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_income_list():
    if request.method == 'GET':
        income_controller = incomeController()
        incomes = income_controller.get_income_list()
        response = jsonify(incomes)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 200
    if request.method == 'POST':
        data = request.form
        income_controller = incomeController()
        result = income_controller.create_income(data.get('user'), data.get('value'), data.get('description'), data.get('date'), data.get('category'))
        status_code = result.get('statusCode', 500)
        response = jsonify(result)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, status_code
    if request.method == 'DELETE':
        income_id = request.args.get('income_id')
        income_controller = incomeController()
        result = income_controller.remove_income(income_id)
        status_code = result.get('statusCode', 500)
        response = jsonify(result)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, status_code
    if request.method == 'PUT':
        data = request.form
        income_controller = incomeController()
        result = income_controller.update_income(data.get('income_id'), data.get('value'), data.get('description'), data.get('date'), data.get('category'))
        status_code = result.get('statusCode', 500)
        response = jsonify(result)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, status_code
    
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