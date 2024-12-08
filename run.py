from app import FlaskAppFactory

# Membuat instance FlaskAppFactory dan mendapatkan aplikasi
factory = FlaskAppFactory(config_name="development")
app = factory.get_app()

if __name__ == "__main__":
    app.run(debug=True)
