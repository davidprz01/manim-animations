# Animaciones de Manim para expresiones algebraicas

Este repositorio contiene cinco escenas de Manim en español sobre expresiones algebraicas:
- Escena1: conceptos básicos (monomio, binomio, trinomio, polinomio y grado)
- Escena2: suma de polinomios
- Escena3: resta de polinomios
- Escena4: producto de polinomios
- Escena5: producto de dos binomios (fórmula general y ejemplos paso a paso)

## Requisitos
- Python 3.10+ (recomendado)
- [Manim Community](https://docs.manim.community/en/stable/)
- Distribución LaTeX (para MathTex)

Instala dependencias Python con:
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

## Renderizar escenas
El código vivo está en `src/expresiones_algebraicas.py` (el notebook `Expresiones Algebraicas/manin.ipynb` sigue igual para consulta/edición en Jupyter).

Ejemplos de render a 720p, calidad media (rápido):
```bash
manim -pqm src/expresiones_algebraicas.py Escena1_ExpresionesAlgebraicas
manim -pqm src/expresiones_algebraicas.py Escena2_SumaPolinomios
manim -pqm src/expresiones_algebraicas.py Escena3_RestaPolinomios
manim -pqm src/expresiones_algebraicas.py Escena4_ProductoPolinomios
manim -pqm src/expresiones_algebraicas.py Escena5_ProductoBinomios
```

Cambia `-pqm` por `-pqh` o `-p` para más calidad. Los videos se guardan en `media/videos/...` (ignorados por git).

## Estructura
- `Expresiones Algebraicas/manin.ipynb`: notebook original usado para iterar.
- `src/expresiones_algebraicas.py`: mismas escenas listas para CLI.
- `Potencia y Radicacion/main.py`: espacio para futuras escenas de potencia y radicación.
- `media/`: salidas de render (ignoradas).

## Notas
- Si instalas LaTeX recientemente, reinicia la terminal antes de renderizar.
- Usa `manim -h` para opciones adicionales (resolución, fps, etc.).
