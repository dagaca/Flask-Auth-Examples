"""
Database configuration and user model for authentication.
"""
import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

def setup_database(app):
    """
    Configures and initializes the database connection.
    
    This function sets up SQLAlchemy and binds it to the Flask application.
    The database URL is loaded from the environment variable `DATABASE_URL`,
    defaulting to an SQLite database if not provided.
    
    Args:
        app (Flask): The Flask application instance.
    
    Returns:
        None
    """
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///users.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

class User(db.Model):
    """
    Represents a registered user in the system.
    
    Attributes:
        id (int): Primary key.
        username (str): Unique username of the user (required).
        email (str): Unique email address of the user (required).
        password (str): Hashed password for authentication (optional).
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=True)
