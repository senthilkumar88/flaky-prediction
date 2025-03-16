import logging
from app import create_app
from app.storage import init_db

logging.basicConfig(level=logging.INFO)

# Initialize the database
init_db()

# Create and run the Flask app
app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
