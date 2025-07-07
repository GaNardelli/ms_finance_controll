from flask import Flask, jsonify, request
from server.controller.categories_controller import categoriesController
from app import app
from server.routes.users import token_required

@app.route("/category", methods=['GET', 'POST', 'PUT', 'DELETE'])
@token_required
def category_routes():
    categories_controller = categoriesController()
    if request.method == 'GET':
        data = request.form
        categories = categories_controller.get_category_list(user=data.get('user_id'))
        response = jsonify(categories)
        response.headers.add('Access-Controll-Allow-Origin', '*')
        return response, 200
    if request.method == 'POST':
        data = request.form
        categories = categories_controller.create_category(user=data.get('user_id'), description=data.get('description'), generic=data.get('generic'))
        response = jsonify(categories)
        response.headers.add('Access-Controll-Allow-Origin', '*')
        return response, 200
    if request.method == 'PUT':
        data = request.form
        categories = categories_controller.update_category(id=data.get('id'), user=data.get('user_id'), description=data.get('description'), generic=data.get('generic'))
        response = jsonify(categories)
        response.headers.add('Access-Controll-Allow-Origin', '*')
        return response, 200
    if request.method == 'DELETE':
        id = request.args.get('id')
        categories = categories_controller.delete_category(id=id)
        response = jsonify(categories)
        response.headers.add('Access-Controll-Allow-Origin', '*')
        return response, 200