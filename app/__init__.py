from flask import Flask
from sqlalchemy import text
from core.config import configurations
from core.extensions import db, migrate
from app.models import *
from app.controllers.item_controller import item_controller

def create_app(config_name="development"):
    app = Flask(__name__)

    # Konfigurasi
    app.config.from_object(configurations[config_name])

    # Inisialisasi ekstensi (db)
    db.init_app(app)
    migrate.init_app(app, db)
    
    app.register_blueprint(item_controller)

    # Membuat tabel secara otomatis saat aplikasi pertama kali dijalankan
    with app.app_context():
        db.create_all()  # Perbaiki typo: 'creatte_all' menjadi 'create_all'

    @app.route('/ping-db')
    def ping_db():
        try:
            query = text("SELECT 1")
            result = db.session.execute(query)
            return str(result.fetchone())
        except Exception as e:
            return {"error": str(e)}, 500

    return app
