import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, Float, Time
from Config.ETLconfig import Config

def create_table(engine, table_name, df):
    """
    Crea la tabla en la base de datos basada en el DataFrame proporcionado.
    """
    metadata = MetaData()

    # Definir la tabla dinámicamente basado en las columnas del DataFrame
    columns = []
    for column in df.columns:
        if df[column].dtype == 'object':
            columns.append(Column(column, String(255)))  # Definir como String para texto
        elif df[column].dtype == 'int64':
            columns.append(Column(column, Integer()))  # Definir como Integer
        elif df[column].dtype == 'float64':
            columns.append(Column(column, Float()))  # Definir como Float
        elif df[column].dtype == 'datetime64[ns]':
            columns.append(Column(column, Date()))  # Definir como Date para fechas
        elif df[column].dtype == 'timedelta64[ns]':
            columns.append(Column(column, Time()))  # Definir como Time para duración

    # Crear la tabla en la base de datos
    table = Table(table_name, metadata, *columns)
    metadata.create_all(engine)  # Crear la tabla si no existe

    print(f"Tabla '{table_name}' creada con éxito.")
    return table

def extract_data():
    """
    Extrae los datos desde el archivo CSV y crea la tabla si no existe.
    """
    # Crear la conexión a la base de datos usando SQLAlchemy
    engine = create_engine(Config.DATABASE_URI)
    
    # Cargar los datos desde el archivo CSV
    df = pd.read_csv(Config.INPUT_PATH)
    
    # Crear la base de datos y la tabla automáticamente
    table_name = 'volleyball_matches'  # Nombre de la tabla que se va a crear
    create_table(engine, table_name, df)

    # Insertar los datos en la tabla creada
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    
    print(f"Datos extraídos y cargados en la tabla '{table_name}' con éxito.")
    return df
