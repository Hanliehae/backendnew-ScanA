from src.database.config import SessionLocal
from src.database.models import Attendance
from src.database.models import Meeting
from src.database.models import Course
from sqlalchemy.orm import joinedload

db = SessionLocal()


def get_attendance_history(student_id, course_id=None, semester=None, year=None):
    query = db.query(Attendance).join(Attendance.meeting).join(Meeting.course).options(
        joinedload(Attendance.meeting).joinedload(Meeting.course)
    ).filter(Attendance.student_id == student_id)

    if course_id:
        query = query.filter(Meeting.course_id == course_id)
    if semester:
        query = query.filter(Course.semester == semester)
    if year:
        query = query.filter(Course.academic_year == year)

    return query.all()
