from src.database.config import SessionLocal
from src.database.models import Attendance, Meeting, Course, ClassStudent, Class
from sqlalchemy.orm import joinedload

db = SessionLocal()


def get_all_attendance_history(course_id=None, student_id=None, semester=None, year=None, status=None):
    query = db.query(Attendance)\
        .join(Attendance.meeting)\
        .join(Meeting.class_)\
        .join(Class.course)\
        .join(Attendance.class_student)\
        .join(ClassStudent.student)\
        .options(
            joinedload(Attendance.meeting).joinedload(
                Meeting.class_).joinedload(Class.course),
            joinedload(Attendance.class_student).joinedload(
                ClassStudent.student)
    )

    if course_id:
        query = query.filter(Class.course_id == course_id)
    if student_id:
        query = query.filter(ClassStudent.student_id == student_id)
    if semester:
        query = query.filter(Course.semester == semester)
    if year:
        query = query.filter(Course.academic_year == year)
    if status:
        query = query.filter(Attendance.status == status)

    return query.all()
