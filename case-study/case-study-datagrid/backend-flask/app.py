from flask import Flask, jsonify
from flask_cors import CORS
import json 
import os 
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)

#loading insurance data 
def load_insurance_data() : 
    try : 
        json_path = os.getenv("DATA_PATH")
        with open(json_path, 'r', encoding = 'utf-8') as file : 
            data = json.load(file)
            return data
    except Exception as e : 
        print(f"Error in loading data {str(e)}")
        return []

@app.route("/api/insurance", methods = ['GET'])
def get_insurance_data() : 
    try : 
        data = load_insurance_data()
        if not data : 
            return jsonify({"error" : "No data found"}), 404
        return jsonify(data)
    
    except Exception as e : 
        print(f"Error in returning data : {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__" : 
    app.run(debug = True, port = 5000)
