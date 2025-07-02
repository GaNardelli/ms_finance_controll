import os
import pymysql
from db_file import db
from flask import Flask, jsonify, request
from sqlalchemy.sql import text
from server.controller.income_controller import incomeController

app = Flask(__name__)

# Configuração do banco de dados a partir de variáveis de ambiente
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
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

@app.route("/income_list", methods=['GET', 'POST', 'PUT', 'DELETE'])
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
    
@app.cli.command('init-db')
def init_db_command():
    """Create db tables."""
    with app.app_context():
        db.create_all()
    print('Data base initialized.')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)