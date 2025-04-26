from flask import Blueprint, request, jsonify
from app.models.jadwal_model import Jadwal
from app import db

jadwal_bp = Blueprint('jadwal', __name__)

@jadwal_bp.route('/jadwal', methods=['GET'])
def get_jadwal():
    jadwal = Jadwal.query.all()
    result = [
        {'id': j.id, 'mata_kuliah_id': j.mata_kuliah_id, 'pertemuan': j.pertemuan, 'tanggal': j.tanggal, 'jam_mulai': j.jam_mulai, 'jam_selesai': j.jam_selesai}
        for j in jadwal
    ]
    return jsonify(result)

@jadwal_bp.route('/jadwal', methods=['POST'])
def create_jadwal():
    data = request.json
    new_jadwal = Jadwal(
        mata_kuliah_id=data['mata_kuliah_id'],
        pertemuan=data['pertemuan'],
        tanggal=data['tanggal'],
        jam_mulai=data['jam_mulai'],
        jam_selesai=data['jam_selesai']
    )
    db.session.add(new_jadwal)
    db.session.commit()
    return jsonify({'message': 'Jadwal created'})
