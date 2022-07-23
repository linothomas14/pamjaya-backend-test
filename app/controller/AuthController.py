import uuid
from flask import request
from app.model.user import User
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
            'noHp': noHp,
        }
        access_token = create_access_token(data)

        user = User.query.filter_by(no_hp=noHp).first()
        if not user:

            return response.ok({"token": access_token},'User Belum jadi pelanggan')
        id_user = uuid.uuid4()
        user.id_user = id_user
        db.session.add(user)
        db.session.commit()
        return response.ok(
            {
                "token": access_token,
            }, "Berhasil login")

    except Exception as e:
        print(e)
        return response.badRequest('error', 'Bad request')
