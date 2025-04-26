from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Load .env
    load_dotenv()

    # Config
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER')

    # Inisialisasi
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Import dan register blueprints (nanti kita buat)
    from app.routes.auth_routes import auth_bp
    from app.routes.mahasiswa_routes import mahasiswa_bp
    from app.routes.mata_kuliah_routes import matakuliah_bp
    from app.routes.jadwal_routes import jadwal_bp
    from app.routes.kehadiran_routes import kehadiran_bp
    from app.routes.scan_routes import scan_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(mahasiswa_bp, url_prefix='/api/mahasiswa')
    app.register_blueprint(matakuliah_bp, url_prefix='/api/matakuliah')
    app.register_blueprint(jadwal_bp, url_prefix='/api/jadwal')
    app.register_blueprint(kehadiran_bp, url_prefix='/api/kehadiran')
    app.register_blueprint(scan_bp, url_prefix='/api/scan')

    return app
