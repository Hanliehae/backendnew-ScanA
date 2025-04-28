from src.database.config import SessionLocal
from src.database.models import Meeting, Class
from datetime import datetime


def create_meeting(class_id, date, start_time, end_time):
    session = SessionLocal()

    # Pastikan kelas ada
    class_obj = session.query(Class).filter(Class.id == class_id).first()
    if not class_obj:
        session.close()
        return None, "Class not found."

    # Buat pertemuan baru
    new_meeting = Meeting(
        class_id=class_id,
        date=date,
        start_time=start_time,
        end_time=end_time
    )
    session.add(new_meeting)
    session.commit()

    session.refresh(new_meeting)
    session.close()

    return new_meeting, None


def get_meetings_by_class(class_id):
    session = SessionLocal()
    meetings = session.query(Meeting).filter(
        Meeting.class_id == class_id).order_by(Meeting.date.asc()).all()
    session.close()
    return meetings
