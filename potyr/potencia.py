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

# Propiedades de las Potencias - Parte 1: Producto y Cociente
class PropiedadesPotenciasP1(Scene):
      
    def construct(self):
        # ==================== TÍTULO ====================
        titulo = Text("Propiedades de las Potencias", font_size=40, color=BLUE, weight=BOLD)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        self.wait(1)
        
        # ==================== PROPIEDAD 1: PRODUCTO ====================
        propiedad1_titulo = Text(
            "1. Producto de potencias de la misma base",
            font_size=28,
            color=GREEN
        ).next_to(titulo, DOWN, buff=0.8)
        self.play(Write(propiedad1_titulo))
        self.wait(1)
        
        # Regla general
        regla1 = MathTex(
            r"a^{n}",      # [0]
            r"\cdot",      # [1]
            r"a^{m}",      # [2]
            r"=",          # [3]
            r"a^{n+m}",    # [4]
            font_size=60
        ).next_to(propiedad1_titulo, DOWN, buff=0.5)
        
        # Colorear partes
        regla1[0].set_color(YELLOW)
        regla1[2].set_color(YELLOW)
        regla1[4].set_color(RED)
        
        self.play(Write(regla1[0:3]))  # a^n · a^m
        self.wait(1)
        self.play(Write(regla1[3]))    # =
        self.wait(0.5)
        self.play(TransformFromCopy(VGroup(regla1[0], regla1[2]), regla1[4]))  # a^(n+m)
        self.wait(2)
        
        # Explicación
        explicacion1 = Text(
            "Se pone la misma base y se SUMAN los exponentes",
            font_size=24,
            color=BLUE
        ).next_to(regla1, DOWN, buff=0.5)
        explicacion1[len("Se pone la misma base y se "):len("SUMAN los exponentes")].set_color(RED)
        self.play(FadeIn(explicacion1))
        self.wait(2)
        
        # Ejemplo: 3² · 3⁵
        ejemplo1 = MathTex(
            r"3^{2} \cdot 3^{5}",      # [0]
            r"=",          # [1]
            r"3^{2+5}",    # [2]
            r"=",          # [3]
            r"3^{7}",      # [4]
            font_size=50
        ).next_to(explicacion1, DOWN, buff=0.5)
        
        self.play(Write(ejemplo1[0:2]))
        self.wait(1)
        self.play(TransformFromCopy(ejemplo1[0],ejemplo1[2]))
        self.wait(0.5)
        self.play(Write(ejemplo1[3]))
        self.wait(0.5)
        self.play(TransformFromCopy(ejemplo1[2], ejemplo1[4]))
        self.wait(1)
        

        # paso_intermedio = MathTex(
        #     r"3^{2+5}",
        #     font_size=45,
        #     color=YELLOW
        # ).move_to(ejemplo1[2].get_center())

        # Recuadro
        caja1 = SurroundingRectangle(ejemplo1[4], color=GOLD, buff=0.2)
        self.play(Create(caja1))
        self.wait(2)
        
        # Limpiar
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob != titulo])
        self.wait(0.5)
        
        # ==================== PROPIEDAD 2: COCIENTE ====================
        propiedad2_titulo = Text(
            "2. Cociente de potencias de la misma base",
            font_size=28,
            color=GREEN
        ).next_to(titulo, DOWN, buff=0.8)
        self.play(Write(propiedad2_titulo))
        self.wait(1)
        
        # Regla general
        regla2 = MathTex(
            r"\frac{a^{n}}{a^{m}}",   # [0]
            r"=",                      # [1]
            r"a^{n-m}",                # [2]
            font_size=60
        ).next_to(propiedad2_titulo, DOWN, buff=0.5)
        
        regla2[0].set_color(YELLOW)
        regla2[2].set_color(RED)
        
        self.play(Write(regla2[0]))
        self.wait(1)
        self.play(Write(regla2[1]))
        self.wait(0.5)
        self.play(TransformFromCopy(regla2[0], regla2[2]))
        self.wait(2)
        
        # Explicación
        explicacion2 = Text(
            "Se pone la misma base y se RESTAN los exponentes",
            font_size=24,
            color=BLUE
        ).next_to(regla2, DOWN, buff=0.5)
        explicacion2[len("Se pone la misma base y se "):len("RESTAN lod exponentes")].set_color(RED)
        self.play(FadeIn(explicacion2))
        self.wait(2)
        
        # Ejemplo: 3⁵ / 3²
        ejemplo2 = MathTex(
            r"\frac{3^{5}}{3^{2}}",   # [0]
            r"=",                      # [1]
            r"3^{5-2}",                # [2]
            r"=",                      # [3]
            r"3^{3}",                  # [4]
            font_size=50
        ).next_to(explicacion2, DOWN, buff=0.5)
        
        self.play(Write(ejemplo2[0]))
        self.wait(1)
        self.play(Write(ejemplo2[1]))
        self.wait(0.5)
        self.play(TransformFromCopy(ejemplo2[0], ejemplo2[2]))
        self.wait(1)
        self.play(Write(ejemplo2[3]), Write(ejemplo2[4]))
        self.wait(2)
        
        caja2 = SurroundingRectangle(ejemplo2[4], color=GOLD, buff=0.2)
        self.play(Create(caja2))
        self.wait(2)


