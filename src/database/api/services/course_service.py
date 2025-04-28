from src.database.config import SessionLocal
from src.database.models import Course


def create_course(semester, course_code, academic_year, course_name):
    session = SessionLocal()

    existing_course = session.query(Course).filter(
        Course.course_code == course_code, Course.academic_year == academic_year).first()
    if existing_course:
        session.close()
        return None, "Course with this code and academic year already exists."

    new_course = Course(
        semester=semester,
        course_code=course_code,
        academic_year=academic_year,
        course_name=course_name
    )

    session.add(new_course)
    session.commit()
    session.refresh(new_course)
    session.close()

    return new_course, None


def get_all_courses():
    session = SessionLocal()
    courses = session.query(Course).order_by(
        Course.academic_year.desc(), Course.course_name.asc()).all()
    session.close()
    return courses


def get_course_by_id(course_id):
    session = SessionLocal()
    course = session.query(Course).filter(Course.id == course_id).first()
    session.close()
    return course
