import json
from config.settings import Config

def load_insurance_data():
    try:
        with open(Config.DATA_PATH, 'r', encoding='utf-8') as file:
            data = json.load(file)
            # CSV or excel
            # data = pd.read_csv(Config.DATA_PATH).to_dict(orient="records")
            # data = pd.read_excel(Config.DATA_PATH, engine="openpyxl").to_dict(orient="records")
            return data
    except Exception as e:
        print(f"Error in loading data: {str(e)}")
        return []
