import csv

# 1. Funciones CalcularPuntos, liderTabla y CalcularDiferenciaGoles
def calcularPuntos(equipo):
    """
    Calcula los puntos de un equipo.
    Victoria -> 3 puntos
    Empate  -> 1 punto
    Derrota -> 0 puntos
    """
    return equipo["ganados"] * 3 + equipo["empatados"] * 1


def calcularDiferenciaGoles(equipo):
    """Calcula la diferencia de goles (goles_favor - goles_contra)."""
    return equipo["goles_favor"] - equipo["goles_contra"]


def liderTabla(equipos):
    """
    Retorna el equipo con la mayor puntuación.
    En caso de empate en puntos, se desempata por diferencia de goles.
    """
    if not equipos:
        return None

    # Ordenar por puntos (descendente) y diferencia de goles (descendente) como desempate
    lider = max(
        equipos,
        key=lambda e: (calcularPuntos(e), calcularDiferenciaGoles(e))
    )
    return lider

# 2. Lectura del archivo CSV de entrada y creación de la lista de equipos
equipos = []  # Lista de diccionarios, cada uno representa un equipo

with open("Python_equipos/equiposChampions.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)

    for fila in lector:
        equipo = {
            "nombre": fila["equipo"],
            "ganados": int(fila["ganados"]),
            "empatados": int(fila["empatados"]),
            "perdidos": int(fila["perdidos"]),
            "goles_favor": int(fila["goles_favor"]),
            "goles_contra": int(fila["goles_contra"]),
        }
        equipos.append(equipo)


# 3. Cálculo de puntos y diferencia de goles para cada equipo
for equipo in equipos:
    equipo["puntos"] = calcularPuntos(equipo)
    equipo["diferencia_goles"] = calcularDiferenciaGoles(equipo)


# 4. Calculo de lider
lider = liderTabla(equipos)

# 5. Impresión de la tabla de posiciones con lider destacado
print("=" * 60)
print("              TABLA DE POSICIONES - CHAMPIONS LEAGUE")
print("=" * 60)

if lider:
    print(f"\n>>> LÍDER DE LA TABLA: {lider['nombre']} <<<")
    print(f"    Puntos: {lider['puntos']}")
    print(f"    Ganados: {lider['ganados']} | Empatados: {lider['empatados']} | Perdidos: {lider['perdidos']}")
    print(f"    Goles a favor: {lider['goles_favor']} | Goles en contra: {lider['goles_contra']}")
    print(f"    Diferencia de goles: {lider['diferencia_goles']:+d}")

# 6. El adicional: Impresión de la tabla ordenada por puntos y diferencia de goles
print(f"\n{' Pos ':4s} {'Equipo':22s} {'PJ':3s} {'G':3s} {'E':3s} {'P':3s} {'GF':3s} {'GC':3s} {'DG':4s} {'Pts':4s}")
print("-" * 60)

# 7. Ordenar por puntuación (descendente) y asignar posición
equipos_ordenados = sorted(
    equipos,
    ## Funcion lambda para ordenar por puntos y luego por diferencia de goles
    ## El orden es descendente, por eso se usa reverse=True
    key=lambda e: (e["puntos"], e["diferencia_goles"]),
    reverse=True
)

# 8. Imprimir la tabla con posiciones asignadas
for i, equipo in enumerate(equipos_ordenados, start=1):
    equipo["posicion"] = i
    pj = equipo["ganados"] + equipo["empatados"] + equipo["perdidos"]
    print(
        f"{i:4d}  {equipo['nombre']:22s} "
        f"{pj:3d} {equipo['ganados']:3d} {equipo['empatados']:3d} {equipo['perdidos']:3d} "
        f"{equipo['goles_favor']:3d} {equipo['goles_contra']:3d} "
        f"{equipo['diferencia_goles']:+4d} {equipo['puntos']:4d}"
    )

# 9. Escritura del archivo CSV de salida
with open("Python_equipos/equiposSalida.csv", "w", newline="", encoding="utf-8") as archivo:
    campos = [
        "posicion", "equipo", "ganados", "empatados", "perdidos",
        "goles_favor", "goles_contra", "puntos", "diferencia_goles"
    ]
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()

    for equipo in equipos_ordenados:
        escritor.writerow({
            "posicion": equipo["posicion"],
            "equipo": equipo["nombre"],
            "ganados": equipo["ganados"],
            "empatados": equipo["empatados"],
            "perdidos": equipo["perdidos"],
            "goles_favor": equipo["goles_favor"],
            "goles_contra": equipo["goles_contra"],
            "puntos": equipo["puntos"],
            "diferencia_goles": equipo["diferencia_goles"],
        })


# 10. Pequeño extra, escritura del archivo TXT de salida con tabulación y formato legible
with open("Python_equipos/equiposSalida.txt", "w", encoding="utf-8") as archivo:
    archivo.write("=" * 70 + "\n")
    archivo.write("           TABLA DE POSICIONES - CHAMPIONS LEAGUE\n")
    archivo.write("=" * 70 + "\n\n")

    archivo.write(f"LÍDER: {lider['nombre']} - {lider['puntos']} puntos\n\n")

    encabezado = (
        f"{'Pos':4s} {'Equipo':22s} {'PJ':3s} {'G':3s} {'E':3s} {'P':3s} "
        f"{'GF':3s} {'GC':3s} {'DG':4s} {'Pts':4s}"
    )
    archivo.write(encabezado + "\n")
    archivo.write("-" * 60 + "\n")

    for equipo in equipos_ordenados:
        pj = equipo["ganados"] + equipo["empatados"] + equipo["perdidos"]
        linea = (
            f"{equipo['posicion']:4d}  {equipo['nombre']:22s} "
            f"{pj:3d} {equipo['ganados']:3d} {equipo['empatados']:3d} {equipo['perdidos']:3d} "
            f"{equipo['goles_favor']:3d} {equipo['goles_contra']:3d} "
            f"{equipo['diferencia_goles']:+4d} {equipo['puntos']:4d}"
        )
        archivo.write(linea + "\n")

    archivo.write("\n" + "=" * 70 + "\n")
    archivo.write("PJ: Partidos Jugados  |  G: Ganados  |  E: Empatados  |  P: Perdidos\n")
    archivo.write("GF: Goles a Favor     |  GC: Goles en Contra  |  DG: Diferencia de Goles\n")
    archivo.write("Pts: Puntos (Victoria=3, Empate=1, Derrota=0)\n")

print("\n" + "=" * 60)
print("Archivos generados exitosamente:")
print("  - Python_equipos/equiposSalida.csv")
print("  - Python_equipos/equiposSalida.txt")
print("=" * 60)
