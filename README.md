# UNAL-projects

Un repositorio para todos los proyectos básicos necesarios en la UNAL cuya complejidad no amerite realizar un repositorio completo.

A repository for all basic or one-repository UNAL projects whose complexity is not big enough for a large repo.

## Directorio / Directory

- [Programación de Computadores](#programacion-de-computadores)
  1. [Python Equipos — Análisis de equipos de fútbol](#1-python-equipos--analisis-de-equipos-de-futbol)
  2. [Python Pandas — Análisis de películas](#2-python-pandas--analisis-de-peliculas)

---

## Ejercicios presentes / Exercises

### Programación de Computadores

#### 1. Python Equipos — Análisis de equipos de fútbol

| Archivo | Descripción |
|---------|-------------|
| [Python_equipos/registro_equipos.py](Python_equipos/registro_equipos.py) | Script principal: lee, analiza y genera tabla de posiciones |
| [Python_equipos/equiposChampions.csv](Python_equipos/equiposChampions.csv) | Datos de entrada: equipos con partidos ganados, empatados, perdidos y goles |

**Funcionalidad:**
- Calcula puntos por equipo (victoria = 3, empate = 1, derrota = 0)
- Determina el líder de la tabla (desempate por diferencia de goles)
- Imprime la tabla de posiciones ordenada en consola
- Genera archivos de salida: `equiposSalida.csv` y `equiposSalida.txt`

**Ejecución:** Ejecutar con Python directamente desde terminal (no tiene manejo absoluto de directorio; requiere ejecutarse desde la raíz del proyecto).

```bash
python Python_equipos/registro_equipos.py
```
---

#### 2. Python Pandas — Análisis de películas

| Archivo | Descripción |
|---------|-------------|
| [Python_pandas/main.py](Python_pandas/main.py) | Script principal: lee, transforma, analiza y exporta datos de películas |
| [Python_pandas/peliculas.csv](Python_pandas/peliculas.csv) | Datos de entrada: películas con título, género, duración, calificación y año |

**Funcionalidad:**
- Clasifica películas por apreciación (Excelente, Buena, Regular, Mala, Pésima) según calificación
- Marca si una película es clásica (anterior a 1995)
- Calcula promedio de calificación y cantidad de películas por género
- Genera archivos de salida: `peliculas_transformadas.csv` y `analisis_peliculas.xlsx`

**Ejecución:** Usa `os.path.dirname(os.path.abspath(__file__))` para manejo absoluto de directorio — puede ejecutarse desde cualquier ubicación. El archivo [peliculas.csv](Python_pandas/peliculas.csv) debe estar en el mismo directorio que el script.

```bash
python Python_pandas/main.py
```
**Requerimientos:** Se necesita tener la libreria de python pandas para que el funcionamiento sea el esperado.

---


---

> **Enlace al repositorio:** [github.com/TheAbsdag/UNAL-projects](https://github.com/TheAbsdag/UNAL-projects)
