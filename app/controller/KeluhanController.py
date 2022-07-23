from flask_jwt_extended import *
from flask import request
from app.controller.PelangganController import transform_pelanggan
from app.model.keluhan import Keluhan
from app import response, db
from datetime import datetime
import uuid

from app.model.pelanggan import Pelanggan

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
        'id_pelanggan': keluhan.id_pelanggan,
        'kelurahan': keluhan.kelurahan,
        'kecamatan': keluhan.kecamatan,
        'kota_madya': keluhan.kota_madya,
        'kode_pos': keluhan.kode_pos,
        'status': keluhan.status,
        'created_at': keluhan.created_at,
        'updated_at': keluhan.updated_at,
    }
    return data


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
        kode_pos = request.json['kode_pos']

        user_identity = get_jwt_identity()
        print("HELLOOOOOOO")
        idPelanggan = user_identity['id']
        print("INI ADALAH ID PELANGGAN"+idPelanggan)
        pelanggan = Pelanggan.query.filter_by(id_pelanggan=idPelanggan).first()
        if not pelanggan:
            return response.notFound([], 'Pelanggan not found')
        id = uuid.uuid4()

        keluhan = Keluhan(id=id, keluhan=keluhan,
                          jenis_keluhan=jenisKeluhan,
                          id_pelanggan=idPelanggan,
                          kelurahan=kelurahan,
                          kecamatan=kecamatan,
                          kota_madya=kota_madya,
                          kode_pos=kode_pos)

        db.session.add(keluhan)
        db.session.commit()
        return response.addData('', 'Keluhan id ' + str(id) + 'added')

    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')


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
