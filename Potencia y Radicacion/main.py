"""
Escenas para potencia y radicación.
Agrega aquí clases de Manim similares a las de `src/expresiones_algebraicas.py`.
"""

from manim import *


class EjemploPotencia(Scene):
    def construct(self):
        titulo = Text("Potencia y Radicación", font_size=48, color=BLUE)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        self.wait(2)
        aviso = Text("Agrega tus escenas aquí", font_size=36, color=YELLOW)
        self.play(FadeIn(aviso))
        self.wait(2)
