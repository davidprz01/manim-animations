from manim import *

class ReglasCadenaYImplicita(Scene):
    def construct(self):
        self.introduccion()
        self.wait(2)
        self.clear()

        self.regla_cadena_explicacion()
        self.wait(2)
        self.clear()

        self.regla_cadena_ejemplo1()
        self.wait(2)
        self.clear()

        self.regla_cadena_ejemplo2()
        self.wait(2)
        self.clear()

        self.regla_cadena_ejemplo3()
        self.wait(2)
        self.clear()

        self.diferenciacion_implicita_intro()
        self.wait(2)
        self.clear()

        self.diferenciacion_implicita_ejemplo()
        self.wait(2)
        self.clear()

        self.diferenciacion_implicita_ejemplo2()
        self.wait(2)
        self.clear()

        self.diferenciacion_implicita_ejemplo3()
        self.wait(2)
        self.clear()

        self.resumen_comparativo()
        self.wait(2)
        self.clear()

        self.conclusion()
        self.wait(3)
    
    def introduccion(self):
        """Escena de introducción"""
        titulo = Text("Derivadas Avanzadas", font_size=60, color=BLUE)
        subtitulo = Text("Regla de la Cadena y Diferenciación Implícita", 
                        font_size=36, color=WHITE)
        subtitulo.next_to(titulo, DOWN, buff=0.5)
        
        self.play(Write(titulo), run_time=1.5)
        self.play(FadeIn(subtitulo, shift=UP), run_time=1)
        self.wait()
    
    def regla_cadena_explicacion(self):
        """Explicación teórica de la regla de la cadena"""
        titulo = Text("Regla de la Cadena", font_size=48, color=BLUE)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        
        # Definición
        definicion = MathTex(
            r"\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)",
            font_size=50
        )
        definicion.set_color_by_tex("f", YELLOW)
        definicion.set_color_by_tex("g", GREEN)
        self.play(Write(definicion), run_time=2)
        self.wait()
        
        # Explicación visual
        self.play(definicion.animate.scale(0.8).to_edge(UP, buff=1.5))
        
        explicacion = VGroup(
            Text("Función compuesta:", font_size=32, color=GRAY),
            MathTex(r"y = f(g(x))", font_size=40, color=WHITE),
            Text("Derivamos de afuera hacia adentro", font_size=28, color=GRAY)
        ).arrange(DOWN, buff=0.3)
        explicacion.shift(DOWN * 0.5)
        
        self.play(FadeIn(explicacion, shift=UP), run_time=1.5)
        self.wait()
        
        # Diagrama de flujo
        boxes = VGroup(
            self.crear_caja("x", WHITE),
            self.crear_caja("g(x)", GREEN),
            self.crear_caja("f(g(x))", YELLOW)
        ).arrange(RIGHT, buff=1.2).shift(DOWN * 2)
        
        arrows = VGroup(
            Arrow(boxes[0].get_right(), boxes[1].get_left(), color=GREEN),
            Arrow(boxes[1].get_right(), boxes[2].get_left(), color=YELLOW)
        )
        
        self.play(
            FadeOut(explicacion),
            LaggedStart(*[FadeIn(box) for box in boxes], lag_ratio=0.3)
        )
        self.play(Create(arrows), run_time=1.5)
        self.wait()
    
    def regla_cadena_ejemplo1(self):
        """Ejemplo 1: Derivada de función compuesta simple"""
        titulo = Text("Ejemplo 1: Regla de la Cadena", font_size=40, color=BLUE)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        
        # Función original
        func = MathTex(r"y = (3x^2 + 5)^4", font_size=48, color=WHITE)
        self.play(Write(func))
        self.wait()
        self.play(func.animate.shift(UP * 2))
        
        # Identificar funciones
        paso1 = VGroup(
            Text("Paso 1: Identificar funciones", font_size=28, color=GRAY),
            MathTex(r"f(u) = u^4", font_size=36, color=YELLOW),
            MathTex(r"g(x) = 3x^2 + 5", font_size=36, color=GREEN)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        paso1.next_to(func, DOWN, buff=0.8)
        
        self.play(FadeIn(paso1, shift=UP), run_time=1.5)
        self.wait()
        
        # Derivar función externa
        self.play(FadeOut(paso1))
        paso2 = VGroup(
            Text("Paso 2: Derivar función externa", font_size=28, color=GRAY),
            MathTex(r"f'(u) = 4u^3", font_size=36, color=YELLOW)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        paso2.next_to(func, DOWN, buff=0.8)
        
        self.play(FadeIn(paso2, shift=UP), run_time=1.5)
        self.wait()
        
        # Derivar función interna
        self.play(FadeOut(paso2))
        paso3 = VGroup(
            Text("Paso 3: Derivar función interna", font_size=28, color=GRAY),
            MathTex(r"g'(x) = 6x", font_size=36, color=GREEN)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        paso3.next_to(func, DOWN, buff=0.8)
        
        self.play(FadeIn(paso3, shift=UP), run_time=1.5)
        self.wait()
        
        # Aplicar regla
        self.play(FadeOut(paso3))
        paso4 = VGroup(
            Text("Paso 4: Multiplicar", font_size=28, color=GRAY),
            MathTex(r"\frac{dy}{dx} = 4(3x^2 + 5)^3 \cdot 6x", font_size=40, color=ORANGE)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        paso4.next_to(func, DOWN, buff=0.8)
        
        self.play(FadeIn(paso4, shift=UP), run_time=1.5)
        self.wait()
        
        # Simplificar
        resultado = MathTex(
            r"\frac{dy}{dx} = 24x(3x^2 + 5)^3",
            font_size=48,
            color=RED
        )
        resultado.shift(DOWN * 1.5)
        
        caja = SurroundingRectangle(resultado, color=RED, buff=0.2)
        self.play(
            FadeOut(paso4),
            Write(resultado),
            run_time=2
        )
        self.play(Create(caja))
        self.wait()
    
    def regla_cadena_ejemplo2(self):
        """Ejemplo 2: Función compuesta más compleja"""
        titulo = Text("Ejemplo 2: Composición Multiple", font_size=40, color=BLUE)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        
        # Función original
        func = MathTex(r"y = \sin(e^{2x})", font_size=48, color=WHITE)
        self.play(Write(func))
        self.wait()
        self.play(func.animate.shift(UP * 2))
        
        # Identificar capas
        paso1 = VGroup(
            Text("Identificar capas (de afuera hacia adentro):", font_size=28, color=GRAY),
            MathTex(r"f(u) = \sin(u)", font_size=36, color=YELLOW),
            MathTex(r"g(x) = e^{2x}", font_size=36, color=GREEN)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        paso1.next_to(func, DOWN, buff=0.8)
        
        self.play(FadeIn(paso1, shift=UP), run_time=1.5)
        self.wait()
        
        # Derivadas
        self.play(FadeOut(paso1))
        paso2 = VGroup(
            Text("Calcular derivadas:", font_size=28, color=GRAY),
            MathTex(r"f'(u) = \cos(u)", font_size=36, color=YELLOW),
            MathTex(r"g'(x) = 2e^{2x}", font_size=36, color=GREEN)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        paso2.next_to(func, DOWN, buff=0.8)
        
        self.play(FadeIn(paso2, shift=UP), run_time=1.5)
        self.wait()
        
        # Aplicar regla
        self.play(FadeOut(paso2))
        paso3 = VGroup(
            Text("Aplicar regla de la cadena:", font_size=28, color=GRAY),
            MathTex(r"\frac{dy}{dx} = \cos(e^{2x}) \cdot 2e^{2x}", font_size=40, color=ORANGE)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        paso3.next_to(func, DOWN, buff=0.8)
        
        self.play(FadeIn(paso3, shift=UP), run_time=1.5)
        self.wait()
        
        # Resultado final
        resultado = MathTex(
            r"\frac{dy}{dx} = 2e^{2x}\cos(e^{2x})",
            font_size=48,
            color=RED
        )
        resultado.shift(DOWN * 1.5)
        
        caja = SurroundingRectangle(resultado, color=RED, buff=0.2)
        self.play(
            FadeOut(paso3),
            Write(resultado),
            run_time=2
        )
        self.play(Create(caja))
        self.wait()
    
    def diferenciacion_implicita_intro(self):
        """Introducción a diferenciación implícita"""
        titulo = Text("Diferenciación Implícita", font_size=48, color=BLUE)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        
        # Comparación
        explicita = VGroup(
            Text("Función Explícita:", font_size=32, color=GRAY),
            MathTex(r"y = x^2 + 3x", font_size=40, color=GREEN)
        ).arrange(DOWN, buff=0.2)
        explicita.shift(UP * 1)
        
        implicita = VGroup(
            Text("Función Implícita:", font_size=32, color=GRAY),
            MathTex(r"x^2 + y^2 = 25", font_size=40, color=YELLOW)
        ).arrange(DOWN, buff=0.2)
        implicita.shift(DOWN * 1.5)
        
        self.play(FadeIn(explicita, shift=UP), run_time=1.5)
        self.wait()
        self.play(FadeIn(implicita, shift=UP), run_time=1.5)
        self.wait()
        
        # Nota importante
        nota = Text(
            "En funciones implícitas, derivamos ambos lados respecto a x",
            font_size=28,
            color=ORANGE
        )
        nota.to_edge(DOWN, buff=0.5)
        
        self.play(Write(nota), run_time=2)
        self.wait()
    
    def diferenciacion_implicita_ejemplo(self):
        """Ejemplo completo de diferenciación implícita"""
        titulo = Text("Ejemplo: Círculo", font_size=40, color=BLUE)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        
        # Ecuación original
        ecuacion = MathTex(r"x^2 + y^2 = 25", font_size=48, color=WHITE)
        objetivo = Text("Encontrar dy/dx", font_size=32, color=GRAY)
        objetivo.next_to(ecuacion, DOWN, buff=0.3)
        
        self.play(Write(ecuacion))
        self.play(FadeIn(objetivo, shift=UP))
        self.wait()
        self.play(
            ecuacion.animate.shift(UP * 2),
            FadeOut(objetivo)
        )
        
        # Paso 1: Derivar ambos lados
        paso1_titulo = Text("Paso 1: Derivar ambos lados respecto a x", 
                           font_size=28, color=GRAY)
        paso1_titulo.next_to(ecuacion, DOWN, buff=0.5)
        
        derivacion = MathTex(
            r"\frac{d}{dx}(x^2 + y^2) = \frac{d}{dx}(25)",
            font_size=40,
            color=WHITE
        )
        derivacion.next_to(paso1_titulo, DOWN, buff=0.3)
        
        self.play(Write(paso1_titulo))
        self.play(Write(derivacion), run_time=1.5)
        self.wait()
        
        # Paso 2: Aplicar regla de la cadena a y²
        self.play(FadeOut(paso1_titulo), FadeOut(derivacion))
        
        paso2_titulo = Text("Paso 2: Recordar que y depende de x", 
                           font_size=28, color=GRAY)
        paso2_titulo.next_to(ecuacion, DOWN, buff=0.5)
        
        explicacion = VGroup(
            MathTex(r"\frac{d}{dx}(x^2) = 2x", font_size=36, color=GREEN),
            MathTex(r"\frac{d}{dx}(y^2) = 2y \cdot \frac{dy}{dx}", 
                   font_size=36, color=YELLOW),
            MathTex(r"\frac{d}{dx}(25) = 0", font_size=36, color=BLUE)
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        explicacion.next_to(paso2_titulo, DOWN, buff=0.4)
        
        self.play(Write(paso2_titulo))
        self.play(LaggedStart(*[Write(eq) for eq in explicacion], lag_ratio=0.5))
        self.wait()
        
        # Paso 3: Sustituir
        self.play(FadeOut(paso2_titulo), FadeOut(explicacion))
        
        paso3_titulo = Text("Paso 3: Sustituir en la ecuación", 
                           font_size=28, color=GRAY)
        paso3_titulo.next_to(ecuacion, DOWN, buff=0.5)
        
        sustitucion = MathTex(
            r"2x + 2y\frac{dy}{dx} = 0",
            font_size=44,
            color=ORANGE
        )
        sustitucion.next_to(paso3_titulo, DOWN, buff=0.4)
        
        self.play(Write(paso3_titulo))
        self.play(Write(sustitucion), run_time=1.5)
        self.wait()
        
        # Paso 4: Despejar dy/dx
        self.play(FadeOut(paso3_titulo))
        
        paso4_titulo = Text("Paso 4: Despejar dy/dx", 
                           font_size=28, color=GRAY)
        paso4_titulo.next_to(ecuacion, DOWN, buff=0.5)
        
        self.play(
            sustitucion.animate.next_to(paso4_titulo, DOWN, buff=0.4),
            Write(paso4_titulo)
        )
        
        despeje1 = MathTex(r"2y\frac{dy}{dx} = -2x", font_size=44, color=ORANGE)
        despeje1.next_to(sustitucion, DOWN, buff=0.4)
        
        self.play(TransformFromCopy(sustitucion, despeje1), run_time=1.5)
        self.wait()
        
        # Resultado final
        resultado = MathTex(
            r"\frac{dy}{dx} = -\frac{x}{y}",
            font_size=52,
            color=RED
        )
        resultado.shift(DOWN * 1.8)
        
        caja = SurroundingRectangle(resultado, color=RED, buff=0.3)
        
        self.play(
            FadeOut(paso4_titulo),
            FadeOut(sustitucion),
            FadeOut(despeje1)
        )
        self.play(Write(resultado), run_time=2)
        self.play(Create(caja))
        self.wait()
    
    def conclusion(self):
        """Escena de conclusión"""
        titulo = Text("Resumen", font_size=52, color=BLUE)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        
        puntos = VGroup(
            Text(" Regla de la Cadena:", font_size=32, color=YELLOW),
            Text("   Derivar de afuera hacia adentro", font_size=26, color=GRAY),
            Text(" Diferenciación Implícita:", font_size=32, color=GREEN),
            Text("   Derivar ambos lados y despejar dy/dx", font_size=26, color=GRAY),
            Text(" Ambas técnicas usan la regla de la cadena", 
                font_size=28, color=ORANGE)
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        puntos.shift(DOWN * 0.5)
        
        self.play(LaggedStart(*[FadeIn(p, shift=UP) for p in puntos], lag_ratio=0.3))
        self.wait()
        
        mensaje = Text("¡Practica estos métodos!", font_size=40, color=RED)
        mensaje.to_edge(DOWN, buff=1)
        self.play(Write(mensaje), run_time=1.5)
    
    def crear_caja(self, texto, color):
        """Crea una caja con texto para diagramas"""
        caja = Rectangle(width=2, height=1, color=color, fill_opacity=0.2)
        text = MathTex(texto, color=color)
        return VGroup(caja, text)

    def regla_cadena_ejemplo3(self):
        titulo = Text("Ejemplo 3: Logaritmo de potencia", font_size=40, color=BLUE)
        titulo.to_edge(UP)
        self.play(Write(titulo))

        func = MathTex(r"y = \ln\big((2x+1)^5\big)", font_size=48, color=WHITE)
        self.play(Write(func))
        self.wait()
        self.play(func.animate.shift(UP * 2))

        paso1 = VGroup(
            Text("Identificar funciones:", font_size=28, color=GRAY),
            MathTex(r"f(u) = \ln(u)", font_size=36, color=YELLOW),
            MathTex(r"g(x) = (2x+1)^5", font_size=36, color=GREEN)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        paso1.next_to(func, DOWN, buff=0.8)
        self.play(FadeIn(paso1, shift=UP), run_time=1.5)
        self.wait()

        self.play(FadeOut(paso1))
        paso2 = VGroup(
            Text("Derivadas:", font_size=28, color=GRAY),
            MathTex(r"f'(u) = \frac{1}{u}", font_size=36, color=YELLOW),
            MathTex(r"g'(x) = 5(2x+1)^4\cdot 2", font_size=36, color=GREEN)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        paso2.next_to(func, DOWN, buff=0.8)
        self.play(FadeIn(paso2, shift=UP), run_time=1.5)
        self.wait()

        self.play(FadeOut(paso2))
        paso3 = VGroup(
            Text("Aplicar regla de la cadena:", font_size=28, color=GRAY),
            MathTex(r"\frac{dy}{dx} = \frac{1}{(2x+1)^5}\cdot 10(2x+1)^4", font_size=40, color=ORANGE)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        paso3.next_to(func, DOWN, buff=0.8)
        self.play(FadeIn(paso3, shift=UP), run_time=1.5)
        self.wait()

        resultado = MathTex(r"\frac{dy}{dx} = \frac{10}{2x+1}", font_size=48, color=RED)
        resultado.shift(DOWN * 1.5)
        caja = SurroundingRectangle(resultado, color=RED, buff=0.2)
        self.play(FadeOut(paso3), Write(resultado), run_time=2)
        self.play(Create(caja))
        self.wait()

    def diferenciacion_implicita_ejemplo2(self):
        titulo = Text("Ejemplo: Hipérbola", font_size=40, color=BLUE)
        titulo.to_edge(UP)
        self.play(Write(titulo))

        ecuacion = MathTex(r"xy = 1", font_size=48, color=WHITE)
        objetivo = Text("Encontrar dy/dx", font_size=32, color=GRAY)
        objetivo.next_to(ecuacion, DOWN, buff=0.3)
        self.play(Write(ecuacion))
        self.play(FadeIn(objetivo, shift=UP))
        self.wait()
        self.play(ecuacion.animate.shift(UP * 2), FadeOut(objetivo))

        paso1_titulo = Text("Paso 1: Derivar ambos lados", font_size=28, color=GRAY)
        paso1_titulo.next_to(ecuacion, DOWN, buff=0.5)
        derivacion = MathTex(r"\frac{d}{dx}(xy) = \frac{d}{dx}(1)", font_size=40, color=WHITE)
        derivacion.next_to(paso1_titulo, DOWN, buff=0.3)
        self.play(Write(paso1_titulo))
        self.play(Write(derivacion), run_time=1.5)
        self.wait()

        self.play(FadeOut(paso1_titulo), FadeOut(derivacion))
        paso2_titulo = Text("Paso 2: Regla del producto", font_size=28, color=GRAY)
        paso2_titulo.next_to(ecuacion, DOWN, buff=0.5)
        explicacion = VGroup(
            MathTex(r"\frac{d}{dx}(xy) = x\frac{dy}{dx} + y", font_size=36, color=YELLOW),
            MathTex(r"\frac{d}{dx}(1) = 0", font_size=36, color=BLUE)
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        explicacion.next_to(paso2_titulo, DOWN, buff=0.4)
        self.play(Write(paso2_titulo))
        self.play(LaggedStart(*[Write(eq) for eq in explicacion], lag_ratio=0.5))
        self.wait()

        self.play(FadeOut(paso2_titulo), FadeOut(explicacion))
        paso3_titulo = Text("Paso 3: Despejar dy/dx", font_size=28, color=GRAY)
        paso3_titulo.next_to(ecuacion, DOWN, buff=0.5)
        sustitucion = MathTex(r"x\frac{dy}{dx} + y = 0", font_size=44, color=ORANGE)
        sustitucion.next_to(paso3_titulo, DOWN, buff=0.4)
        self.play(Write(paso3_titulo))
        self.play(Write(sustitucion), run_time=1.5)
        self.wait()

        despeje = MathTex(r"\frac{dy}{dx} = -\frac{y}{x}", font_size=52, color=RED)
        despeje.shift(DOWN * 1.8)
        caja = SurroundingRectangle(despeje, color=RED, buff=0.3)
        self.play(FadeOut(paso3_titulo), FadeOut(sustitucion))
        self.play(Write(despeje), run_time=2)
        self.play(Create(caja))
        self.wait()

    def diferenciacion_implicita_ejemplo3(self):
        titulo = Text("Ejemplo: Curva cúbica", font_size=40, color=BLUE)
        titulo.to_edge(UP)
        self.play(Write(titulo))

        ecuacion = MathTex(r"x^3 + y^3 = 1", font_size=48, color=WHITE)
        objetivo = Text("Encontrar dy/dx", font_size=32, color=GRAY)
        objetivo.next_to(ecuacion, DOWN, buff=0.3)
        self.play(Write(ecuacion))
        self.play(FadeIn(objetivo, shift=UP))
        self.wait()
        self.play(ecuacion.animate.shift(UP * 2), FadeOut(objetivo))

        paso1_titulo = Text("Paso 1: Derivar ambos lados", font_size=28, color=GRAY)
        paso1_titulo.next_to(ecuacion, DOWN, buff=0.5)
        derivacion = MathTex(r"\frac{d}{dx}(x^3 + y^3) = \frac{d}{dx}(1)", font_size=40, color=WHITE)
        derivacion.next_to(paso1_titulo, DOWN, buff=0.3)
        self.play(Write(paso1_titulo))
        self.play(Write(derivacion), run_time=1.5)
        self.wait()

        self.play(FadeOut(paso1_titulo), FadeOut(derivacion))
        paso2_titulo = Text("Paso 2: Aplicar derivadas", font_size=28, color=GRAY)
        paso2_titulo.next_to(ecuacion, DOWN, buff=0.5)
        explicacion = VGroup(
            MathTex(r"\frac{d}{dx}(x^3) = 3x^2", font_size=36, color=GREEN),
            MathTex(r"\frac{d}{dx}(y^3) = 3y^2\cdot\frac{dy}{dx}", font_size=36, color=YELLOW),
            MathTex(r"\frac{d}{dx}(1) = 0", font_size=36, color=BLUE)
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        explicacion.next_to(paso2_titulo, DOWN, buff=0.4)
        self.play(Write(paso2_titulo))
        self.play(LaggedStart(*[Write(eq) for eq in explicacion], lag_ratio=0.5))
        self.wait()

        self.play(FadeOut(paso2_titulo), FadeOut(explicacion))
        paso3_titulo = Text("Paso 3: Despejar dy/dx", font_size=28, color=GRAY)
        paso3_titulo.next_to(ecuacion, DOWN, buff=0.5)
        sustitucion = MathTex(r"3x^2 + 3y^2\frac{dy}{dx} = 0", font_size=44, color=ORANGE)
        sustitucion.next_to(paso3_titulo, DOWN, buff=0.4)
        self.play(Write(paso3_titulo))
        self.play(Write(sustitucion), run_time=1.5)
        self.wait()

        despeje = MathTex(r"\frac{dy}{dx} = -\frac{x^2}{y^2}", font_size=52, color=RED)
        despeje.shift(DOWN * 1.8)
        caja = SurroundingRectangle(despeje, color=RED, buff=0.3)
        self.play(FadeOut(paso3_titulo), FadeOut(sustitucion))
        self.play(Write(despeje), run_time=2)
        self.play(Create(caja))
        self.wait()

    def resumen_comparativo(self):
        titulo = Text("Resumen Comparativo", font_size=48, color=BLUE)
        titulo.to_edge(UP)
        self.play(Write(titulo))

        caja1 = Rectangle(width=5.5, height=3.5, color=YELLOW, fill_opacity=0.1)
        caja2 = Rectangle(width=5.5, height=3.5, color=GREEN, fill_opacity=0.1)
        grupo = VGroup(caja1, caja2).arrange(RIGHT, buff=1.0).shift(DOWN * 0.5)
        self.play(FadeIn(grupo))

        titulo1 = Text("Regla de la Cadena", font_size=28, color=YELLOW)
        titulo2 = Text("Implícita", font_size=28, color=GREEN)
        titulo1.move_to(caja1.get_top() + DOWN * 0.4)
        titulo2.move_to(caja2.get_top() + DOWN * 0.4)
        self.play(FadeIn(titulo1), FadeIn(titulo2))

        lista1 = VGroup(
            Text("f(g(x))", font_size=24, color=WHITE),
            Text("Derivar afuera y adentro", font_size=24, color=GRAY),
            Text("Multiplicar por g'(x)", font_size=24, color=GRAY)
        ).arrange(DOWN, buff=0.25)
        lista2 = VGroup(
            Text("Ecuación con x y y", font_size=24, color=WHITE),
            Text("Derivar ambos lados", font_size=24, color=GRAY),
            Text("Despejar dy/dx", font_size=24, color=GRAY)
        ).arrange(DOWN, buff=0.25)
        lista1.move_to(caja1.get_center())
        lista2.move_to(caja2.get_center())
        self.play(LaggedStart(*[FadeIn(i, shift=UP) for i in lista1], lag_ratio=0.2))
        self.play(LaggedStart(*[FadeIn(i, shift=UP) for i in lista2], lag_ratio=0.2))
        self.wait()
