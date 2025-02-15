"""
Defines all authentication routes in one file with logging and Swagger documentation.
"""
from flask import request, jsonify
from app import app, limiter
from database.database import db, User
from app.auth_jwt import generate_token, token_required
from app.auth_basic import auth
from app.auth_apikey import api_key_required
from app.rate_limiter import RATE_LIMIT
from config.log_config import configure_logging, log_request_info, log_response_info

# Configure logging
configure_logging(app)
log_request_info(app)
log_response_info(app)

# ========== HEALTH CHECK ==========
@app.route("/health", methods=["GET"])
def health_check():
    """
    FAE-001 (Health Check)
    This endpoint performs a health check to verify that the service is running correctly.

    -------
    tags:
      - System
    responses:
      '200':
        description: Service is healthy.
        content:
          application/json:
            schema:
              type: object
              properties:
                healthy:
                  type: string
                  example: Ok
    """
    app.logger.info("✅ Health check endpoint accessed.")
    return jsonify({"healthy": "Ok"}), 200


# ========== USER REGISTRATION (JWT) ==========
@app.route('/register', methods=['POST'])
def register():
    """
    FAE-101 (User Registration)
    Registers a new user with email and password.

    -------
    tags:
      - Authentication
    parameters:
      - in: body
        name: body
        required: true
        description: JSON object containing user details.
        schema:
          type: object
          properties:
            username:
              type: string
              description: Unique username for the user.
            email:
              type: string
              description: User's email address.
            password:
              type: string
              description: User's password.
    responses:
      '201':
        description: User registered successfully.
      '400':
        description: Email already registered.
    """
    data = request.get_json() or {}
    app.logger.info(f"📥 Register attempt: {data}")

    if User.query.filter_by(email=data.get('email')).first():
        app.logger.warning(f"⚠️ Registration failed: Email {data.get('email')} already exists.")
        return jsonify({'message': 'Email already registered'}), 400

    new_user = User(
        username=data.get('username'),
        email=data.get('email'),
        password=data.get('password')
    )
    db.session.add(new_user)
    db.session.commit()

    app.logger.info(f"✅ User registered successfully: {new_user.email}")
    return jsonify({'message': 'User registered successfully'}), 201


# ========== USER LOGIN (JWT) ==========
@app.route('/login', methods=['POST'])
def login():
    """
    FAE-102 (User Login)
    Authenticates a user and provides a JWT token.

    -------
    tags:
      - Authentication
    parameters:
      - in: body
        name: body
        required: true
        description: JSON object containing login credentials.
        schema:
          type: object
          properties:
            email:
              type: string
              description: User's registered email.
            password:
              type: string
              description: User's password.
    responses:
      '200':
        description: Returns JWT token.
        content:
          application/json:
            schema:
              type: object
              properties:
                token:
                  type: string
                  description: JWT authentication token.
      '401':
        description: Invalid credentials.
    """
    data = request.get_json() or {}
    app.logger.info(f"📥 Login attempt: {data.get('email')}")

    user = User.query.filter_by(email=data.get('email')).first()
    if user and user.password == data.get('password'):
        token = generate_token(user)
        app.logger.info(f"✅ User {user.email} logged in successfully.")
        return jsonify({'token': token}), 200

    app.logger.warning(f"⚠️ Invalid login attempt for email: {data.get('email')}")
    return jsonify({'message': 'Invalid credentials'}), 401


# ========== PROTECTED (JWT + Rate Limit from .env) ==========
@app.route('/protected', methods=['GET'])
@limiter.limit(RATE_LIMIT)
@token_required
def protected():
    """
    FAE-203 (Protected Route)
    This endpoint is protected by JWT token and is rate-limited.

    -------
    tags:
      - Authentication
    parameters:
      - in: header
        name: Authorization
        required: true
        description: Bearer <JWT_TOKEN>.
        schema:
          type: string
    responses:
      '200':
        description: Authorized access.
      '401':
        description: Unauthorized.
      '429':
        description: Too many requests.
    """
    app.logger.info(f"🔒 Protected route accessed by User ID: {request.user_id}")
    return jsonify({'message': f'Welcome, User {request.user_id}!'}), 200


# ========== BASIC AUTH ==========
@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """
    FAE-301 (Basic Auth Protected Route)
    This endpoint requires Basic Authentication.

    -------
    tags:
      - Authentication
    responses:
      '200':
        description: Authorized access.
      '401':
        description: Unauthorized.
    """
    app.logger.info(f"🔐 Basic auth accessed by: {auth.current_user()}")
    return jsonify({'message': f'Welcome, {auth.current_user()}!'}), 200


# ========== API KEY ==========
@app.route('/apikey-protected', methods=['GET'])
@api_key_required
def apikey_protected():
    """
    FAE-401 (API Key Protected Route)
    This endpoint requires an API Key.

    -------
    tags:
      - Authentication
    parameters:
      - in: header
        name: X-API-KEY
        required: true
        description: Your API key from .env.
        schema:
          type: string
    responses:
      '200':
        description: Authorized access.
      '401':
        description: Invalid or missing API key.
    """
    app.logger.info("🔑 API Key authentication successful.")
    return jsonify({'message': 'Welcome, API user!'}), 200
