from src.database.config import SessionLocal
from src.database.models import Attendance, Meeting, StudentClass
from datetime import datetime


def mark_attendance(meeting_id, student_id, scan_type):
    session = SessionLocal()

    # Pastikan meeting ada
    meeting = session.query(Meeting).filter(Meeting.id == meeting_id).first()
    if not meeting:
        session.close()
        return None, "Meeting not found."

    # Cek apakah mahasiswa terdaftar di kelas meeting
    student_class = session.query(StudentClass).filter(
        StudentClass.student_id == student_id,
        StudentClass.class_id == meeting.class_id
    ).first()

    if not student_class:
        session.close()
        return None, "Student is not assigned to this class."

    # Cek apakah sudah ada attendance record
    attendance = session.query(Attendance).filter(
        Attendance.meeting_id == meeting_id,
        Attendance.student_id == student_id
    ).first()

    if not attendance:
        attendance = Attendance(
            meeting_id=meeting_id,
            student_id=student_id
        )
        session.add(attendance)
        session.commit()
        session.refresh(attendance)

    now = datetime.now()

    if scan_type == "in":
        if attendance.check_in_time is None:
            attendance.check_in_time = now
    elif scan_type == "out":
        if attendance.check_out_time is None:
            attendance.check_out_time = now
    else:
        session.close()
        return None, "Invalid scan_type. Must be 'in' or 'out'."

    # Update status
    if attendance.check_in_time:
        attendance.status = "Present"

    session.commit()
    session.refresh(attendance)
    session.close()

    return attendance, None


def get_attendance_by_meeting(meeting_id):
    session = SessionLocal()

    attendances = session.query(Attendance).filter(
        Attendance.meeting_id == meeting_id
    ).all()

    session.close()
    return attendances
