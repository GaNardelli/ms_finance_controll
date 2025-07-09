from flask import Flask, jsonify, request
from server.controller.categories_controller import categoriesController
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import app

@app.route("/category", methods=['GET', 'POST', 'PUT', 'DELETE'])
@jwt_required()
def category_routes():
    username = get_jwt_identity()
    categories_controller = categoriesController()
    if request.method == 'GET':
        data = request.form
        categories = categories_controller.get_category_list(user=username)
        response = jsonify(categories)
        response.headers.add('Access-Controll-Allow-Origin', '*')
        return response, 200
    if request.method == 'POST':
        data = request.form
        categories = categories_controller.create_category(user=username, description=data.get('description'), generic=data.get('generic'))
        response = jsonify(categories)
        response.headers.add('Access-Controll-Allow-Origin', '*')
        return response, 200
    if request.method == 'PUT':
        data = request.form
        categories = categories_controller.update_category(id=data.get('id'), user=username, description=data.get('description'), generic=data.get('generic'))
        response = jsonify(categories)
        response.headers.add('Access-Controll-Allow-Origin', '*')
        return response, 200
    if request.method == 'DELETE':
        id = request.args.get('id')
        categories = categories_controller.delete_category(id=id)
        response = jsonify(categories)
        response.headers.add('Access-Controll-Allow-Origin', '*')
        return response, 200