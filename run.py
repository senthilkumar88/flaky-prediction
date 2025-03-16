import logging
from flask import Flask
from app.routes import register_routes

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
