from flask import Blueprint, request, jsonify
from app.models.riwayat_kehadiran_model import Kehadiran
from app import db

kehadiran_bp = Blueprint('kehadiran', __name__)

@kehadiran_bp.route('/kehadiran', methods=['GET'])
def get_kehadiran():
    kehadiran = Kehadiran.query.all()
    result = [
        {'id': k.id, 'user_id': k.user_id, 'jadwal_id': k.jadwal_id, 'status': k.status, 'tanggal': k.tanggal}
        for k in kehadiran
    ]
    return jsonify(result)
