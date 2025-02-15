# 🔐 Flask Auth Examples (FAE)

**Flask Auth Examples (FAE)** is a **Flask API project** demonstrating various **authentication methods** such as **JWT, Basic Authentication, and API Key Authentication**. It also integrates **Rate Limiting, Logging, and API Documentation with Swagger** to ensure security and maintainability.

---

## 📌 Features
✔️ **JWT Authentication** – Secure user authentication with JSON Web Tokens  
✔️ **Basic Authentication** – Username and password authentication  
✔️ **API Key Authentication** – API key-based authentication for secure API access  
✔️ **Rate Limiting** – Prevent abuse by restricting request rates  
✔️ **Logging** – Logs API requests and responses for debugging and monitoring  
✔️ **Swagger UI** – Provides an interactive API documentation  
✔️ **Flask-SQLAlchemy** – ORM for database management  

---

## 🚀 Installation & Setup
### 1️⃣ **Prerequisites**
Before running the project, ensure you have the following:
- Python **3.8+**
- pip
- **virtualenv** (recommended for isolated environments)

### 2️⃣ **Clone the Repository**
```bash
git clone https://github.com/dagaca/Flask-Auth-Examples.git
cd Flask-Auth-Examples
```

### 3️⃣ **Create a Virtual Environment (Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 4️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 5️⃣ **Create a .env File**
Set up the `.env` file with the following variables:
```ini
DATABASE_URL=your_database_url_here
SECRET_KEY=your_secret_key_here

LOG_DIR=your_log_directory_here
LOG_FILE=your_log_file_name_here

RATE_LIMIT=your_rate_limit_here (e.g., 5 per minute)

BASIC_USER=your_basic_auth_username
BASIC_PASS=your_basic_auth_password
API_KEY=your_api_key_here
```

---

## ▶️ **Running the Application**
Start the Flask application:
```bash
python run.py
```
The API will be available at **http://127.0.0.1:8080**.

---

## 📖 **API Documentation (Swagger UI)**
Access the **Swagger UI** at **http://127.0.0.1:8080/apidocs/** to explore available endpoints and their specifications.

---

## 🔑 **Authentication Methods**

### **1️⃣ JWT Authentication**
#### **📌 User Registration**
📍 **POST** `/register`
```json
{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "Secret123"
}
```

#### **📌 User Login (JWT Token Retrieval)**
📍 **POST** `/login`
```json
{
  "email": "john@example.com",
  "password": "Secret123"
}
```
✅ **Response:**
```json
{
  "token": "your_jwt_token_here"
}
```

#### **📌 Accessing a JWT-Protected Endpoint**
📍 **GET** `/protected`  
🔹 **Headers:**
```http
Authorization: Bearer your_jwt_token_here
```
✅ **Response:**
```json
{
  "message": "Welcome, User 1!"
}
```

---

### **2️⃣ Basic Authentication**
📍 **GET** `/basic-protected`  
🔹 **Headers:**
```http
Username: admin
Password: adminpass
```
✅ **Response:**
```json
{
  "message": "Welcome, admin!"
}
```

---

### **3️⃣ API Key Authentication**
📍 **GET** `/apikey-protected`  
🔹 **Headers:**
```http
X-API-KEY: your_api_key_here
```
✅ **Response:**
```json
{
  "message": "Welcome, API user!"
}
```

---

## ⚠️ **Rate Limiting**
Endpoints are restricted based on the `.env` rate limit setting:
```ini
RATE_LIMIT=your_rate_limit_here (e.g., 5 per minute)
```
📍 **GET** `/protected`  
⏳ **Exceeding the limit results in:**
```json
{
  "message": "Too many requests"
}
```

---

## 📝 **Logging**
All requests and responses are logged for monitoring and debugging.
✅ **Example Log Output:**
```bash
2025-02-15 22:41:19,089 - app - INFO - Request URL: http://127.0.0.1:8080/protected
2025-02-15 22:41:19,089 - app - INFO - Request Method: GET
2025-02-15 22:41:19,089 - app - INFO - Authorization: Bearer eyJhbGciOiJI...
2025-02-15 22:41:19,092 - app - INFO - User ID: 1 Access Granted
```

---

## 🛠 **Technologies Used**
| Technology         | Description |
|-------------------|-------------|
| **Flask**         | Python web framework |
| **Flasgger**      | API documentation (Swagger UI) |
| **Flask-SQLAlchemy** | ORM for database management |
| **Flask-Limiter** | API Rate Limiting |
| **Flask-HTTPAuth** | Basic Authentication |
| **PyJWT**         | JWT Token management |

---

## 📜 **License**
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