class PropiedadesPotenciasP2(Scene):
    # Propiedades de las Potencias - Parte 2: Potencia de potencia
    
    def construct(self):
        titulo = Text("Propiedades de las Potencias", font_size=40, color=BLUE, weight=BOLD)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        self.wait(1)
        
        # ==================== PROPIEDAD 3: POTENCIA DE UNA POTENCIA ====================
        propiedad3_titulo = Text(
            "3. Potencia de una potencia",
            font_size=28,
            color=GREEN
        ).next_to(titulo, DOWN, buff=0.8)
        self.play(Write(propiedad3_titulo))
        self.wait(1)
        
        # Regla general
        regla3 = MathTex(
            r"(",          # [0]
            r"a^{n}",      # [1]
            r")^{m}",      # [2]
            r"=",          # [3]
            r"a^{n \cdot m}",  # [4]
            font_size=60
        ).next_to(propiedad3_titulo, DOWN, buff=0.5)
        
        regla3[1].set_color(YELLOW)
        regla3[4].set_color(RED)
        
        self.play(Write(regla3[0:3]))  # (a^n)^m
        self.wait(1)
        self.play(Write(regla3[3]))
        self.wait(0.5)
        self.play(TransformFromCopy(VGroup(regla3[1], regla3[2]), regla3[4]))
        self.wait(2)
        
        # Explicación
        explicacion3 = Text(
            "Se pone la misma base y se MULTIPLICAN los exponentes",
            font_size=24,
            color=BLUE
        ).next_to(regla3, DOWN, buff=0.5)
        self.play(FadeIn(explicacion3))
        self.wait(2)
        
        # Ejemplo: (3²)³
        ejemplo3 = MathTex(
            r"( 3^{2})^{3}",      # [0]
            r"=",          # [1]
            r"3^{2 \cdot 3}",  # [2]
            r"=",          # [3]
            r"3^{6}",      # [4]
            font_size=50
        ).next_to(explicacion3, DOWN, buff=0.5)
        
        self.play(Write(ejemplo3[0]))
        self.wait(1)
        self.play(Write(ejemplo3[1]))
        self.wait(0.5)
        
        # Transformar exponentes
        self.play(TransformFromCopy(ejemplo3[0], ejemplo3[2]))  
        self.wait(0.5)
        self.play(Write(ejemplo3[3]))  # =
        self.play(TransformFromCopy(ejemplo3[2], ejemplo3[4]))  
        self.wait(1) 
        
        caja3 = SurroundingRectangle(ejemplo3[4], color=GOLD, buff=0.2)
        self.play(Create(caja3))
        self.wait(2)
        
        # Limpiar
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob != titulo])
        self.wait(0.5)
        
        # ==================== PROPIEDAD 4: EXPONENTE CERO ====================
        propiedad4_titulo = Text(
            "4. Potencia con exponente cero",
            font_size=28,
            color=GREEN
        ).next_to(titulo, DOWN, buff=0.8)
        self.play(Write(propiedad4_titulo))
        self.wait(1)
        
        # Regla general
        regla4 = MathTex(
            r"a^{0}",      # [0]
            r"=",          # [1]
            r"1",          # [2]
            font_size=70
        ).next_to(propiedad4_titulo, DOWN, buff=0.5)
        
        regla4[0].set_color(YELLOW)
        regla4[2].set_color(RED)
        
        self.play(Write(regla4[0]))
        self.wait(1)
        self.play(Write(regla4[1]))
        self.wait(0.5)
        self.play(Write(regla4[2]))
        self.wait(2)
        
        # Explicación
        explicacion4 = Text(
            "Todo número elevado a cero es igual a 1",
            font_size=24,
            color=BLUE
        ).next_to(regla4, DOWN, buff=0.5)
        self.play(FadeIn(explicacion4))
        self.wait(2)
        
        # Ejemplos múltiples
        ejemplos4 = VGroup(
            MathTex(r"5^{0} = 1", font_size=45),
            MathTex(r"(-2)^{0} = 1", font_size=45),
            MathTex(r"100^{0} = 1", font_size=45)
        ).arrange(RIGHT, buff=1).next_to(explicacion4, DOWN, buff=0.7)
        
        for ej in ejemplos4:
            self.play(Write(ej))
            self.wait(1)
        
        self.wait(3)


