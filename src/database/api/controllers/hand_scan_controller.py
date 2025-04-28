# from flask import Blueprint, request
# import os
# from werkzeug.utils import secure_filename
# from src.database.api.services import hand_scan_service
# from src.utils.jwt_helper import admin_required

# UPLOAD_FOLDER = 'src/storage/uploads'  # Sementara di folder lokal uploads/
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# hand_scan_bp = Blueprint('hand_scan', __name__, url_prefix='/api/hand-scan')


# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# @hand_scan_bp.route('/upload', methods=['POST'])
# @admin_required
# def upload_hand_scan():
#     if 'file' not in request.files:
#         return {"message": "No file part"}, 400
#     file = request.files['file']

#     if file.filename == '':
#         return {"message": "No selected file"}, 400

#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         file_path = os.path.join(UPLOAD_FOLDER, filename)

#         # Simpan file sementara
#         os.makedirs(UPLOAD_FOLDER, exist_ok=True)
#         file.save(file_path)

#         # Prediksi
#         student_id, confidence = hand_scan_service.predict_hand_owner(
#             file_path)

#         # Hapus file setelah prediksi
#         os.remove(file_path)

#         if student_id is None:
#             return {"message": "Student not recognized."}, 404

#         return {
#             "message": "Hand scan processed successfully.",
#             "student_id": student_id,
#             "confidence": confidence
#         }, 200

#     return {"message": "Invalid file type."}, 400
