from _.extensions import db


class Jadwal(db.Model):
    __tablename__ = 'jadwal'

    id = db.Column(db.Integer, primary_key=True)
    mata_kuliah_id = db.Column(db.Integer, db.ForeignKey(
        'mata_kuliah.id'), nullable=False)
    pertemuan_ke = db.Column(db.Integer, nullable=False)
    tanggal = db.Column(db.Date, nullable=False)
    jam_mulai = db.Column(db.Time, nullable=False)
    jam_selesai = db.Column(db.Time, nullable=False)

    kehadirans = db.relationship('Kehadiran', backref='jadwal', lazy=True)
