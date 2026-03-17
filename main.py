# from src.extract_data import extract_weather_data
# from src.load_data import load_wheather_data
# from src.transform_data import data_transformations

# import os
# from pathlib import Path
# from dotenv import load_dotenv
# import pandas as pd

# import logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# env_path = Path(__file__).resolve().parent.parent /'config' / '.env'
# load_dotenv(env_path)

# API_KEY = os.getenv('OPENWEATHER_API_KEY')

# url = f'https://api.openweathermap.org/data/2.5/weather?q=Rio de Janeiro,BR&units=metric&appid={API_KEY}'
# table_name = 'rj_weather'

# def pipeline():
#     try:
#         logging.info("ETAPA 1: Extração de dados")
#         extract_weather_data(url)

#         logging.info("ETAPA 2: Transformação de dados")
#         df = data_transformations()

#         logging.info("ETAPA 3: Carga de dados")
#         load_wheather_data(table_name, df)

#         print(f"\n {60*'='}")
#         print("Pipeline executado com sucesso!")
#         print(f"{60*'='}\n")
        
#     except Exception as e:
#         logging.error(f"Erro na execução do pipeline: {e}")
#         import traceback
#         traceback.print_exc()
#         return

# pipeline()
