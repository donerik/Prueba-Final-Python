import pandas as pd

# Función para filtrar por fechas con conversión a datetime
def filtrar_por_fechas(df, columna, fecha_inicio, fecha_fin):
    # Convertir la columna de fechas a tipo datetime si no lo está
    df[columna] = pd.to_datetime(df[columna])
    
    # Convertir las fechas de inicio y fin a datetime
    fecha_inicio = pd.to_datetime(fecha_inicio)
    fecha_fin = pd.to_datetime(fecha_fin)
    
    # Crear una máscara para filtrar los datos entre las fechas
    mask = (df[columna] >= fecha_inicio) & (df[columna] <= fecha_fin)
    return df.loc[mask]

# Función para generar reportes pivotados
def generar_reporte(df, filas, columnas, valores, funcion_agrupadora):
    pivot = pd.pivot_table(df, index=filas, columns=columnas, values=valores, aggfunc=funcion_agrupadora, fill_value=0)
    return pivot.reset_index()

# Función para guardar un DataFrame en PostgreSQL
def escribir_en_postgres(df, tabla, engine, if_exists='replace'):
    df.to_sql(tabla, engine, if_exists=if_exists, index=False)