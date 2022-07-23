from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.String(50), nullable=True)
    id_pelanggan = db.Column(db.String(50),nullable=True)
    nama = db.Column(db.String(100), nullable=False)
    no_hp = db.Column(db.String(30), nullable=False)
    alamat_lengkap = db.Column(db.String(200), nullable=False)

    kelurahan = db.Column(db.String(50), nullable=False)
    kecamatan = db.Column(db.String(50), nullable=False)
    kota_madya = db.Column(db.String(50), nullable=False)
    # kode_pos = db.Column(db.String(10), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    keluhan = db.relationship("Keluhan", backref="user")


    def __repr__(self):
        return '<Pelanggan {}>'.format(self.name)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
