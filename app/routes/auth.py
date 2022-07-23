from flask import request
from app import app
from app.controller import AuthController
from flask_jwt_extended import *

@app.route('/confirmOTP', methods=['POST'])
def login():
    return AuthController.confirmOTP()

@app.route('/sendOTP', methods=['POST'])
def sendOTP():
    return AuthController.sendOTP()

# @app.route('/register', methods=['POST'])
# def register():
#     return AuthController.register()