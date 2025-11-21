from manim import *

class IntroPotencia(Scene):
    # Introducción a la Potenciación con ejemplo
    
    def construct(self):
        # titulo 
        titulo = Text("Potenciación", font_size=40, color=BLUE, weight=BOLD)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        self.wait(1)
        
        # def
        definicion = Text(
            "En la potenciación se distinguen tres partes importantes:",
            font_size=26
        ).next_to(titulo, DOWN, buff=0.5)
        self.play(Write(definicion))
        self.wait(2)
        
        self.play(definicion.animate.scale(0.8).to_edge(UP).shift(DOWN * 0.8))
        self.wait(0.5)
        
        # Componentes de la potencia
        potencia_general = MathTex(
            r"a^{n}",
            font_size=80
        ).shift(UP * 1.5)
        self.play(Write(potencia_general))
        self.wait(1)
        
        flecha_base = Arrow(
            start=potencia_general.get_bottom() + DOWN * 0.5 + LEFT * 0.7,
            end=potencia_general.get_left() + DOWN * 0.3 + RIGHT * 0.1,
            color=RED,
            buff=0.1
        )
        etiqueta_base = MathTex(r"a = Base", color=RED, font_size=36).next_to(flecha_base, LEFT)
        
        self.play(
            Create(flecha_base),
            Write(etiqueta_base)
        )
        self.wait(1)
        
        flecha_exp = Arrow(
            start=potencia_general.get_top() + UP * 0.2 + RIGHT * 0.7,
            end=potencia_general.get_right() + LEFT * 0.2 + UP * 0.3,
            color=YELLOW,
            buff=0.1
        )
        etiqueta_exp = MathTex(r"n = exponente", color=YELLOW, font_size=36).next_to(flecha_exp, RIGHT + LEFT * 0.9)
        
        self.play(
            Create(flecha_exp),
            Write(etiqueta_exp)
        )
        self.wait(2)
        
        # explicación del exponente
        explicacion_exp = Text(
            "n factores: significa cuántas veces\nse multiplica la base por sí misma",
            font_size=22,
            color=YELLOW
        ).next_to(etiqueta_exp, DOWN, buff=0.3).align_to(etiqueta_exp, LEFT)
        self.play(FadeIn(explicacion_exp))
        self.wait(3)
        
        # formula expandida
        self.play(
            FadeOut(flecha_base), FadeOut(etiqueta_base),
            FadeOut(flecha_exp), FadeOut(etiqueta_exp),
            FadeOut(explicacion_exp),
            potencia_general.animate.shift(LEFT * 3)
        )
        self.wait(0.5)
        
        # Mostrar expansión
        igual = MathTex(r"=", font_size=60).next_to(potencia_general, RIGHT, buff=0.3)
        
        expansion = MathTex(
            r"a \cdot a \cdot ... \cdot a = P",
            font_size=50
        ).next_to(igual, RIGHT, buff=0.3)
        
        texto_nfactores = Text("n factores", font_size=20, color=GREEN).next_to(expansion, UP, buff=0.2)
        
        self.play(Write(igual))
        self.wait(0.5)
        self.play(Write(expansion))
        self.wait(0.5)
        self.play(FadeIn(texto_nfactores))
        self.wait(2)
        
        # Resultado
        etiqueta_resultado = Text("P = Potencia (resultado)", font_size=26, color=GREEN).next_to(expansion, DOWN, buff=0.5)
        self.play(Write(etiqueta_resultado))
        self.wait(2)
        
        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob != titulo]
        )
        self.wait(0.5)
  
        ejemplo_titulo = Text("Ejemplo:", font_size=30, color=BLUE).to_edge(LEFT).shift(UP * 2)
        self.play(Write(ejemplo_titulo))
        self.wait(0.5)
        
        # Potencia 3^4
        potencia_ej = MathTex(
            r"3^{4}",
            font_size=70
        ).next_to(ejemplo_titulo, DOWN, buff=0.5).shift(RIGHT * 2)
        self.play(Write(potencia_ej))
        self.wait(1)
        

        flecha_base_ej = Arrow(
            start=potencia_ej.get_bottom() + DOWN * 0.7,
            end=potencia_ej.get_left() + DOWN * 0.4 + RIGHT * 0.1,
            color=RED,
            buff=0.1
        )
        etiqueta_base_ej = MathTex(r"3 = Base", color=RED, font_size=32).next_to(flecha_base_ej, DOWN)
        
        flecha_exp_ej = Arrow(
            start=potencia_ej.get_top() + RIGHT * 0.5 + UP * 0.7,
            end=potencia_ej.get_right() + LEFT * 0.1 + UP * 0.3,
            color=YELLOW,
            buff=0.1
        )
        etiqueta_exp_ej = MathTex(r"4 = exponente", color=YELLOW, font_size=32).next_to(flecha_exp_ej, RIGHT + UP * 0.4)
        texto_4factores = Text("4 factores: la base (3)\nse multiplica (4) veces", font_size=20, color=YELLOW).next_to(etiqueta_exp_ej, DOWN, buff=0.2).align_to(etiqueta_exp_ej, LEFT)
        
        self.play(
            Create(flecha_base_ej),
            Write(etiqueta_base_ej)
        )
        self.wait(1)
        
        self.play(
            Create(flecha_exp_ej),
            Write(etiqueta_exp_ej)
        )
        self.wait(0.5)
        self.play(FadeIn(texto_4factores))
        self.wait(2)
        
        self.play(
            FadeOut(flecha_base_ej), FadeOut(etiqueta_base_ej),
            FadeOut(flecha_exp_ej), FadeOut(etiqueta_exp_ej),
            FadeOut(texto_4factores)
        )
        self.wait(0.5)
        
        self.play(potencia_ej.animate.shift(LEFT * 2 + UP * 0.1))
        self.wait(0.5)


        igual_ej = MathTex(r"=", font_size=60).next_to(potencia_ej, RIGHT, buff=0.3)
        self.play(Write(igual_ej))
        self.wait(0.5)
        
        # Expansión: 3x3x3x3
        expansion_ej = MathTex(
            r"3",      # [0]
            r"\cdot",  # [1]
            r"3",      # [2]
            r"\cdot",  # [3]
            r"3",      # [4]
            r"\cdot",  # [5]
            r"3",      # [6]
            font_size=50
        ).next_to(igual_ej, RIGHT, buff=0.3)
        
        # Transformar base a cada factor
        self.play(
            TransformFromCopy(potencia_ej[0], expansion_ej[0])
        )
        self.wait(0.3)
        self.play(Write(expansion_ej[1]))
        self.wait(0.2)
        self.play(
            TransformFromCopy(potencia_ej[0], expansion_ej[2])
        )
        self.wait(0.3)
        self.play(Write(expansion_ej[3]))
        self.wait(0.2)
        self.play(
            TransformFromCopy(potencia_ej[0], expansion_ej[4])
        )
        self.wait(0.3)
        self.play(Write(expansion_ej[5]))
        self.wait(0.2)
        self.play(
            TransformFromCopy(potencia_ej[0], expansion_ej[6])
        )
        self.wait(1)
        
        # Marcar 4 factores
        brace = Brace(expansion_ej, DOWN, color=GREEN)
        brace_text = Text("4 factores", font_size=24, color=GREEN).next_to(brace, DOWN)
        self.play(Create(brace), Write(brace_text))
        self.wait(2)
        
        # Resultado
        self.play(FadeOut(brace), FadeOut(brace_text))
        self.wait(0.5)
        
        # Calcular resultado
        igual_resultado = MathTex(r"=", font_size=60).next_to(expansion_ej, RIGHT, buff=0.3)
        resultado = MathTex(r"81", font_size=60, color=GREEN).next_to(igual_resultado, RIGHT, buff=0.3)
        
        self.play(Write(igual_resultado))
        self.wait(0.5)
        self.play(Write(resultado))
        self.wait(2)
        
        caja_resultado = SurroundingRectangle(resultado, color=GOLD, buff=0.2)
        self.play(Create(caja_resultado))
        self.wait(2)
        
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob != titulo])
        self.wait(0.5)


