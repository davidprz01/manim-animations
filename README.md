# Animaciones con Manim: expresiones algebraicas y potencias

Material en espanol para practicar Manim Community: escenas CLI y notebooks sobre expresiones algebraicas/potencias, mas un set de notebooks del curso "Manim Professional".

## Contenido
- `src/expresiones_algebraicas.py`: escenas listas para CLI (suma, resta y producto de polinomios).
- `Expresiones Algebraicas/manin.ipynb`: notebook editable con las mismas escenas.
- `potyr/potencia.py`: escenas introductorias sobre potenciacion.
- `Potencia y Radicacion/main.py`: boceto de escena de potencia/radicacion.
- `Curso Manim Professional/`: 15 notebooks tematicos basados en la guia de DevTaoism.
- `media/`: salidas de render; git las ignora.

## Requisitos
- Python 3.10+ recomendado.
- Manim Community 0.18.x (`pip install -r requirements.txt`).
- Distribucion LaTeX si usas `MathTex`/`Tex`.
- Jupyter o VS Code si piensas abrir los notebooks.

## Configuracion rapida
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
En Linux/macOS usa `source .venv/bin/activate`.

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
Cambia `-pqm` por `-pqh` o `-p` si quieres mas calidad. Los videos quedan en `media/videos/...`.

## Trabajar con los notebooks
- Abre `Expresiones Algebraicas/manin.ipynb` o cualquier notebook en `Curso Manim Professional/`.
- Usa Jupyter/VS Code; ejecuta las celdas en orden y modifica parametros para experimentar.
- Si quieres llevar una escena al CLI, copia la clase/escena a un `.py` y ejecutala con `manim -pqm archivo.py NombreDeEscena`.

## Notas utiles
- Tras instalar LaTeX, reinicia la terminal antes de renderizar.
- `manim -h` muestra opciones de resolucion, fps y directorios.
