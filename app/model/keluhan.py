from app import db
from datetime import datetime
from app.model.user import User


class Keluhan(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    jenis_keluhan = db.Column(db.String(50), nullable=False)
    keluhan = db.Column(db.String(100), nullable=False)
    
    kelurahan = db.Column(db.String(50), nullable=False)
    kecamatan = db.Column(db.String(50), nullable=False)
    kota_madya = db.Column(db.String(50), nullable=False)
   
    status = db.Column(db.String(100), nullable=False,
                       default="Sedang diproses")
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)
    id_user = db.Column(db.Integer,  db.ForeignKey(User.id))
    
    def __repr__(self):
        return '<Keluhan {}>'.format(self.id)
