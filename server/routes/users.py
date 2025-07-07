from datetime import datetime, timedelta
from functools import wraps
import os
from flask import Flask, jsonify, redirect, request, session
import jwt
from app import app
from server.controller.users_controller import usersController

secret_key = os.getenv('SECRET_KET_JWT', 'secret key for jwt')

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request/args.get('token')
        if not token:
            return jsonify({'Alert!':'Token is missing!'})
        try:
            data = jwt.token.decode(token, secret_key)
        except Exception as e:
            return jsonify({'Alert!':'Invalid Token'})
    return decorated
        
@app.route("/", methods=['GET'])
def users():
    if not session.get('logged_in'):
        return redirect('http://www.example.com') # redirect to signup / singin page when exists
    return 'logged in!'

@app.route('/singup', methods=['POST'])
def singup():
    data = request.form
    users_controller = usersController()

@app.route('/login', methods=['POST'])
def login(): 
    # get from backend the user and the password
    username = 'Teste'
    password = 'Teste'
    if request.form['username'] == username and request.form['password'] == password:
        session['logged_in'] = True
        token = jwt.encode({
            'user':request.form['username'],
            'expiration': str(datetime.now() + timedelta(hours=12))
        }, secret_key)
        return jsonify({'token': token.decode('utf-8')}), 200
    else:
        return {'statusCode':403, 'msg': 'Unable to identify'}
