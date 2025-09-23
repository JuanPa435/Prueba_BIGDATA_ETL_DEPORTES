import pandas as pd

def transform_data(df):
    """
    Transforma los datos extraídos:
    1. Convierte la columna 'date' a formato datetime.
    2. Convierte las columnas 'score' a formato adecuado y divide en dos sets.
    """
    # Convertir la columna 'date' a formato datetime
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Para el campo 'score', se asume que el formato es algo como "21-18, 21-12"
    # Convertimos esa cadena en dos columnas para cada set (si es necesario)
    
    # Usamos `fillna` para asegurar que no haya valores nulos antes de dividir
    df['score'] = df['score'].fillna('0-0, 0-0')  # Reemplazar los valores nulos con un formato de puntaje por defecto
    
    # Dividir la columna 'score' en dos sets usando `str.split()`
    # Primero verificamos si hay más de un set, y si no, se asignan valores por defecto
    df[['score_set1', 'score_set2']] = df['score'].str.split(',', expand=True, n=1)

    # Rellenar valores nulos en ambas columnas después de la división
    df['score_set1'] = df['score_set1'].fillna('0-0')
    df['score_set2'] = df['score_set2'].fillna('0-0')

    # Limpiar las columnas de puntajes, asegurándose de que cada puntaje esté en el formato esperado
    df['score_set1'] = df['score_set1'].apply(lambda x: x.strip().replace('-', '') if isinstance(x, str) else '0')  # Limpiar y quitar '-'
    df['score_set2'] = df['score_set2'].apply(lambda x: x.strip().replace('-', '') if isinstance(x, str) else '0')  # Limpiar y quitar '-'

    # Ahora, intentamos convertir estos valores a enteros si son válidos
    df['score_set1'] = pd.to_numeric(df['score_set1'], errors='coerce')  # Convertir a número
    df['score_set2'] = pd.to_numeric(df['score_set2'], errors='coerce')  # Convertir a número

    # Asegurarnos de que los valores nulos sean reemplazados por ceros si no son válidos
    df['score_set1'] = df['score_set1'].fillna(0).astype(int)
    df['score_set2'] = df['score_set2'].fillna(0).astype(int)

    print("Datos transformados con éxito.")
    return df
