from flask import request
from app.model.pelanggan import Pelanggan
from app import response, app, db
from flask_jwt_extended import *
import os
from twilio.rest import Client

def sendOTP():
    try:
        noHp = request.json['no_hp']

        account_sid = str(os.environ.get("TWILIO_ACCOUNT_SID"))
        auth_token = str(os.environ.get("TWILIO_AUTH_TOKEN"))
        client = Client(account_sid, auth_token)

        client.verify \
            .v2 \
            .services(str(os.environ.get("VERIFICATION_SID"))) \
            .verifications \
            .create(to='+62{noHp}'.format(noHp=noHp), channel='sms')

        return response.ok('','OTP dikirim ke nomor +62'+noHp)          
    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')

def confirmOTP():
    try:
        otpCode = request.json['kode_otp']
        noHp = request.json['no_hp']
        
        account_sid = str(os.environ.get("TWILIO_ACCOUNT_SID"))
        auth_token = str(os.environ.get("TWILIO_AUTH_TOKEN"))
        
        client = Client(account_sid, auth_token)
        verification_check = client.verify \
        .v2 \
        .services(str(os.environ.get("VERIFICATION_SID"))) \
        .verification_checks \
        .create(to='+62{noHp}'.format(noHp=noHp), code=str(otpCode))

        if verification_check.status != 'approved':
            return response.badRequest('', 'kode OTP salah')

        data = {
            'id': noHp,
        }
        access_token = create_access_token(data)


        return response.ok(
            {
                "token": access_token,
            }, "Berhasil login")

    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')

def register():
    try:
        idPelanggan = request.json['id_pelanggan']
        password = request.json['password']
        otpCode = request.json['otp_code']
        
        pelanggan = Pelanggan.query.filter_by(id_pelanggan=idPelanggan).first()
        
        if not pelanggan:
            return response.notFound('', 'Id pelanggan tidak ditemukan')

        noHp = pelanggan.no_hp

        account_sid = str(os.environ.get("TWILIO_ACCOUNT_SID"))
        auth_token = str(os.environ.get("TWILIO_AUTH_TOKEN"))
        
        client = Client(account_sid, auth_token)
        verification_check = client.verify \
        .v2 \
        .services(str(os.environ.get("VERIFICATION_SID"))) \
        .verification_checks \
        .create(to='+62{noHp}'.format(noHp=noHp), code=str(otpCode))

        if verification_check.status != 'approved':
            return response.badRequest('', 'kode OTP salah')

        pelanggan.set_password(password)
        pelanggan.registered = 1
        db.session.commit()

        return response.addData('', 'register success')

    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')


def login():
    try:
        idPelanggan = request.json['id_pelanggan']
        password = request.json['password']

        pelanggan = Pelanggan.query.filter_by(id_pelanggan=idPelanggan).first()
        if not pelanggan:
            return response.notFound([], 'Pelanggan not found')

        if not pelanggan.check_password(password):
            return response.badRequest([], 'Password salah')

        data = {
            'id': pelanggan.id_pelanggan,
        }
        access_token = create_access_token(data)

        return response.ok(
            {
                "token": access_token,
            }, "Berhasil login")

    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')
