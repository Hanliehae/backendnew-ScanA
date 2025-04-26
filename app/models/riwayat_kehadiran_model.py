from app.models import db

class Kehadiran(db.Model):
    __tablename__ = 'kehadiran'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    jadwal_id = db.Column(db.Integer, db.ForeignKey('jadwal.id'), nullable=False)
    status = db.Column(db.String(20))  # "Hadir", "Terlambat", "Tidak Hadir"
    timestamp = db.Column(db.DateTime, nullable=False)
