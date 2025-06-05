from flask import Blueprint, request, jsonify
from database.db import get_db_connection
import json
import os

project_bp = Blueprint('project', __name__)

@project_bp.route('/save_project', methods=['POST'])
def save_project():
    data = request.get_json()
    drawing_number = data.get("drawing_number")
    revision_number = data.get("revision_number")

    if not drawing_number or not revision_number:
        return jsonify({"error": "Missing drawing number or revision"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO projects (drawing_number, revision_number, data)
        VALUES (%s, %s, %s)
    """, (drawing_number, revision_number, json.dumps(data)))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Project saved successfully"}), 201


@project_bp.route('/get_project', methods=['GET'])
def get_project():
    drawing_number = request.args.get("drawing_number")
    revision_number = request.args.get("revision_number")

    if not drawing_number or not revision_number:
        return jsonify({"error": "Missing drawing number or revision"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT data FROM projects
        WHERE drawing_number = %s AND revision_number = %s
    """, (drawing_number, revision_number))

    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if row:
        return jsonify(json.loads(row[0]))
    else:
        return jsonify({"error": "Project not found"}), 404
