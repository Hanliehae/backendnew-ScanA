from _.extensions import db


class Mahasiswa(db.Model):
    __tablename__ = 'mahasiswa'

    id = db.Column(db.Integer, primary_key=True)
    nim = db.Column(db.String(50), unique=True, nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100))
    nomor_telepon = db.Column(db.String(20))
    foto_tangan_kanan = db.Column(db.String(255))
    foto_tangan_kiri = db.Column(db.String(255))

    kontraks = db.relationship('Kontrak', backref='mahasiswa', lazy=True)
    kehadirans = db.relationship('Kehadiran', backref='mahasiswa', lazy=True)
