# backend/controllers/auth_controller.py
from flask import Blueprint, request, jsonify
from services.encryption_service import hash_password, check_password
from database.db import get_db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get('name')
    password = data.get('password')

    if not name or not password:
        return jsonify({'message': 'Name and password required'}), 400

    hashed_pw = hash_password(password)
    conn = get_db()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (name, password, role) VALUES (%s, %s, %s)", (name, hashed_pw, 'user'))
        conn.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except:
        conn.rollback()
        return jsonify({'message': 'User already exists'}), 409

@auth_bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    name = data.get('name')
    password = data.get('password')

    conn = get_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE name = %s", (name,))
    user = cursor.fetchone()

    if user and check_password(password, user['password']):
        return jsonify({
            'message': 'Login successful',
            'name': user['name'],
            'role': user['role']
        }), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401
