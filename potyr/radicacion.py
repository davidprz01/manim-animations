from manim import *

class IntroduccionRadicacion(Scene):
    # Introducción a la Radicación - Conceptos básicos
    
    def construct(self):
        # TÍTULO
        titulo = Text("Radicación", font_size=40, color=BLUE, weight=BOLD)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        self.wait(1)
        
        # DEFINICIÓN
        definicion = Text(
            "La radicación es la operación inversa de la potenciación",
            font_size=28
        ).next_to(titulo, DOWN, buff=0.5)
        self.play(Write(definicion))
        self.wait(2)
        
        self.play(definicion.animate.scale(0.85).to_edge(UP).shift(DOWN * 0.8))
        self.wait(0.5)
        
        # RADICAL GENERAL
        radical_general = MathTex(
            r"\sqrt[b]{c^{a}}",
            font_size=90
        ).shift(UP * 1)
        self.play(Write(radical_general))
        self.wait(2)
        
        # COMPONENTES - Índice
        flecha_indice = Arrow(
            start=radical_general.get_left() + LEFT * 0.9 + UP * 0.3,
            end=radical_general.get_left() + LEFT * 0.1 + UP * 0.1,
            color=RED,
            buff=0.1
        )
        etiqueta_indice = MathTex(
            r"b = \text{Índice}",
            color=RED,
            font_size=32
        ).next_to(flecha_indice, LEFT).shift(LEFT * 0.3 + UP * 0.1)
        
        self.play(Create(flecha_indice), Write(etiqueta_indice))
        self.wait(2)
        
        nota_indice = Text(
            "Si b=2, se omite",
            font_size=22,
            color=RED
        ).next_to(etiqueta_indice, DOWN, buff=0.3).align_to(etiqueta_indice, LEFT)
        self.play(FadeIn(nota_indice))
        self.wait(2)
        
        # COMPONENTES - Radicando
        flecha_radicando = Arrow(
            start=radical_general.get_bottom() + DOWN * 0.8,
            end=radical_general.get_bottom() + DOWN * 0.1,
            color=YELLOW,
            buff=0.1
        )
        etiqueta_radicando = MathTex(
            r"c^{a} = \text{Radicando}",
            color=YELLOW,
            font_size=32
        ).next_to(flecha_radicando, DOWN, buff=0.1)
        
        self.play(Create(flecha_radicando), Write(etiqueta_radicando))
        self.wait(2)
        
        # LIMPIAR
        self.play(
            FadeOut(flecha_indice), FadeOut(etiqueta_indice), FadeOut(nota_indice),
            FadeOut(flecha_radicando), FadeOut(etiqueta_radicando)
        )
        self.wait(0.5)
        
        # CONVERSIÓN
        titulo_conversion = Text(
            "Conversión: Radicales ↔ Exponentes",
            font_size=30,
            color=GREEN
        ).next_to(definicion, DOWN, buff=0.5)
        self.play(Write(titulo_conversion))
        self.wait(1)

        self.play(radical_general.animate.scale(0.8).shift(LEFT * 3 + DOWN * 0.5))
        self.wait(0.5)

        texto_radical = Text("Expresión en Radicales", font_size=24, color=BLUE).next_to(radical_general, DOWN, buff=0.5)
        self.play(Write(texto_radical))
        self.wait(1)

# PRIMERO: Señalar b (índice) → Denominador
        flecha_b = Arrow(
            start=radical_general.get_left() + LEFT * 0.3 + UP * 0.6,
            end=radical_general.get_left() + UP * 0.4,
            color=RED,
            buff=0.05,
            stroke_width=4
        )
        label_b_denom = Text("b = Denominador", font_size=24, color=RED).next_to(flecha_b, LEFT, buff=0.2)

        self.play(Create(flecha_b), Write(label_b_denom))
        self.wait(2)

# SEGUNDO: Señalar a (exponente) → Numerador
        flecha_a = Arrow(
            start=radical_general.get_right() + RIGHT * 1.2 + UP * 0.2,
            end=radical_general.get_right() + UP * 0.1,
            color=YELLOW,
            buff=0.05,
            stroke_width=4
        )
        label_a_num = Text("a = Numerador", font_size=24, color=YELLOW).next_to(flecha_a, RIGHT, buff=0.2).shift(RIGHT * 0.3)

        self.play(Create(flecha_a), Write(label_a_num))
        self.wait(2)

        # TERCERO: Eliminar las flechas explicativas
        self.play(
            FadeOut(flecha_b), FadeOut(label_b_denom),
            FadeOut(flecha_a), FadeOut(label_a_num)
        )
        self.wait(0.5)

        # CUARTO: Flecha verde de conversión
        flecha_conversion = Arrow(
            start=radical_general.get_right() + RIGHT * 0.3,
            end=radical_general.get_right() + RIGHT * 2.5,
            color=GREEN,
            buff=0.1,
            stroke_width=6
        )
        self.play(Create(flecha_conversion))
        self.wait(0.5)

        # QUINTO: Transform a exponente
        exponente_equivalente = MathTex(
            r"c^{\frac{a}{b}}",
            font_size=80
        ).next_to(flecha_conversion, RIGHT, buff=0.3)

        self.play(TransformFromCopy(radical_general, exponente_equivalente))
        self.wait(2)

        texto_exponente = Text("Expresión en Exponentes", font_size=24, color=BLUE).next_to(exponente_equivalente, DOWN, buff=0.5).shift(RIGHT * 0.2)
        self.play(Write(texto_exponente))
        self.wait(2)

