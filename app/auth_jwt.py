"""
Handles JWT authentication for API security.
"""
import os
import jwt
import datetime
from flask import request, jsonify
from functools import wraps
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")

def generate_token(user):
    """
    Generates a JWT token for authentication.

    This function creates a JWT token that includes:
    - The user ID as the `sub` (subject).
    - Issued time (`iat`).
    - Expiration time (`exp`), set to 1 hour from creation.

    Args:
        user (object): The user object, which should have an `id` attribute.

    Returns:
        str: A JWT token encoded with `HS256` algorithm.
    """
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        'iat': datetime.datetime.utcnow(),
        'sub': str(user.id)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def token_required(f):
    """
    Decorator function to validate JWT tokens.

    This decorator checks for a valid JWT token in the `Authorization` header.
    It extracts and decodes the token, verifying its integrity and expiration.

    Usage:
        - Apply as `@token_required` on protected routes.
        - Clients must send the token in the `Authorization` header as "Bearer <JWT_TOKEN>".

    Args:
        f (function): The protected route function.

    Returns:
        function: The decorated function with token validation.

    Raises:
        401 Unauthorized:
            - If the token is missing or improperly formatted.
            - If the token has expired.
            - If the token is invalid.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization', '')
        if not auth_header.startswith("Bearer "):
            return jsonify({'message': 'Invalid token format'}), 401

        token = auth_header.split("Bearer ")[1]

        try:
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            request.user_id = decoded_token['sub']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401

        return f(*args, **kwargs)
    return decorated
