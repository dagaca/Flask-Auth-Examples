"""
Sets up rate limiting from .env (in-memory).
"""
import os
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv

load_dotenv()
RATE_LIMIT = os.getenv("RATE_LIMIT")

def setup_rate_limiter(app):
    """
    Initializes and applies rate limiting to the given Flask application.

    This function sets up Flask-Limiter with the specified request limit per IP address.
    The rate limit is dynamically retrieved from the environment variable RATE_LIMIT.

    Args:
        app (Flask): The Flask application instance.

    Returns:
        Limiter: The configured rate limiter object.
    """
    limiter = Limiter(
        key_func=get_remote_address,  # Limits based on the client's IP address
        default_limits=[RATE_LIMIT]   # Rate limit retrieved from .env
    )
    limiter.init_app(app)
    return limiter
