from website import create_app

app = create_app()

from flask import Flask
from website.auth import auth
from website.models import db  # Import the db object from models.py

from website.food import food
  # Import the food Blueprint





if __name__ == '__main__':
    app.run(debug=True)
