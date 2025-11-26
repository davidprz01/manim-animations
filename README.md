# Animaciones con Manim (expresiones y curso profesional)

Coleccion en espanol para practicar Manim Community: escenas CLI sobre expresiones algebraicas/potenciacion y el set completo de notebooks del curso "Manim Professional".

## Estructura
- `src/expresiones_algebraicas.py`: 4 escenas listas para CLI (Escena1_ExpresionesAlgebraicas, Escena2_SumaPolinomios, Escena3_RestaPolinomios, Escena4_ProductoPolinomios).
- `Expresiones Algebraicas/manin.ipynb`: notebook editable con el mismo contenido de expresiones.
- `potyr/potencia.py`: escenas introductorias sobre potenciacion (IntroPotencia, EjemplosPotenciacion).
- `Potencia y Radicacion/main.py`: boceto de escena de potencia/radicacion.
- `Curso Manim Professional/`: 15 notebooks tematicos (00_Installation a 14_Basic_Updaters) basados en la guia de DevTaoism.
- `media/`: salidas de render que git ignora.

## Requisitos
- Python 3.10+ recomendado.
- Manim Community 0.18.x (`pip install -r requirements.txt`).
- Distribucion LaTeX si usas `MathTex`/`Tex`.
- Jupyter o VS Code si abriras los notebooks.

## Instalacion rapida
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
En Linux/macOS activa con `source .venv/bin/activate`.

## Renderizar escenas (CLI)
```bash
# Expresiones algebraicas
manim -pqm src/expresiones_algebraicas.py Escena1_ExpresionesAlgebraicas
manim -pqm src/expresiones_algebraicas.py Escena2_SumaPolinomios
manim -pqm src/expresiones_algebraicas.py Escena3_RestaPolinomios
manim -pqm src/expresiones_algebraicas.py Escena4_ProductoPolinomios

# Potencias
manim -pqm potyr/potencia.py IntroPotencia
manim -pqm potyr/potencia.py EjemplosPotenciacion

# Borrador potencia/radicacion
manim -pqm "Potencia y Radicacion/main.py" EjemploPotencia
```
Cambia `-pqm` por `-pqh` o `-p` para mas calidad. Videos en `media/videos/...`.

## Trabajar con los notebooks
- Expresiones: abre `Expresiones Algebraicas/manin.ipynb`, ejecuta celdas en orden y ajusta parametros.
- Curso profesional: abre cualquier notebook dentro de `Curso Manim Professional/` y sigue el mismo flujo.
- Las celdas que renderizan escenas guardan videos bajo `media/videos/...` (segun config de Manim).
- Para llevar una escena a CLI, copia la clase a un `.py` y ejecuta `manim -pqm archivo.py NombreDeEscena`.

## Curso Manim Professional (indice)
1. 00_Installation - Instalacion de ManimCE
2. 01_Basic_Elements - Elementos basicos
3. 02_Basic_Mobjects - Atributos basicos de Mobjects
4. 03_Camera_Options - Configuracion de camara y renderizado
5. 04_Layers - Capas y z_index
6. 05_Rate_Functions - Funciones de velocidad
7. 06_Assets - Importar recursos (imagenes, SVG, sonidos)
8. 07_Groups - Groups y VGroups
9. 08_Text_and_Tex - Texto y formulas matematicas
10. 09_Transformations - Transformaciones entre objetos
11. 10_Methods_as_Animations - Metodos como animaciones
12. 11_Manim_Utils - Utilidades de Manim
13. 12_2D_Graphs - Graficos 2D
14. 13_3D_Graphs - Graficos 3D
15. 14_Basic_Updaters - Updaters basicos

## Tips rapidos
- Tras instalar LaTeX, reinicia la terminal antes de renderizar.
- `manim -h` muestra opciones de resolucion, fps y rutas.
- Guarda assets (imagenes, SVG, audio) en una subcarpeta y referencialos con rutas relativas.
- Si algo falla en el render, prueba con `-pql` para compilar mas rapido mientras iteras.
