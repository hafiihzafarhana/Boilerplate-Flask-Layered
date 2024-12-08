from flask_jwt_extended import create_access_token, create_refresh_token, decode_token
from datetime import timedelta

def generate_tokens(identity):
    access_token = create_access_token(identity=identity, expires_delta=timedelta(minutes=30))
    refresh_token = create_refresh_token(identity=identity, expires_delta=timedelta(days=7))
    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }

def decode_jwt(token):
    try:
        payload = decode_token(token)
        return payload
    except Exception as e:
        raise ValueError(f"Invalid token: {str(e)}")
