# Animaciones con Manim: expresiones algebraicas y potencias

Conjunto de escenas en español para manim que cubren expresiones algebraicas (suma, resta, producto) y ejemplos de potenciación.

## Requisitos
- Python 3.10+ recomendado
- [Manim Community](https://docs.manim.community/en/stable/)
- Distribución LaTeX (necesaria para `MathTex`)

## Instalación rápida
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Estructura
- `src/expresiones_algebraicas.py`: escenas listas para CLI.
- `Expresiones Algebraicas/manin.ipynb`: notebook original para edición en Jupyter.
- `potyr/potencia.py`: escenas preliminares sobre potenciación.
- `Potencia y Radicacion/main.py`: boceto de escena de potencia/radicación.
- `media/`: salidas de render (ignoradas por git).

## Escenas disponibles
Expresiones algebraicas (`src/expresiones_algebraicas.py`):
- `Escena1_ExpresionesAlgebraicas`
- `Escena2_SumaPolinomios`
- `Escena3_RestaPolinomios`
- `Escena4_ProductoPolinomios`

Potencias (`potyr/potencia.py`):
- `IntroPotencia`
- `EjemplosPotenciacion`

Borrador potencia/radicación (`Potencia y Radicacion/main.py`):
- `EjemploPotencia`

## Cómo renderizar (720p, modo rápido)
```bash
manim -pqm src/expresiones_algebraicas.py Escena1_ExpresionesAlgebraicas
manim -pqm src/expresiones_algebraicas.py Escena2_SumaPolinomios
manim -pqm src/expresiones_algebraicas.py Escena3_RestaPolinomios
manim -pqm src/expresiones_algebraicas.py Escena4_ProductoPolinomios

manim -pqm potyr/potencia.py IntroPotencia
manim -pqm potyr/potencia.py EjemplosPotenciacion

manim -pqm "Potencia y Radicacion/main.py" EjemploPotencia
```

- Cambia `-pqm` por `-pqh` o `-p` para más calidad. Los videos se guardan bajo `media/videos/...`.

## Notas útiles
- Si acabas de instalar LaTeX, reinicia la terminal antes de renderizar.
- `manim -h` muestra opciones de resolución, fps y paths.
