from flask_jwt_extended import *
from flask import request
from app.controller import UserController
from app.model.keluhan import Keluhan
from app import response, db
from datetime import datetime
import uuid

from app.model.user import User

# def testOptional():
#     try:
#         a = request.json.get('optional')
#         b = request.json['wajib']
        
#         print(a)
#         print(b)
#         data = "{} dan {}".format(a,b)
#         return response.ok(data,"")
#     except Exception as e:
#         print(e)
#         return response.badRequest([], message=e)


# @jwt_required()
def index(page, jenisKeluhan):
    try:
        offset = (int(page) - 1) * 50
        if jenisKeluhan != "all":
            keluhans = Keluhan.query.filter_by(
                jenis_keluhan=jenisKeluhan).offset(offset).limit(50).all()
        else:
            keluhans = Keluhan.query.offset(offset).limit(50).all()
        data = transform(keluhans)
        return response.ok(data, "")

    except Exception as e:
        print(e)
        return response.badRequest([], message=e)


def transform(keluhans):
    data = []
    for i in keluhans:
        data.append(singleTransform(i))
    return data


def singleTransform(keluhan):
    data = {
        'id': keluhan.id,
        'jenis_keluhan': keluhan.jenis_keluhan,
        'keluhan': keluhan.keluhan,
        'id_user': keluhan.id_user,
        'kelurahan': keluhan.kelurahan,
        'kecamatan': keluhan.kecamatan,
        'kota_madya': keluhan.kota_madya,
        'status': keluhan.status,
        'id_user' : keluhan.id_user,
        'created_at': keluhan.created_at,
        'updated_at': keluhan.updated_at,
    }
    return data

@jwt_required()
def show(id):
    try:
        keluhan = Keluhan.query.filter_by(id=id).first()
        if not keluhan:
            return response.notFound([], 'keluhan not found')
        data = singleTransform(keluhan)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')

@jwt_required()
def addKeluhan():
    try:
        jenisKeluhan = request.json['jenis_keluhan']
        keluhan = request.json['keluhan']
        kelurahan = request.json['kelurahan']
        kecamatan = request.json['kecamatan']
        kota_madya = request.json['kota_madya']
        # keterangan = request.json['keterangan']
        # noHp = request.json['no_hp']
        user_identity = get_jwt_identity()

        noHp = user_identity['noHp']
        user = User.query.filter_by(no_hp=noHp).first()
        if not user:
            return response.notFound('', 'user not found')

        idUser = user.id
        # id = uuid.uuid4()
        keluhan = Keluhan(keluhan=keluhan,
                          jenis_keluhan=jenisKeluhan,
                          id_user=idUser,
                          kelurahan=kelurahan,
                          kecamatan=kecamatan,
                          kota_madya=kota_madya,
                          )

        db.session.add(keluhan)
        db.session.commit()
        return response.addData('', 'Keluhan '  + ' added')

    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')

# @jwt_required()
def updateKeluhan(id):
    try:
        keluhan = Keluhan.query.filter_by(id=id).first()

        # Check if keluhan not found
        if not keluhan:
            return response.notFound('', 'keluhan not found')

        keluhan.status = "Selesai"
        keluhan.updated_at = datetime.now()
        db.session.commit()

        return response.ok('', 'id = ' + str(id)+', status = ' + str(keluhan.status))

    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')

# @jwt_required()
def deleteKeluhan(id):
    try:
        keluhan = Keluhan.query.filter_by(id=id).first()

        # Check if keluhan not found
        if not keluhan:
            return response.notFound('', 'keluhan not found')

        db.session.delete(keluhan)
        db.session.commit()

        return response.ok('', 'keluhan deleted')

    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')
