from flask import Blueprint, request
from src.database.api.services import course_service
from src.utils.jwt_helper import admin_required, login_required

course_bp = Blueprint('course', __name__, url_prefix='/api/courses')


@course_bp.route('/', methods=['POST'])
@admin_required
def create_course():
    data = request.get_json()
    semester = data.get('semester')  # "ganjil" / "genap"
    course_code = data.get('course_code')
    academic_year = data.get('academic_year')
    course_name = data.get('course_name')

    course, error = course_service.create_course(
        semester, course_code, academic_year, course_name)
    if error:
        return {"message": error}, 400

    return {
        "message": "Course created successfully",
        "course": {
            "id": course.id,
            "semester": course.semester,
            "course_code": course.course_code,
            "academic_year": course.academic_year,
            "course_name": course.course_name
        }
    }, 201


@course_bp.route('/', methods=['GET'])
@login_required
def list_courses():
    courses = course_service.get_all_courses()
    course_list = [{
        "id": c.id,
        "semester": c.semester,
        "course_code": c.course_code,
        "academic_year": c.academic_year,
        "course_name": c.course_name
    } for c in courses]

    return {"courses": course_list}, 200


@course_bp.route('/<int:course_id>', methods=['GET'])
@login_required
def get_course_detail(course_id):
    course = course_service.get_course_by_id(course_id)
    if not course:
        return {"message": "Course not found"}, 404

    return {
        "course": {
            "id": course.id,
            "semester": course.semester,
            "course_code": course.course_code,
            "academic_year": course.academic_year,
            "course_name": course.course_name
        }
    }, 200
