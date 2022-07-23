from app import db
from datetime import datetime
from app.model.pelanggan import Pelanggan


class Keluhan(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    jenis_keluhan = db.Column(db.String(50), nullable=False)
    keluhan = db.Column(db.String(100), nullable=False)
    
    kelurahan = db.Column(db.String(50), nullable=False)
    kecamatan = db.Column(db.String(50), nullable=False)
    kota_madya = db.Column(db.String(50), nullable=False)
    kode_pos = db.Column(db.String(10), nullable=False)
   
    status = db.Column(db.String(100), nullable=False,
                       default="Sedang diproses")
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    id_pelanggan = db.Column(db.String(50), db.ForeignKey(Pelanggan.id_pelanggan))
    # pelanggan = db.relationship('Pelanggan', backref='id_pelanggan')

    def __repr__(self):
        return '<Keluhan {}>'.format(self.id)