# (Eliminar las líneas anteriores de label_b y label_a que tenías)
        
        # LIMPIAR PARA EJEMPLOS
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob != titulo])
        self.wait(0.5)
        
        # EJEMPLO 1: √16
        ejemplo_titulo = Text("Ejemplo 1:", font_size=30, color=GREEN).to_edge(LEFT).shift(UP * 2.5)
        self.play(Write(ejemplo_titulo))
        self.wait(0.5)
        
        radical_ej1 = MathTex(r"\sqrt{16}", font_size=70).next_to(ejemplo_titulo, DOWN, buff=0.5).shift(RIGHT * 1.5)
        self.play(Write(radical_ej1))
        self.wait(1)
        
        nota_ej1 = Text("Índice b=2 (omitido)", font_size=22, color=RED).next_to(radical_ej1, RIGHT, buff=0.3)
        self.play(FadeIn(nota_ej1))
        self.wait(1.5)
        self.play(FadeOut(nota_ej1))
        self.wait(0.5)
        
        igual_ej1 = MathTex(r"=", font_size=60).next_to(radical_ej1, RIGHT, buff=0.3)
        self.play(Write(igual_ej1))
        self.wait(0.3)
        
        exponente_ej1 = MathTex(r"16^{\frac{1}{2}}", font_size=60).next_to(igual_ej1, RIGHT, buff=0.3)
        self.play(TransformFromCopy(radical_ej1, exponente_ej1))
        self.wait(1.5)
        
        igual_resultado_ej1 = MathTex(r"=", font_size=60).next_to(exponente_ej1, RIGHT, buff=0.3)
        resultado_ej1 = MathTex(r"4", font_size=60, color=GREEN).next_to(igual_resultado_ej1, RIGHT, buff=0.3)
        
        self.play(Write(igual_resultado_ej1), Write(resultado_ej1))
        self.wait(1)
        
        verificacion_ej1 = MathTex(r"4^{2} = 16", font_size=35, color=BLUE).next_to(resultado_ej1, DOWN, buff=0.5)
        self.play(FadeIn(verificacion_ej1))
        self.wait(2)
        
        # EJEMPLO 2: ³√27
        self.play(
            FadeOut(radical_ej1), FadeOut(igual_ej1), FadeOut(exponente_ej1),
            FadeOut(igual_resultado_ej1), FadeOut(resultado_ej1), FadeOut(verificacion_ej1)
        )
        self.wait(0.5)
        
        ejemplo2_titulo = Text("Ejemplo 2:", font_size=30, color=GREEN).next_to(ejemplo_titulo, DOWN, buff=1)
        self.play(Write(ejemplo2_titulo))
        self.wait(0.5)
        
        radical_ej2 = MathTex(r"\sqrt[3]{27}", font_size=70).next_to(ejemplo2_titulo, DOWN, buff=0.5).shift(RIGHT * 1.5)
        self.play(Write(radical_ej2))
        self.wait(1)
        
        flecha_indice_ej2 = Arrow(
            start=radical_ej2.get_left() + LEFT * 0.3 + UP * 0.5,
            end=radical_ej2.get_left() + UP * 0.3,
            color=RED,
            buff=0.05,
            stroke_width=3
        )
        label_indice_ej2 = Text("índice b=3", font_size=20, color=RED).next_to(flecha_indice_ej2, LEFT, buff=0.1)
        
        self.play(Create(flecha_indice_ej2), Write(label_indice_ej2))
        self.wait(1)
        self.play(FadeOut(flecha_indice_ej2), FadeOut(label_indice_ej2))
        self.wait(0.5)
        
        igual_ej2 = MathTex(r"=", font_size=60).next_to(radical_ej2, RIGHT, buff=0.3)
        self.play(Write(igual_ej2))
        self.wait(0.3)
        
        exponente_ej2 = MathTex(r"27^{\frac{1}{3}}", font_size=60).next_to(igual_ej2, RIGHT, buff=0.3)
        self.play(TransformFromCopy(radical_ej2, exponente_ej2))
        self.wait(1.5)
        
        igual_resultado_ej2 = MathTex(r"=", font_size=60).next_to(exponente_ej2, RIGHT, buff=0.3)
        resultado_ej2 = MathTex(r"3", font_size=60, color=GREEN).next_to(igual_resultado_ej2, RIGHT, buff=0.3)
        
        self.play(Write(igual_resultado_ej2), Write(resultado_ej2))
        self.wait(1)
        
        verificacion_ej2 = MathTex(r"3^{3} = 27", font_size=35, color=BLUE).next_to(resultado_ej2, DOWN, buff=0.5)
        self.play(FadeIn(verificacion_ej2))
        self.wait(3)