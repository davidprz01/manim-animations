# Animaciones con Manim (expresiones, calculo y curso profesional)

Coleccion en espanol para practicar Manim Community: escenas CLI sobre expresiones algebraicas, potencia/radicacion y calculo (derivadas/limites), mas el set completo de notebooks del curso "Manim Professional".

## Estructura
- `src/expresiones_algebraicas.py`: 4 escenas listas para CLI (Escena1_ExpresionesAlgebraicas, Escena2_SumaPolinomios, Escena3_RestaPolinomios, Escena4_ProductoPolinomios).
- `Expresiones Algebraicas/manin.ipynb`: notebook editable con el mismo contenido de expresiones.
- `potyr/potencia.py`: introduccion a potencia/radicacion (componentes del radical y conversion a exponentes) en la escena `Escena3_IntroduccionRadicacion`.
- `potyr/radicacion.py`: variante guiada de radicacion con conversion radical ↔ exponente (`IntroduccionRadicacion`).
- `Grupos/Grupo_1.py`: Regla de la cadena y diferenciacion implicita (`ReglasCadenaYImplicita`).
- `Grupos/Grupo_2.py`: Metodos para resolver limites (sustitucion, factorizacion, racionalizacion) (`LimitesAnimation`).
- `Grupos/Grupo_3.py`: Reglas de derivacion: suma, producto y cociente (`ReglasDerivadasScene`).
- `Curso Manim Professional/`: 15 notebooks tematicos (00_Installation a 14_Basic_Updaters) basados en la guia de DevTaoism.
- `Videos/`: renders de ejemplo (no requeridos para ejecutar).
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

# Potencias y radicacion
manim -pqm potyr/potencia.py Escena3_IntroduccionRadicacion
manim -pqm potyr/radicacion.py IntroduccionRadicacion

# Calculo (derivadas/limites)
manim -pqm Grupos/Grupo_1.py ReglasCadenaYImplicita
manim -pqm Grupos/Grupo_2.py LimitesAnimation
manim -pqm Grupos/Grupo_3.py ReglasDerivadasScene
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
