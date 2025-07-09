from flask import Flask, jsonify, request
from server.controller.expense_controller import expenseController
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import app

@app.route("/expense", methods=['GET', 'POST', 'PUT', 'DELETE'])
@jwt_required()
def expenses_routes():
    username = get_jwt_identity()
    if request.method == 'GET':
        expense_controller = expenseController()
        expenses = expense_controller.get_expense_list()
        response = jsonify(expenses)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 200
    if request.method == 'POST':
        expense_controller = expenseController()
        data = request.form
        result = expense_controller.create_expense(user=username, value=data.get('value'), description=data.get('description'), date=data.get('date'), category=data.get('category'), is_fixed=data.get('is_fixed'))
        status_code = result.get('statusCode', 500)
        response = jsonify(result)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, status_code
    if request.method == 'PUT':
        expense_controller = expenseController()
        data = request.form
        result = expense_controller.update_expense(id=data.get('id'), value=data.get('value'), description=data.get('description'), date=data.get('date'), category=data.get('category'), is_fixed=data.get('is_fixed'), user_id=username)
        status_code = result.get('statusCode', 500)
        response = jsonify(result)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, status_code
    if request.method == 'DELETE':
        expense_controller = expenseController()
        id = request.args.get('id')
        result = expense_controller.remove_expense(id)
        status_code = result.get('statusCode', 500)
        response = jsonify(result)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, status_code