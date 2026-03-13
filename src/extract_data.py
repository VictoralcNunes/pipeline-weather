import requests
import json
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

api_key = "3771d759db50f472dc235c6753adf851"
url = f'https://api.openweathermap.org/data/2.5/weather?q=Rio de Janeiro,BR&units=metric&appid={api_key}' 

def extract_weather_data(url: str) -> list:
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        logging.error("erro na requisição")
        return []
    
    if not data:
        logging.error("Nenhum dado retornado pela API")
        return []

    output_path = 'data/weather_data.json'
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)

    logging.info(f"Arquivo salvo em {output_path}")
    return data
