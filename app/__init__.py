from flask import Flask
from sqlalchemy import text
from core.config import configurations
from core.extensions import db, migrate, jwt
from app.models import *
from app.controllers.item_controller import item_controller


class FlaskAppFactory:
    def __init__(self, config_name="development"):
        """
        Inisialisasi pabrik aplikasi Flask dengan konfigurasi yang ditentukan.
        """
        self.config_name = config_name
        self.app = Flask(__name__)
        self._configure_app()
        self._initialize_extensions()
        self._register_blueprints()
        self._initialize_database()

    def _configure_app(self):
        """Konfigurasi aplikasi dari objek konfigurasi."""
        self.app.config.from_object(configurations[self.config_name])

    def _initialize_extensions(self):
        """Inisialisasi ekstensi Flask seperti database dan migrasi."""
        db.init_app(self.app)
        migrate.init_app(self.app, db)
        jwt.init_app(self.app)

    def _register_blueprints(self):
        """Daftarkan blueprint ke aplikasi Flask."""
        self.app.register_blueprint(item_controller)

    def _initialize_database(self):
        """Inisialisasi dan buat tabel database jika belum ada."""
        with self.app.app_context():
            db.create_all()  # Membuat semua tabel

    def get_app(self):
        """Mengembalikan instance aplikasi Flask."""
        return self.app
