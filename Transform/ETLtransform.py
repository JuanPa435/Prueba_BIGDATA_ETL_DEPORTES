from sqlalchemy import create_engine
from Config.ETLconfig import Config

def load_data(df):
    """
    Carga los datos transformados en la base de datos MySQL.
    """
    engine = create_engine(Config.DATABASE_URI)

    # Guardar el DataFrame como archivo CSV limpio
    df.to_csv(Config.OUTPUT_PATH, index=False)

    # Escribir el DataFrame en una nueva tabla de la base de datos
    df.to_sql('processed_volleyball_matches', engine, if_exists='replace', index=False)

    print(f"Datos cargados correctamente en la base de datos MySQL y guardados en {Config.OUTPUT_PATH}.")
