import seaborn as sns
import matplotlib.pyplot as plt

def generate_graphs(df):
    
    import os
    output_dir = 'Data'
    os.makedirs(output_dir, exist_ok=True)

    if 'gender' in df.columns and 'country' in df.columns:
        conteo_genero_pais = df.groupby(['country', 'gender']).size().reset_index(name='count')
        plt.figure(figsize=(10, 6))
        sns.barplot(x='country', y='count', hue='gender', data=conteo_genero_pais)
        plt.title('Cantidad de Mujeres y Hombres por País')
        plt.xlabel('País')
        plt.ylabel('Cantidad')
        plt.legend(title='Género')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'grafica1.png'))
        plt.close()


    if 'date' in df.columns:
        df['year'] = df['date'].dt.year
        partidos_por_anio = df.groupby('year').size().reset_index(name='match_num')
        plt.figure(figsize=(6, 4))
        sns.barplot(x='year', y='match_num', data=partidos_por_anio, color='purple')
        plt.title('Cantidad de Partidos por Año')
        plt.xlabel('Año')
        plt.ylabel('Número de Partidos')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'grafica2.png'))
        plt.close()
    
    if 'date' in df.columns and 'score_set1' in df.columns and 'gender' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='date', y='score_set1', hue='gender', data=df)
        plt.title('Puntaje del Set 1 a lo largo del tiempo por Género')
        plt.xlabel('Fecha')
        plt.ylabel('Puntaje Set 1')
        plt.legend(title='Género')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'grafica3.png'))
        plt.close()