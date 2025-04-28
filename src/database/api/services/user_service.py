from src.database.config import SessionLocal
from src.database.models import User


def get_users():
    session = SessionLocal()
    users = session.query(User).filter(
        User.role == 'user').order_by(User.nim.asc()).all()
    session.close()
    return users
