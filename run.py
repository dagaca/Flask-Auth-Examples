"""
Runs the Flask authentication application.
"""
from app import app

if __name__ == '__main__':
    app.run(debug=True, port=8080)
