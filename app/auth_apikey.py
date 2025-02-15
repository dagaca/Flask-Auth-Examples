"""
Handles API Key authentication for API security.
"""
import os
from flask import request, jsonify
from functools import wraps
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")  # Read API Key from .env

def api_key_required(f):
    """
    Decorator function to enforce API Key authentication.

    This decorator checks for a valid API key in the `X-API-KEY` header.
    If the API key is missing or invalid, the request is rejected with a 401 Unauthorized error.

    Usage:
        - Apply as `@api_key_required` on protected routes.
        - Clients must send the API key in the `X-API-KEY` header.

    Args:
        f (function): The protected route function.

    Returns:
        function: The decorated function with API key validation.

    Raises:
        401 Unauthorized:
            - If the API key is missing.
            - If the API key is invalid.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key = request.headers.get("X-API-KEY")

        if not api_key:
            return jsonify({"message": "Missing API Key"}), 401

        if api_key != API_KEY:
            return jsonify({"message": "Invalid API Key"}), 401

        return f(*args, **kwargs)

    return decorated