class EjemplosPotenciacion(Scene):
    # Ejemplos variados de potenciación
    
    def construct(self):
        # Título
        titulo = Text("Ejemplos de Potenciación", font_size=36, color=BLUE, weight=BOLD)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        self.wait(1)
        
        # Lista de ejemplos del libro
        ejemplos = [
            (r"5^{3}", r"5 \cdot 5 \cdot 5", r"125"),
            (r"(-3)^{3}", r"(-3) \cdot (-3) \cdot (-3)", r"-27"),
            (r"8^{2}", r"8 \cdot 8", r"64"),
        ]
        
        posicion_y = 2
        
        for potencia, expansion, resultado in ejemplos:
            # Potencia
            eq_potencia = MathTex(potencia, font_size=45).shift(UP * posicion_y + LEFT * 4)
            self.play(Write(eq_potencia))
            self.wait(0.5)
            
            # Igual
            eq_igual = MathTex(r"=", font_size=45).next_to(eq_potencia, RIGHT, buff=0.3)
            self.play(Write(eq_igual))
            self.wait(0.3)
            
            # Expansión
            eq_expansion = MathTex(expansion, font_size=40).next_to(eq_igual, RIGHT, buff=0.3)
            self.play(TransformFromCopy(eq_potencia, eq_expansion))
            self.wait(0.5)
            
            # Resultado
            eq_igual2 = MathTex(r"=", font_size=45).next_to(eq_expansion, RIGHT, buff=0.3)
            eq_resultado = MathTex(resultado, font_size=45, color=GREEN).next_to(eq_igual2, RIGHT, buff=0.3)
            
            self.play(Write(eq_igual2), Write(eq_resultado))
            self.wait(1.5)
            
            posicion_y -= 1.5
        
        self.wait(3)