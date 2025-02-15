"""
Handles Basic Authentication for API security.
"""
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize HTTP Basic Auth
auth = HTTPBasicAuth()

# Example in-memory user storage (for demonstration purposes)
users = {
    "admin": generate_password_hash("adminpass"),
    "testuser": generate_password_hash("testpass")
}

@auth.verify_password
def verify_password(username, password):
    """
    Verifies the provided username and password.
    
    This function checks if the given username exists and verifies the password
    against the stored hashed password.
    
    Args:
        username (str): The username provided by the client.
        password (str): The plaintext password provided by the client.
    
    Returns:
        str: The authenticated username if verification is successful.
        None: If authentication fails.
    
    Raises:
        401 Unauthorized:
            - If the username is not found.
            - If the password does not match.
    """
    if username in users and check_password_hash(users[username], password):
        return username
    return None
