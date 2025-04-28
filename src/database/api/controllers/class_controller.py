from flask import Blueprint, request
from src.database.api.services import class_service
from src.utils.jwt_helper import admin_required, login_required

class_bp = Blueprint('class', __name__, url_prefix='/api/classes')


@class_bp.route('/create', methods=['POST'])
@admin_required
def create_class():
    data = request.get_json()
    course_id = data.get('course_id')

    class_obj, error = class_service.create_class(course_id)
    if error:
        return {"message": error}, 400

    return {
        "message": "Class created successfully",
        "class": {
            "id": class_obj.id,
            "name": class_obj.name,
            "course_id": class_obj.course_id
        }
    }, 201


@class_bp.route('/by-course/<int:course_id>', methods=['GET'])
@login_required
def get_classes_by_course(course_id):
    classes = class_service.get_classes_by_course(course_id)
    class_list = [{
        "id": c.id,
        "name": c.name,
        "course_id": c.course_id
    } for c in classes]

    return {"classes": class_list}, 200


@class_bp.route('/<int:class_id>', methods=['GET'])
@login_required
def get_class_detail(class_id):
    class_obj = class_service.get_class_by_id(class_id)
    if not class_obj:
        return {"message": "Class not found"}, 404

    return {
        "class": {
            "id": class_obj.id,
            "name": class_obj.name,
            "course_id": class_obj.course_id
        }
    }, 200
