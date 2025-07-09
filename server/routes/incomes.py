from flask import Flask, jsonify, request
from server.controller.income_controller import incomeController
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import app

@app.route("/income", methods=['GET', 'POST', 'PUT', 'DELETE'])
@jwt_required()
def incomes_routes():
    username = get_jwt_identity()
    if request.method == 'GET':
        income_controller = incomeController()
        incomes = income_controller.get_income_list()
        response = jsonify(incomes)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 200
    if request.method == 'POST':
        data = request.form
        income_controller = incomeController()
        result = income_controller.create_income(username, data.get('value'), data.get('description'), data.get('date'), data.get('category'))
        status_code = result.get('statusCode', 500)
        response = jsonify(result)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, status_code
    if request.method == 'DELETE':
        id = request.args.get('id')
        income_controller = incomeController()
        result = income_controller.remove_income(id)
        status_code = result.get('statusCode', 500)
        response = jsonify(result)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, status_code
    if request.method == 'PUT':
        data = request.form
        income_controller = incomeController()
        result = income_controller.update_income(data.get('id'), data.get('value'), data.get('description'), data.get('date'), data.get('category'))
        status_code = result.get('statusCode', 500)
        response = jsonify(result)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, status_code