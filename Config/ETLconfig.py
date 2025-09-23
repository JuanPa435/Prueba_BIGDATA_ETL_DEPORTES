import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DATABASE_URI = os.getenv('DATABASE_URI')
    INPUT_PATH = os.getenv('INPUT_PATH', 'Data/BeachVolleyball.csv')  
    OUTPUT_PATH = os.getenv('OUTPUT_PATH', 'Data/BeachVolleyball_Limpio.csv')
