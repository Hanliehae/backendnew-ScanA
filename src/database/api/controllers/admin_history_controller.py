from flask import Blueprint, request
from src.database.api.services import admin_history_service
from src.utils.jwt_helper import admin_required

admin_history_bp = Blueprint(
    'admin_history', __name__, url_prefix='/api/admin/history')


@admin_history_bp.route('/', methods=['GET'])
@admin_required
def all_attendance_history():
    course_id = request.args.get('course_id', type=int)
    student_id = request.args.get('student_id', type=int)
    semester = request.args.get('semester')
    year = request.args.get('year', type=int)
    status = request.args.get('status')

    attendance_list = admin_history_service.get_all_attendance_history(
        course_id=course_id,
        student_id=student_id,
        semester=semester,
        year=year,
        status=status
    )

    result = []
    for attendance in attendance_list:
        meeting = attendance.meeting
        class_ = meeting.class_
        course = class_.course
        student = attendance.class_student.student

        result.append({
            "student_id": student.id,
            "student_name": student.name,
            "course_name": course.name,
            "course_id": course.id,
            "semester": course.semester,
            "academic_year": course.academic_year,
            "meeting_date": meeting.date.strftime('%Y-%m-%d'),
            "meeting_start_time": meeting.start_time,
            "meeting_end_time": meeting.end_time,
            "check_in_time": attendance.check_in_time.strftime('%H:%M') if attendance.check_in_time else None,
            "check_out_time": attendance.check_out_time.strftime('%H:%M') if attendance.check_out_time else None,
            "status": attendance.status
        })

    return {"history": result}, 200
