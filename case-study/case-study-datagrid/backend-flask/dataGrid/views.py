from flask import Blueprint, jsonify
from .service import load_insurance_data

insurance_bp = Blueprint("insurance", __name__)

@insurance_bp.route("/api/insurance", methods=['GET'])
def get_insurance_data():
    try:
        data = load_insurance_data()
        if not data:
            return jsonify({"error": "No data found"}), 404
        return jsonify(data)
    except Exception as e:
        print(f"Error in returning data: {str(e)}")
        return jsonify({"error": str(e)}), 500
