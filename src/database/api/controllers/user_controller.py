from flask import Blueprint, request
from src.database.api.services import user_service
from src.utils.jwt_helper import admin_required, login_required

user_bp = Blueprint('user', __name__, url_prefix='/api/users')


@user_bp.route('/', methods=['GET'])
@login_required
def list_users():
    users = user_service.get_users()
    user_list = [{
        "id": u.id,
        "nim": u.nim,
        "name": u.name,
        "email": u.email,
        "phone": u.phone
    } for u in users]

    return {"users": user_list}, 200
