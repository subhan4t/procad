# backend/app.py

from flask import Flask
from flask_cors import CORS
from controllers.auth_controller import auth_bp
from controllers.project_controller import project_bp
from database.db import init_db

app = Flask(__name__)
CORS(app)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(project_bp, url_prefix='/project')

# Initialize MySQL DB
init_db()

if __name__ == '__main__':
    app.run(debug=True)
