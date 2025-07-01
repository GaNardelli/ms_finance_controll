import pymysql
import configparser
from db_file import db
from flask import Flask, jsonify, request
from sqlalchemy.sql import text
from server.controller.income_controller import incomeController

app = Flask(__name__)
config = configparser.ConfigParser()
config.read('config.ini')
database_host = config['database']['host']
database_password = config['database']['password']
database_username = config['database']['username']
userpass = 'mysql+pymysql://' + database_username + ':' + database_password + '@'
server = 'localhost'
dbname = '/fc'
socket = '?unix_socket=/var/run/mysqld/mysqld.sock'
app.config['SQLALCHEMY_DATABASE_URI'] = userpass + server + dbname + socket
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

@app.route("/income_list", methods=['GET'])
def get_income_list():
    income_controller = incomeController()
    incomes = income_controller.getIncomesList()
    response = jsonify(incomes)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, 200

@app.route("/income_list", methods=["POST"])
def add_new_income():
    income_controller = incomeController()
    response = jsonify(request)
    return response, 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)