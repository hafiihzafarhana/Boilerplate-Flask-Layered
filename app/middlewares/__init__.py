from functools import wraps
from flask import request, jsonify
import jwt

# Kunci rahasia untuk JWT
SECRET_KEY = "your_secret_key"

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Token dikirimkan melalui header Authorization
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]  # "Bearer <token>"
        
        if not token:
            return jsonify({'error': 'Token is missing!'}), 401

        try:
            # Decode token
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            # Opsional: Anda bisa melakukan validasi tambahan di sini
            request.user = data  # Simpan data user di request
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid token!'}), 401

        return f(*args, **kwargs)
    return decorated