class PropiedadesPotenciasP3(Scene):
    # Propiedades de las Potencias - Parte 3: Exponente negativo y producto con mismo exponente
    
    def construct(self):
        titulo = Text("Propiedades de las Potencias", font_size=40, color=BLUE, weight=BOLD)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        self.wait(1)
        
        # ==================== PROPIEDAD 5: EXPONENTE NEGATIVO ====================
        propiedad5_titulo = Text(
            "5. Potencia con exponente negativo",
            font_size=28,
            color=GREEN
        ).next_to(titulo, DOWN, buff=0.8)
        self.play(Write(propiedad5_titulo))
        self.wait(1)
        
        # Regla general
        regla5 = MathTex(
            r"a^{-n}",         # [0]
            r"=",              # [1]
            r"\frac{1}{a^{n}}", # [2]
            font_size=60
        ).next_to(propiedad5_titulo, DOWN, buff=0.5)
        
        regla5[0].set_color(YELLOW)
        regla5[2].set_color(RED)
        
        self.play(Write(regla5[0]))
        self.wait(1)
        self.play(Write(regla5[1]))
        self.wait(0.5)
        self.play(TransformFromCopy(regla5[0], regla5[2]))
        self.wait(2)
        
        # Explicación
        explicacion5 = Text(
            "Se invierte: 1 dividido por la potencia positiva",
            font_size=24,
            color=BLUE
        ).next_to(regla5, DOWN, buff=0.5)
        self.play(FadeIn(explicacion5))
        self.wait(2)
        
        # Ejemplo: 3⁻²
        ejemplo5 = MathTex(
            r"3^{-2}",          # [0]
            r"=",               # [1]
            r"\frac{1}{3^{2}}", # [2]
            r"=",               # [3]
            r"\frac{1}{9}",     # [4]
            font_size=50
        ).next_to(explicacion5, DOWN, buff=0.5)
        
        self.play(Write(ejemplo5[0]))
        self.wait(1)
        self.play(Write(ejemplo5[1]))
        self.wait(0.5)
        self.play(TransformFromCopy(ejemplo5[0], ejemplo5[2]))
        self.wait(1)
        self.play(Write(ejemplo5[3]), Write(ejemplo5[4]))
        self.wait(2)
        
        caja5 = SurroundingRectangle(ejemplo5[4], color=GOLD, buff=0.2)
        self.play(Create(caja5))
        self.wait(2)
        
        # Limpiar
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob != titulo])
        self.wait(0.5)
        
        # ==================== PROPIEDAD 6: PRODUCTO CON MISMO EXPONENTE ====================
        propiedad6_titulo = Text(
            "6. Producto de potencias con el mismo exponente",
            font_size=28,
            color=GREEN
        ).next_to(titulo, DOWN, buff=0.8)
        self.play(Write(propiedad6_titulo))
        self.wait(1)
        
        # Regla general
        regla6 = MathTex(
            r"a^{n}",      # [0]
            r"\cdot",      # [1]
            r"b^{n}",      # [2]
            r"=",          # [3]
            r"(",          # [4]
            r"a \cdot b",  # [5]
            r")^{n}",      # [6]
            font_size=60
        ).next_to(propiedad6_titulo, DOWN, buff=0.5)
        
        regla6[0].set_color(YELLOW)
        regla6[2].set_color(YELLOW)
        regla6[5].set_color(RED)
        
        self.play(Write(regla6[0:3]))
        self.wait(1)
        self.play(Write(regla6[3]))
        self.wait(0.5)
        self.play(
            Write(regla6[4]),
            TransformFromCopy(VGroup(regla6[0], regla6[2]), regla6[5]),
            Write(regla6[6])
        )
        self.wait(2)
        
        # Explicación
        explicacion6 = Text(
            "Se MULTIPLICAN las bases y se pone el mismo exponente",
            font_size=24,
            color=BLUE
        ).next_to(regla6, DOWN, buff=0.5)
        self.play(FadeIn(explicacion6))
        self.wait(2)
        
        # Ejemplo: 3² · 2²
        ejemplo6 = MathTex(
            r"3^{2}",           # [0]
            r"\cdot",           # [1]
            r"2^{2}",           # [2]
            r"=",               # [3]
            r"(",               # [4]
            r"3 \cdot 2",       # [5]
            r")^{2}",           # [6]
            r"=",               # [7]
            r"6^{2}",           # [8]
            r"=",               # [9]
            r"36",              # [10]
            font_size=45
        ).next_to(explicacion6, DOWN, buff=0.5)
        
        self.play(Write(ejemplo6[0:3])) #3^2 x 2^2
        self.wait(1)

        self.play(Write(ejemplo6[3])) # = 
        self.wait(0.5)

        self.play(Write(ejemplo6[4])) # (
        self.wait(1)
        self.play(Write(ejemplo6[6])) #)

        self.play(FadeIn(ejemplo6[5]))
        self.wait(1)

        self.play(Write(ejemplo6[7]), Write(ejemplo6[8]))
        self.wait(1)

        self.play(Write(ejemplo6[9]), Write(ejemplo6[10]))
        self.wait(2)
        
        caja6 = SurroundingRectangle(ejemplo6[10], color=GOLD, buff=0.2)
        self.play(Create(caja6))
        self.wait(3)


