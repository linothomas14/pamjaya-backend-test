from flask import jsonify, request
from app import app
from app.controller import UserController


@app.route('/')
def index():
    return jsonify({"msg": "This is price-optimizer-api"})

@app.route('/addUser', methods=['POST'])
def addUser():
    return UserController.addUser()

@app.route('/users', methods=['GET'])
def user():
    page = request.args.get('page', 1)
    nama = request.args.get('nama', 'all')
    return UserController.index(page, nama)

# Read userById


@app.route('/users/<string:id>', methods=['GET'])
def user_get(id):
    return UserController.show(id)



