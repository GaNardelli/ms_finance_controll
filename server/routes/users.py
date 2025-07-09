from datetime import datetime, timedelta
from functools import wraps
from flask import Flask, jsonify, redirect, request, session
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app import app
from server.controller.users_controller import usersController

@app.route("/", methods=['GET'])
@jwt_required() 
def users():
    if not session.get('logged_in'):
        return redirect('http://www.example.com') # redirect to signup / singin page when exists
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@app.route('/singup', methods=['POST'])
def singup():
    data = request.form
    users_controller = usersController()
    signup_response = users_controller.signup_user(name=data.get('name'), username=data.get('username'), password=data.get('password'), email=data.get('email'))
    status_code = signup_response.get('statusCode')
    response = jsonify(signup_response)
    return response, status_code

@app.route('/login', methods=['POST'])
def login(): 
    data = request.form
    users_controller = usersController()
    validate_login = users_controller.validate_login(username=data.get('username'), password=data.get('password'))
    if validate_login.get('statusCode') == 200:
        session['logged_in'] = True
        access_token = create_access_token(identity=request.form['username'])
        return jsonify({'access_token': access_token}), 200
    else:
        return {'statusCode':403, 'msg': validate_login.get('msg')}
