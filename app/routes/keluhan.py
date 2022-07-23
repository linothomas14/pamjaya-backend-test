from flask import request
from app import app
from app.controller import KeluhanController
from flask_jwt_extended import *
# Read and add keluhans


@app.route('/keluhans', methods=['GET', 'POST'])
def keluhan():
    if request.method == 'GET':
        page = request.args.get('page', 1)

        jenisKeluhan = request.args.get('jenis_keluhan', "all")
        return KeluhanController.index(page, jenisKeluhan)
    else:
        return KeluhanController.addKeluhan()

# CRUD keluhan



@app.route('/keluhans/<string:id>', methods=['GET', 'PUT', 'DELETE'])
def keluhans(id):
    if request.method == 'PUT':
        return KeluhanController.updateKeluhan(id)
    if request.method == 'DELETE':
        return KeluhanController.deleteKeluhan(id)
    else:
        return KeluhanController.show(id)

# Return True if user role is admin



def checkAuth():
    user_identity = get_jwt_identity()
    return True if user_identity['role'] == 'admin' else False

@app.route('/test', methods=['POST'])
def testOptinal():
    return KeluhanController.testOptional()
