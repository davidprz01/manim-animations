# Curso Manim Professional


## Requisitos
- Python 3.10+ y Manim Community 0.18.x (instala desde la raiz: `pip install -r ..\requirements.txt`).
- Jupyter Notebook/Lab o VS Code con la extension de Jupyter.
- Distribucion LaTeX si quieres renderizar celdas con `Tex` o `MathTex`.

## Preparacion rapida
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r ..\requirements.txt
pip install jupyterlab
```
En Linux/macOS activa con `source .venv/bin/activate` y usa la ruta `../requirements.txt`.

## Como usar los notebooks
1. Abre el notebook de cada carpeta y ejecuta las celdas en orden.
2. Las celdas que renderizan escenas guardan videos bajo `../media/videos/...` segun la configuracion de Manim.
3. Ajusta parametros y duplica celdas para probar variantes sin perder los ejemplos originales.
4. Si prefieres la CLI, copia la clase/escena a un `.py` y ejecuta `manim -pqm ruta.py NombreDeEscena`.

## Estructura del curso
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

## Recursos adicionales
- Video de introduccion: https://www.youtube.com/watch?v=RN8el9uNioc&t=13s
- Documentacion oficial: https://docs.devtaoism.com/docs/html/index.html
- Comunidad Manim: https://www.manim.community/

Consejo: usa `06_Assets/` para guardar imagenes, SVG o sonidos y referenciarlos con rutas relativas en tus escenas.
