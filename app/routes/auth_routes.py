from flask import Blueprint, request, jsonify
from app.models.user import User  # pastikan path ini sesuai modelmu
from app.utils.auth_helper import verify_password, generate_token
from app.models import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or not data.get('email') or not data.get('password'):
        return jsonify({"message": "Email dan Password wajib diisi."}), 400

    email = data.get('email')
    password = data.get('password')

    # Cek user dari database
    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"message": "Email tidak ditemukan."}), 404

    # Cek password
    if not verify_password(user.password, password):
        return jsonify({"message": "Password salah."}), 401

    # Jika sukses, buat token
    access_token = generate_token(identity={"id": user.id, "role": user.role})

    return jsonify({
        "access_token": access_token,
        "user": {
            "id": user.id,
            "name": user.nama,  # pastikan field 'nama' ada di User model
            "email": user.email,
            "role": user.role
        }
    }), 200
