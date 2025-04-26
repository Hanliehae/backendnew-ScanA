from _.extensions import db


class MataKuliah(db.Model):
    __tablename__ = 'mata_kuliah'

    id = db.Column(db.Integer, primary_key=True)
    kode_mk = db.Column(db.String(50), nullable=False)
    id_mk = db.Column(db.String(100), unique=True, nullable=False)
    nama_mk = db.Column(db.String(100), nullable=False)
    semester = db.Column(
        db.Enum('Ganjil', 'Genap', name='semester_enum'), nullable=False)
    tahun_akademik = db.Column(db.Integer, nullable=False)
    kelas = db.Column(db.String(10), nullable=False)

    kontraks = db.relationship('Kontrak', backref='mata_kuliah', lazy=True)
    jadwals = db.relationship('Jadwal', backref='mata_kuliah', lazy=True)
