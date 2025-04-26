from flask import Blueprint, request, jsonify
from app.services.scan_service import predict_palm
from app.utils.file_handler import save_uploaded_file

scan_bp = Blueprint('scan', __name__)

@scan_bp.route('/scan', methods=['POST'])
def scan_palm():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    file = request.files['file']
    filename = save_uploaded_file(file, 'palm_right')  # contoh, kanan
    prediction = predict_palm(filename)
    return jsonify({'result': prediction})
