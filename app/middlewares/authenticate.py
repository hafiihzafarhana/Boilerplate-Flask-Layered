from functools import wraps
from flask import request, jsonify
from app.utils.jwt import decode_jwt

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
            # Decode token menggunakan fungsi decode_jwt dari utils
            decoded_token = decode_jwt(token)  # Mendekodekan token
            
            # Dapatkan 'identity' dari payload yang terkandung di dalam token
            current_user = decoded_token['identity']  # Atau data lain yang Anda simpan di token

            # Menyimpan data pengguna di request untuk digunakan di handler
            request.current_user = current_user

        except Exception as e:
            return jsonify({'error': 'Token is invalid or expired!'}), 401

        return f(*args, **kwargs)
    return decorated
