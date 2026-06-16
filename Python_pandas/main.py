import csv
import os
import pandas as pd

# Directorio donde se encuentra este script absoluto, se asume que el archivo peliculas estará en el mismo directorio
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


# 1. Funciones de clasificación y análisis
def clasificarApreciacion(calificacion):
    """
    Clasifica una película según su calificación.
    Excelente: > 8.5
    Buena:     7.0 - 8.5
    Regular:   5.0 - 7.0
    Mala:      3.0 - 5.0
    Pésima:    0.0 - 3.0
    """
    calif = float(calificacion)
    if calif > 8.5:
        return "Excelente"
    elif calif >= 7.0:
        return "Buena"
    elif calif >= 5.0:
        return "Regular"
    elif calif >= 3.0:
        return "Mala"
    else:
        return "Pésima"


def esClasica(anio):
    """Retorna True si la película fue estrenada antes del año 1995."""
    return int(anio) < 1995


def promedioCalificacionPorGenero(df):
    """
    Calcula el promedio de calificación por género.
    Retorna un DataFrame con columnas: Género, Promedio Calificación.
    """
    promedio = (
        df.groupby("genero")["calificacion"]
        .mean()
        .round(2)
        .reset_index()
    )
    promedio.columns = ["Género", "Promedio Calificación"]
    return promedio


def cantidadPeliculasPorGenero(df):
    """
    Calcula la cantidad de películas por género.
    Retorna un DataFrame con columnas: Género, Cantidad de Películas.
    """
    cantidad = (
        df.groupby("genero")["titulo"]
        .count()
        .reset_index()
    )
    cantidad.columns = ["Género", "Cantidad de Películas"]
    return cantidad


# 2. Lectura del archivo CSV de entrada
peliculas = []  # Lista de diccionarios, cada uno representa una película

with open(os.path.join(SCRIPT_DIR, "peliculas.csv"), "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        pelicula = {
            "titulo": fila["titulo"],
            "genero": fila["genero"],
            "duracion": int(fila["duracion"]),
            "calificacion": float(fila["calificacion"]),
            "anio": int(fila["anio"]),
        }
        peliculas.append(pelicula)

# Convertir la lista de diccionarios a DataFrame de pandas
df = pd.DataFrame(peliculas)

print("=" * 60)
print("         DATOS ORIGINALES - PELÍCULAS (primeras 5 filas)")
print("=" * 60)
print(df.head())

# 3. Transformación de datos: columnas "clásica" y "Apreciación"
# Crear un nuevo DataFrame con las columnas solicitadas
df_nuevo = df[["titulo", "genero", "calificacion"]].copy()

# Agregar columna "clásica"
df_nuevo["clásica"] = df["anio"].apply(esClasica)

# Agregar columna "Apreciación"
df_nuevo["Apreciación"] = df["calificacion"].apply(clasificarApreciacion)

print("\n" + "=" * 60)
print("      DATAFRAME TRANSFORMADO (primeras 10 filas)")
print("=" * 60)
print(df_nuevo.head(10))

# 4. Escritura del archivo CSV de salida (películas transformadas)
with open(os.path.join(SCRIPT_DIR, "peliculas_transformadas.csv"), "w", newline="", encoding="utf-8") as archivo:
    campos = ["titulo", "genero", "calificacion", "clásica", "Apreciación"]
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()

    for _, fila in df_nuevo.iterrows():
        escritor.writerow({
            "titulo": fila["titulo"],
            "genero": fila["genero"],
            "calificacion": fila["calificacion"],
            "clásica": "Sí" if fila["clásica"] else "No",
            "Apreciación": fila["Apreciación"],
        })

# 5. Análisis de datos
promedio = promedioCalificacionPorGenero(df)
cantidad = cantidadPeliculasPorGenero(df)

# Combinar ambos análisis en un solo DataFrame
analisis = promedio.merge(cantidad, on="Género")

print("\n" + "=" * 60)
print("              ANÁLISIS POR GÉNERO")
print("=" * 60)
print(analisis.to_string(index=False))

# 6. Escritura del archivo Excel (.xlsx) con el análisis
analisis.to_excel(os.path.join(SCRIPT_DIR, "analisis_peliculas.xlsx"), index=False)

# 7. Resumen de archivos generados
print("\n" + "=" * 60)
print("Archivos generados exitosamente:")
print("  - Python_pandas/peliculas_transformadas.csv")
print("  - Python_pandas/analisis_peliculas.xlsx")
print("=" * 60)
