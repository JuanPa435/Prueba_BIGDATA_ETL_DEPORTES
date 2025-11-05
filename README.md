# Proyecto ETL de Voleibol de Playa

Este proyecto tiene como objetivo extraer, transformar y cargar (ETL) datos sobre partidos de voleibol de playa desde un archivo CSV o una base de datos MySQL. Los datos se procesan para generar visualizaciones de las estadísticas de los partidos, como la distribución de puntajes y la tendencia de puntajes a lo largo del tiempo.

## Estructura de las Ramas de Git

Este proyecto sigue un flujo de trabajo con múltiples ramas de desarrollo:

### 1. **`main`**
- Esta es la rama principal. Aquí se encuentra el código estable y listo para producción.
- Todo el código probado y aprobado se fusiona a `main` para la implementación final.

### 2. **`release`**
- En esta rama se preparan las versiones de producción.
- Se fusiona `development` a `release` para realizar pruebas finales antes de fusionar con `main`.

### 3. **`development`**
- Esta es la rama de desarrollo donde se realizan la mayoría de los cambios.
- Las nuevas características se desarrollan y se prueban en esta rama antes de ser fusionadas con `release`.

### 4. **`features`**
- Las nuevas características (por ejemplo, la integración de Seaborn para las gráficas) se desarrollan en ramas dedicadas de características.
- Una vez que una característica está lista, se fusiona a `development`.

## Descripción de la Base de Datos

### Estructura de la Base de Datos

La base de datos contiene información sobre partidos de **voleibol de playa**, con detalles sobre los jugadores, los puntajes, y las estadísticas de cada partido. A continuación se muestra una descripción de los campos clave:

| Campo                       | Descripción                                                                                       |
|-----------------------------|---------------------------------------------------------------------------------------------------|
| `circuit`                   | El circuito del torneo (por ejemplo, AVP)                                                        |
| `tournament`                | Nombre del torneo                                                                                 |
| `country`                   | País donde se jugó el torneo                                                                       |
| `year`                      | Año en el que se jugó el torneo                                                                    |
| `date`                      | Fecha del partido                                                                                 |
| `gender`                    | Género de los jugadores (M o F)                                                                    |
| `match_num`                 | Número del partido en el torneo                                                                   |
| `w_player1`                 | Nombre del jugador 1 (equipo ganador)                                                              |
| `w_player2`                 | Nombre del jugador 2 (equipo ganador)                                                              |
| `l_player1`                 | Nombre del jugador 1 (equipo perdedor)                                                             |
| `l_player2`                 | Nombre del jugador 2 (equipo perdedor)                                                             |
| `score`                     | El puntaje del partido (formato "XX-XX, YY-YY")                                                   |
| `duration`                  | Duración del partido en formato `HH:MM:SS`                                                        |
| `bracket`                   | Fase del torneo (por ejemplo, "Winner's Bracket")                                                  |
| `round`                     | Ronda del torneo (por ejemplo, "Round 1")                                                         |
| **Estadísticas de Jugadores** |                                                                                                 |
| `w_p1_tot_attacks`          | Total de ataques de jugador 1 (equipo ganador)                                                   |
| `w_p1_tot_kills`            | Total de "kills" de jugador 1 (equipo ganador)                                                   |
| `w_p1_tot_errors`           | Total de errores de jugador 1 (equipo ganador)                                                   |
| ...                         | (Existen estadísticas similares para todos los jugadores en el equipo ganador y perdedor)         |

La tabla se llama `volleyball_matches` y tiene la información de cada partido jugado en el torneo.



# Instrucciones de Instalación y Ejecución

### 1. Clona el repositorio:
Primero, clona el repositorio en tu máquina local:

```bash
git clone <URL_REPOSITORIO>
```

### 2. Crea y activa un entorno virtual:

Es recomendable usar un entorno virtual para evitar conflictos con otras dependencias del sistema:

## En Linux/macOS:

```bash
python -m venv env
source env/bin/activate
```

## En Windows:

```bash
python -m venv env
env\Scripts\activate
```

### 3. Instala las dependencias:

Una vez que el entorno virtual esté activado, instala todas las dependencias necesarias para el proyecto:

```bash
pip install -r requirements.txt
```

### 4. Crea el archivo .env:

Crea un archivo llamado .env en el directorio raíz del proyecto y agrega la configuración de la base de datos y cualquier otra variable de entorno necesaria. Un ejemplo básico:

```bash
DATABASE_URI =  mysql:EL_LINK_DE_LA_BASE_DE_DATOS
INPUT_PATH = Data/BeachVolleyball.csv  # Ruta al archivo CSV
```

### 5. Ejecuta el flujo ETL:

Finalmente, ejecuta el script principal del flujo ETL:

```bash
python Main.py
```

## Docker

Se proporcionan archivos para contenerizar el proyecto: `Dockerfile` y `docker-compose.yml`.

Instrucciones rápidas:

1) Construir la imagen con Docker:

```bash
docker build -t etl-deportes:latest .
```

2) Ejecutar el contenedor directamente:

```bash
docker run --rm -v "$(pwd)/.env:/app/.env:ro" -v "$(pwd)/Data:/app/Data:ro" etl-deportes:latest
```

Nota: el montaje de `Data` es opcional; si no lo montas, asegúrate de que el archivo `Data/BeachVolleyball.csv` esté presente en el contexto copiado.

3) Usar docker-compose (más sencillo para desarrollo):

```bash
docker-compose up --build
```

4) Detener el servicio:

```bash
docker-compose down
```

Recomendaciones:
- Si tu proyecto requiere escribir en `Data` o en la base de datos, cambia el volumen montado en `docker-compose.yml` a lectura/escritura (quita `:ro`).
- Si usas `mysqlclient` y falla la instalación, revisa que tengas las dependencias de sistema adecuadas; el `Dockerfile` ya instala las más comunes en Debian/Ubuntu.


# Funcionalidad del Proyecto
1. Extracción de Datos (Extract)

Los datos se extraen desde un archivo CSV (BeachVolleyball.csv) o desde la base de datos MySQL. El archivo de entrada y la configuración de la base de datos se gestionan a través del archivo .env.

2. Transformación de Datos (Transform)

Los datos extraídos se transforman:

Se convierten las fechas a formato datetime.

Se dividen los puntajes en columnas separadas (score_set1, score_set2).

Se limpian las columnas y se convierten los tipos de datos según sea necesario.

3. Carga de Datos (Load)

Los datos transformados se cargan en la base de datos MySQL, en la tabla volleyball_matches. Si la tabla no existe, se crea automáticamente.

4. Generación de Gráficas

Se generan tres tipos de gráficas:

Distribución de Puntajes: Muestra la distribución de los puntajes de los partidos.

Tendencia de Puntajes a lo Largo del Tiempo: Muestra cómo los puntajes han cambiado a lo largo de los partidos.

Comparación de Puntajes por País: Compara los puntajes de los partidos según los países de los jugadores.

# Contribuciones

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

Haz un fork del repositorio.

Crea una rama para tu funcionalidad (git checkout -b feature/nueva-funcionalidad).

Realiza tus cambios y haz un commit (git commit -am 'Agregada nueva funcionalidad').

Empuja a tu rama (git push origin feature/nueva-funcionalidad).
