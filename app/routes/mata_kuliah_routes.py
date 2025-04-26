from flask import Blueprint, request, jsonify
from app.models.mata_kuliah_model import MataKuliah
from app import db

mata_kuliah_bp = Blueprint('mata_kuliah', __name__)

@mata_kuliah_bp.route('/mata_kuliah', methods=['GET'])
def get_mk():
    mk = MataKuliah.query.all()
    result = [
        {'id': m.id, 'nama_mk': m.nama_mk, 'id_mk': m.id_mk, 'semester': m.semester, 'tahun_akademik': m.tahun_akademik, 'kelas': m.kelas}
        for m in mk
    ]
    return jsonify(result)

@mata_kuliah_bp.route('/mata_kuliah', methods=['POST'])
def create_mk():
    data = request.json
    mk = MataKuliah(
        id_mk=data['id_mk'],
        nama_mk=data['nama_mk'],
        semester=data['semester'],
        tahun_akademik=data['tahun_akademik'],
        kelas=data['kelas']
    )
    db.session.add(mk)
    db.session.commit()
    return jsonify({'message': 'Mata Kuliah created'})

@mata_kuliah_bp.route('/mata_kuliah/<int:id>', methods=['PUT'])
def update_mk(id):
    mk = MataKuliah.query.get_or_404(id)
    data = request.json
    mk.nama_mk = data['nama_mk']
    mk.semester = data['semester']
    mk.kelas = data['kelas']
    mk.tahun_akademik = data['tahun_akademik']
    db.session.commit()
    return jsonify({'message': 'Mata Kuliah updated'})

@mata_kuliah_bp.route('/mata_kuliah/<int:id>', methods=['DELETE'])
def delete_mk(id):
    mk = MataKuliah.query.get_or_404(id)
    db.session.delete(mk)
    db.session.commit()
    return jsonify({'message': 'Mata Kuliah deleted'})