class PropiedadesPotenciasP4(Scene):
    # Propiedades de las Potencias - Parte 4: Cociente con mismo exponente
    
    def construct(self):
        titulo = Text("Propiedades de las Potencias", font_size=40, color=BLUE, weight=BOLD)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        self.wait(1)
        
        # ==================== PROPIEDAD 7: COCIENTE CON MISMO EXPONENTE ====================
        propiedad7_titulo = Text(
            "7. Cociente de potencias con el mismo exponente",
            font_size=28,
            color=GREEN
        ).next_to(titulo, DOWN, buff=0.8)
        self.play(Write(propiedad7_titulo))
        self.wait(1)
        
        # Regla general
        regla7 = MathTex(
            r"\frac{a^{n}}{b^{n}}",  # [0]
            r"=",                     # [1]
            r"\left(\frac{a}{b}\right)^{n}",  # [2]
            font_size=60
        ).next_to(propiedad7_titulo, DOWN, buff=0.5)
        
        regla7[0].set_color(YELLOW)
        regla7[2].set_color(RED)
        
        self.play(Write(regla7[0]))
        self.wait(1)
        self.play(Write(regla7[1]))
        self.wait(0.5)
        self.play(TransformFromCopy(regla7[0], regla7[2]))
        self.wait(2)
        
        # Explicación
        explicacion7 = Text(
            "Se DIVIDEN las bases y se pone el mismo exponente",
            font_size=24,
            color=BLUE
        ).next_to(regla7, DOWN, buff=0.5)
        self.play(FadeIn(explicacion7))
        self.wait(2)
        
        # Ejemplo: 6³ / 2³
        ejemplo7 = MathTex(
            r"\frac{6^{3}}{2^{3}}",      # [0]
            r"=",                         # [1]
            r"\left(\frac{6}{2}\right)^{3}",  # [2]
            r"=",                         # [3]
            r"3^{3}",                     # [4]
            r"=",                         # [5]
            r"27",                        # [6]
            font_size=50
        ).next_to(explicacion7, DOWN, buff=0.5)
        
        self.play(Write(ejemplo7[0]))
        self.wait(1)
        self.play(Write(ejemplo7[1]))
        self.wait(0.5)
        self.play(TransformFromCopy(ejemplo7[0], ejemplo7[2]))
        self.wait(1)
        self.play(Write(ejemplo7[3]), Write(ejemplo7[4]))
        self.wait(1)
        self.play(Write(ejemplo7[5]), Write(ejemplo7[6]))
        self.wait(2)
        
        caja7 = SurroundingRectangle(ejemplo7[6], color=GOLD, buff=0.2)
        self.play(Create(caja7))
        self.wait(3)