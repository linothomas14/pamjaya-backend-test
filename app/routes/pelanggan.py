from flask import jsonify, request
from app import app
from app.controller import KeluhanController, PelangganController


@app.route('/')
def index():
    return jsonify({"msg": "This is price-optimizer-api"})


@app.route('/pelanggans', methods=['GET'])
def user():
    page = request.args.get('page', 1)
    nama = request.args.get('nama', 'all')
    return PelangganController.index(page, nama)

# Read userById


@app.route('/pelanggans/<string:id>', methods=['GET'])
def user_get(id):
    return PelangganController.show(id)


@app.route('/login', methods=['POST'])
def login():
    return PelangganController.login()

@app.route('/sendOTP', methods=['POST'])
def sendOTP():
    return PelangganController.sendOTP()

@app.route('/register', methods=['POST'])
def register():
    return PelangganController.register()
