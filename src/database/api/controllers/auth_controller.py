from flask import Blueprint, request
from src.database.api.services import auth_service
from src.utils.jwt_helper import login_required, admin_required

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    token, error = auth_service.login(username, password)
    if error:
        return {"message": error}, 401

    return {"access_token": token}, 200


@auth_bp.route('/register-student', methods=['POST'])
@admin_required
def register_student():
    data = request.get_json()
    nim = data.get('nim')
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    hand_left_path = data.get('hand_left_path')
    hand_right_path = data.get('hand_right_path')

    result, error = auth_service.register_student(
        nim, name, email, phone, hand_left_path, hand_right_path)
    if error:
        return {"message": error}, 400

    return {"message": "Student registered successfully", "credentials": result}, 201
