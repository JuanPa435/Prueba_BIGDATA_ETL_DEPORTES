from Extract.ETLextract import extract_data
from Transform.ETLtransform import transform_data
from Load.ETLload import load_data
from Transform.Visualizations import generate_graphs

# Ejecutar el flujo ETL
df = extract_data()
df = transform_data(df)
load_data(df)

# Generar las gráficas
generate_graphs(df)
