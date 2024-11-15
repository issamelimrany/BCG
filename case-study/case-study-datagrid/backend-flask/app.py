from flask import Flask
from flask_cors import CORS
from dataGrid.views import insurance_bp

app = Flask(__name__)
CORS(app)

# Register Blueprints
app.register_blueprint(insurance_bp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
