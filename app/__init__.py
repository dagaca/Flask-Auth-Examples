"""
Initializes the Flask application with all modules.
"""
from flask import Flask
from flasgger import Swagger
from database.database import setup_database, db
from app.rate_limiter import setup_rate_limiter

app = Flask(__name__)
app.secret_key = "random_secret_for_sessions"  # For session usage in OAuth

# Swagger Configuration
app.config['SWAGGER'] = {
    'title': 'Flask-Auth-Examples',
    'description': 'All authentication methods (JWT, Basic, API Key, Google OAuth)\n'
                   'with Rate Limiting and Logging.',
    'version': '1.0.0'
}
swagger = Swagger(app)

# Setup Database
setup_database(app)

# Rate Limiter
limiter = setup_rate_limiter(app)

# Create database tables
with app.app_context():
    db.create_all()

# Import routes
from app import routes
