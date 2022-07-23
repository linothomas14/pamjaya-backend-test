from flask import request
from app.model.pelanggan import Pelanggan
from app import response, app, db
from flask_jwt_extended import *

def index(page, nama):
    try:
        offset = (int(page) - 1) * 50
        if nama == "all":
            pelanggans = Pelanggan.query.offset(offset).limit(50)
        else:
            search = "%{}%".format(nama)
            pelanggans = Pelanggan.query.filter(Pelanggan.nama.like(
                search)).offset(offset).limit(50)
        data = transform_pelanggan(pelanggans)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.badRequest([], message=e)


def transform_pelanggan(pelanggans):
    data = []
    for i in pelanggans:
        data.append(singleTransform(i))
    return data


def singleTransform(pelanggan):
    data = {
        'id_pelanggan': pelanggan.id_pelanggan,
        'nama': pelanggan.nama,
        'no_hp': pelanggan.no_hp,
        'alamat': pelanggan.alamat_lengkap,
        'kelurahan':pelanggan.kelurahan,
        'kecamatan':pelanggan.kecamatan,
        'kota_madya': pelanggan.kota_madya,
        'kode_pos': pelanggan.kode_pos
    }
    return data


def show(id):
    try:
        pelanggan = Pelanggan.query.filter_by(id_pelanggan=id).first()
        if not pelanggan:
            return response.notFound([], 'pelanggan not found')

        data = singleTransform(pelanggan)
        return response.ok(data, "")
    except Exception as e:
        print(e)

