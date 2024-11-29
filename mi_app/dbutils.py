import pyodbc
import pandas as pd

# Configuración de la conexión
server = 'weatherserver.database.windows.net'
database = 'weather'
username = 'admin1'
password = 'Azito21066504'
driver = '{ODBC Driver 17 for SQL Server}'

def get_forecast_data():
    try:
        # Establecer conexión
        conn = pyodbc.connect(
            f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}'
        )

        # Consultar los datos
        query = "SELECT * FROM forecast_weather"
        df = pd.read_sql(query, conn)

        # Cerrar la conexión
        conn.close()

        # Retornar los datos como un DataFrame de pandas
        return df

    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return pd.DataFrame()  # Retorna un DataFrame vacío en caso de error


