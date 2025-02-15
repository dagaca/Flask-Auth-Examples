# FlaskAPI-Secure

FlaskAPI-Secure is a **secure, scalable, and modular Flask API** that provides **JWT authentication, OAuth 2.0 login (Google), and rate limiting**. It ensures **secure access to API endpoints** while following best practices for authentication and API management.

---

## **🔐 Features**
- ✅ **JWT Authentication** (Secure user login & token-based access)
- ✅ **Google OAuth 2.0 Login** (Social authentication)
- ✅ **Rate Limiting** (Prevents excessive API requests)
- ✅ **Database Integration** (User management with SQLite/PostgreSQL/MySQL)
- ✅ **Swagger API Documentation** (Interactive API docs)
- ✅ **Modular Code Structure** (Separation of concerns)
- ✅ **Logging System** (Request/response tracking with log rotation)

---

## **📦 Installation**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/FlaskAPI-Secure.git
cd FlaskAPI-Secure
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Setup Environment Variables**
Create a **.env** file in the root directory and add:
```ini
# JWT Secret Key
SECRET_KEY=supersecretkey

# Database Settings
DATABASE_URL=sqlite:///users.db  # Change to PostgreSQL or MySQL if needed

# Rate Limit Configuration
RATE_LIMIT=5 per minute

# OAuth 2.0 Configuration (Google)
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
GOOGLE_REDIRECT_URI=http://localhost:5000/google/callback

# Logging Configuration
LOG_DIR=logs
LOG_FILE=api.log
```

### **5️⃣ Initialize the Database**
```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

### **6️⃣ Run the Application**
```bash
python run.py
```
The API will be accessible at: **http://localhost:5000**

---

## **🛠️ API Endpoints**

### **🔹 User Authentication (JWT)**
#### **Register a User**
```http
POST /register
```
**Request Body:**
```json
{
    "username": "johndoe",
    "email": "johndoe@example.com",
    "password": "securepassword"
}
```
**Response:**
```json
{
    "message": "User registered successfully"
}
```

#### **User Login**
```http
POST /login
```
**Request Body:**
```json
{
    "email": "johndoe@example.com",
    "password": "securepassword"
}
```
**Response:**
```json
{
    "token": "your-jwt-token"
}
```

#### **Access Protected Route**
```http
GET /protected
Authorization: Bearer <your-jwt-token>
```
**Response:**
```json
{
    "message": "Welcome, User 1!"
}
```

### **🔹 Google OAuth 2.0 Login**
#### **Redirect to Google Login**
```http
GET /google/login
```

#### **Google OAuth Callback**
```http
GET /google/callback
```

### **🔹 Rate-Limited Endpoint**
#### **Test Rate Limiting**
```http
GET /limited
```
**Response if exceeded:**
```json
{
    "message": "Too many requests"
}
```

---

## **🌍 Swagger API Documentation**
Once the API is running, **Swagger documentation** is available at:
🔗 **http://localhost:8080/apidocs**

---

## **📂 Project Structure**
```
FlaskAPI-Secure/
│── app/
│   ├── __init__.py    # Initializes Flask, database, OAuth, rate limiter, logging
│   ├── auth.py        # JWT authentication & token validation
│   ├── database.py    # User model & database setup
│   ├── oauth.py       # Google OAuth authentication
│   ├── rate_limiter.py # API rate limiting
│   ├── log_config.py  # Logging system
│   ├── routes.py      # API endpoints
│── .env               # Environment variables
│── requirements.txt   # Required dependencies
│── run.py             # Application entry point
│── logs/              # API log files
```

---

## **🙌 Contributing**
Contributions are welcome! Feel free to:
- ⭐ Star this repository
- 🛠️ Fork and enhance it
- 🔀 Submit a pull request

---

## **📜 License**
This project is licensed under the **MIT License**.

---
