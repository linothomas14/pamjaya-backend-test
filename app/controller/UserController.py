import uuid
from flask import request
from app.model.user import User
from app import response, app, db
from flask_jwt_extended import *

def index(page, nama):
    try:
        offset = (int(page) - 1) * 50
        if nama == "all":
            users = User.query.offset(offset).limit(50)
        else:
            search = "%{}%".format(nama)
            users = User.query.filter(User.nama.like(
                search)).offset(offset).limit(50)
        data = transform_user(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.badRequest([], message=e)


def transform_user(users):
    data = []
    for i in users:
        data.append(singleTransform(i))
    return data


def singleTransform(user):
    data = {
        'id': user.id,
        'id_pelanggan': user.id_pelanggan,
        'id_user': user.id_user,
        'nama': user.nama,
        'no_hp': user.no_hp,
        'alamat': user.alamat_lengkap,
        'kelurahan':user.kelurahan,
        'kecamatan':user.kecamatan,
        'kota_madya': user.kota_madya,
    }
    return data


def show(id):
    try:
        user = User.query.filter_by(id=id).first()
        if not user:
            return response.notFound([], 'user not found')

        data = singleTransform(user)
        return response.ok(data, "")
    except Exception as e:
        print(e)


@jwt_required()
def addUser():
    try:
        nama = request.json['nama']
        alamat_lengkap = request.json['alamat_lengkap']
        kelurahan = request.json['kelurahan']
        kecamatan = request.json['kecamatan']
        kota_madya = request.json['kota_madya']

        user_identity = get_jwt_identity()

        noHp = user_identity['noHp']

        user = User.query.filter_by(no_hp=noHp).first()
        
        if not user:
            id_user = uuid.uuid4()

            user = User(id_user=id_user,
                        alamat_lengkap=alamat_lengkap,
                        nama=nama,
                        no_hp=noHp,
                        kelurahan=kelurahan,
                        kecamatan=kecamatan,
                        kota_madya=kota_madya
                        )

            db.session.add(user)
            db.session.commit()
            return response.addData('ok', 'User id ' + str(id_user) + 'added')

        return response.badRequest('user sudah terdaftar','error' )


    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')
