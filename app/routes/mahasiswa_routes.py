from flask import Blueprint, request, jsonify
from app.models.user import User
from app import db
from app.utils.auth_helper import hash_password

mahasiswa_bp = Blueprint('mahasiswa', __name__)

@mahasiswa_bp.route('/mahasiswa', methods=['GET'])
def get_mahasiswa():
    mahasiswa = User.query.filter_by(role='mahasiswa').all()
    result = [
        {'id': m.id, 'nim': m.nim, 'nama': m.nama, 'email': m.email, 'no_telp': m.no_telp}
        for m in mahasiswa
    ]
    return jsonify(result)

@mahasiswa_bp.route('/mahasiswa', methods=['POST'])
def create_mahasiswa():
    data = request.form
    new_mahasiswa = User(
        nim=data['nim'],
        nama=data['nama'],
        email=data['email'],
        no_telp=data['no_telp'],
        password=hash_password(data['password']),
        role='mahasiswa'
    )
    db.session.add(new_mahasiswa)
    db.session.commit()
    return jsonify({'message': 'Mahasiswa created successfully'})

@mahasiswa_bp.route('/mahasiswa/<int:id>', methods=['DELETE'])
def delete_mahasiswa(id):
    mahasiswa = User.query.get_or_404(id)
    db.session.delete(mahasiswa)
    db.session.commit()
    return jsonify({'message': 'Mahasiswa deleted'})
