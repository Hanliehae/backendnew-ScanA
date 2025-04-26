from _.extensions import db


class Kontrak(db.Model):
    __tablename__ = 'kontrak'

    id = db.Column(db.Integer, primary_key=True)
    mahasiswa_id = db.Column(db.Integer, db.ForeignKey(
        'mahasiswa.id'), nullable=False)
    mata_kuliah_id = db.Column(db.Integer, db.ForeignKey(
        'mata_kuliah.id'), nullable=False)
