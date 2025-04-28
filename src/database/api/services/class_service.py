from src.database.config import SessionLocal
from src.database.models import Class, Course
import string


def generate_class_name(existing_classes):
    """Generate nama kelas A, B, C, dst sesuai urutan"""
    alphabet = string.ascii_uppercase  # A-Z
    return alphabet[len(existing_classes)]


def create_class(course_id):
    session = SessionLocal()

    # Cek apakah course ada
    course = session.query(Course).filter(Course.id == course_id).first()
    if not course:
        session.close()
        return None, "Course not found."

    # Hitung berapa kelas yang sudah ada di course ini
    existing_classes = session.query(Class).filter(
        Class.course_id == course_id).order_by(Class.name.asc()).all()

    # Generate nama baru (A, B, C, dst)
    if len(existing_classes) >= 26:
        session.close()
        return None, "Maximum number of classes (A-Z) reached."

    class_name = generate_class_name(existing_classes)

    new_class = Class(
        course_id=course_id,
        name=class_name
    )

    session.add(new_class)
    session.commit()
    session.refresh(new_class)
    session.close()

    return new_class, None


def get_classes_by_course(course_id):
    session = SessionLocal()
    classes = session.query(Class).filter(
        Class.course_id == course_id).order_by(Class.name.asc()).all()
    session.close()
    return classes


def get_class_by_id(class_id):
    session = SessionLocal()
    class_obj = session.query(Class).filter(Class.id == class_id).first()
    session.close()
    return class_obj
