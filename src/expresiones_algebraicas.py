from manim import *

"""
Escenas de Manim para expresiones algebraicas.
Extraídas del notebook `Expresiones Algebraicas/manin.ipynb` para ejecución por CLI.
"""


class Escena1_ExpresionesAlgebraicas(Scene):
    def construct(self):
        # Título principal
        titulo = Text("Expresiones Algebraicas", font_size=48, color=BLUE)
        titulo.to_edge(UP)
        self.play(Write(titulo))
        self.wait(2)

        # Definición de expresión algebraica
        expresion_ejemplo = MathTex("3x^2 + 5x - 7", font_size=60, color=YELLOW)
        self.play(FadeIn(expresion_ejemplo))
        self.wait(2)

        # Señalar partes de la expresión
        terminos = VGroup(
            MathTex("3x^2", color=GREEN).scale(1.2),
            MathTex("+", color=WHITE).scale(1.2),
            MathTex("5x", color=GREEN).scale(1.2),
            MathTex("-", color=WHITE).scale(1.2),
            MathTex("7", color=GREEN).scale(1.2)
        ).arrange(RIGHT, buff=0.3)

        self.play(Transform(expresion_ejemplo, terminos))
        self.wait(2)

        # Limpiar para siguiente concepto
        self.play(FadeOut(expresion_ejemplo), FadeOut(terminos))
        self.wait(1)

        # MONOMIO
        titulo_monomio = Text("Monomio", font_size=40, color=BLUE)
        titulo_monomio.to_edge(UP, buff=1.5)
        self.play(Transform(titulo, titulo_monomio))

        monomio1 = MathTex("5x^3", font_size=55, color=YELLOW)
        monomio2 = MathTex("-2ab^2", font_size=55, color=YELLOW)
        monomio3 = MathTex("7", font_size=55, color=YELLOW)

        monomios = VGroup(monomio1, monomio2, monomio3).arrange(DOWN, buff=0.8)

        self.play(FadeIn(monomio1))
        self.wait(1.5)
        self.play(FadeIn(monomio2))
        self.wait(1.5)
        self.play(FadeIn(monomio3))
        self.wait(2)

        # Destacar: un solo término
        rect_monomio = SurroundingRectangle(monomio1, color=GREEN, buff=0.2)
        self.play(Create(rect_monomio))
        self.wait(1)
        self.play(FadeOut(rect_monomio))

        self.play(FadeOut(monomios))
        self.wait(1)

        # BINOMIO
        titulo_binomio = Text("Binomio", font_size=40, color=BLUE)
        titulo_binomio.to_edge(UP, buff=1.5)
        self.play(Transform(titulo, titulo_binomio))

        binomio1 = MathTex("2x + 5", font_size=55, color=YELLOW)
        binomio2 = MathTex("a^2 - 3b", font_size=55, color=YELLOW)

        binomios = VGroup(binomio1, binomio2).arrange(DOWN, buff=0.8)

        self.play(FadeIn(binomio1))
        self.wait(1.5)
        self.play(FadeIn(binomio2))
        self.wait(2)

        # Destacar: dos términos
        termino1 = MathTex("2x", color=GREEN, font_size=55).move_to(binomio1).shift(LEFT * 0.8)
        termino2 = MathTex("5", color=GREEN, font_size=55).move_to(binomio1).shift(RIGHT * 0.8)

        self.play(
            Indicate(termino1, color=GREEN),
            Indicate(termino2, color=GREEN)
        )
        self.wait(2)

        self.play(FadeOut(binomios))
        self.wait(1)

        # TRINOMIO
        titulo_trinomio = Text("Trinomio", font_size=40, color=BLUE)
        titulo_trinomio.to_edge(UP, buff=1.5)
        self.play(Transform(titulo, titulo_trinomio))

        trinomio1 = MathTex("x^2 + 3x - 4", font_size=55, color=YELLOW)
        trinomio2 = MathTex("2a^2 - 5ab + b^2", font_size=55, color=YELLOW)

        trinomios = VGroup(trinomio1, trinomio2).arrange(DOWN, buff=0.8)

        self.play(FadeIn(trinomio1))
        self.wait(1.5)
        self.play(FadeIn(trinomio2))
        self.wait(2)

        # Destacar: tres términos
        self.play(
            trinomio1.animate.scale(1.2).set_color(GREEN)
        )
        self.wait(1)
        self.play(trinomio1.animate.scale(1 / 1.2).set_color(YELLOW))

        self.play(FadeOut(trinomios))
        self.wait(1)

        # POLINOMIO
        titulo_polinomio = Text("Polinomio", font_size=40, color=BLUE)
        titulo_polinomio.to_edge(UP, buff=1.5)
        self.play(Transform(titulo, titulo_polinomio))

        polinomio = MathTex("4x^4 - 2x^3 + 5x^2 - x + 8", font_size=48, color=YELLOW)
        self.play(FadeIn(polinomio))
        self.wait(2)

        # Mostrar que tiene 4 o más términos
        terminos_poly = VGroup(
            MathTex("4x^4", color=GREEN),
            MathTex("-2x^3", color=GREEN),
            MathTex("+5x^2", color=GREEN),
            MathTex("-x", color=GREEN),
            MathTex("+8", color=GREEN)
        ).arrange(RIGHT, buff=0.3).scale(1.1)

        self.play(Transform(polinomio, terminos_poly))
        self.wait(2)

        self.play(FadeOut(polinomio))
        self.wait(1)

        # GRADO DEL POLINOMIO
        titulo_grado = Text("Grado del Polinomio", font_size=40, color=BLUE)
        titulo_grado.to_edge(UP, buff=1.5)
        self.play(Transform(titulo, titulo_grado))

        ejemplo_grado = MathTex("P(x) = 5x^3 + 2x^2 - 4x + 1", font_size=50, color=YELLOW)
        self.play(Write(ejemplo_grado))
        self.wait(2)

        # Señalar el exponente más alto
        exponente_mayor = MathTex("3", color=RED, font_size=70)
        exponente_mayor.next_to(ejemplo_grado, UP).shift(LEFT * 2.2)
        flecha = Arrow(exponente_mayor.get_bottom(), ejemplo_grado.get_top() + LEFT * 2.2, color=RED)

        self.play(GrowArrow(flecha), FadeIn(exponente_mayor))
        self.wait(1)

        grado_texto = Text("Grado: 3", font_size=40, color=GREEN)
        grado_texto.next_to(ejemplo_grado, DOWN, buff=0.8)
        self.play(Write(grado_texto))
        self.wait(2)

        self.play(FadeOut(exponente_mayor), FadeOut(flecha))
        self.wait(1)

        # Más ejemplos de grados
        self.play(FadeOut(ejemplo_grado), FadeOut(grado_texto))

        ejemplo2 = MathTex("Q(x) = x^5 - 3x^2 + 7", font_size=48, color=YELLOW)
        grado2 = Text("Grado: 5", font_size=36, color=GREEN)
        grupo2 = VGroup(ejemplo2, grado2).arrange(DOWN, buff=0.5)

        ejemplo3 = MathTex("R(x) = 2x^2 + 4x - 1", font_size=48, color=YELLOW)
        grado3 = Text("Grado: 2", font_size=36, color=GREEN)
        grupo3 = VGroup(ejemplo3, grado3).arrange(DOWN, buff=0.5)

        grupos = VGroup(grupo2, grupo3).arrange(DOWN, buff=1)

        self.play(FadeIn(grupo2))
        self.wait(2)
        self.play(FadeIn(grupo3))
        self.wait(2)

        # Final
        self.play(FadeOut(grupos), FadeOut(titulo))
        self.wait(1)


class Escena2_SumaPolinomios(Scene):
    def construct(self):
        # Título con animación de escritura
        titulo = Text("Suma de Polinomios", font_size=48, color=BLUE)
        titulo.to_edge(UP)
        self.play(Write(titulo, run_time=1.5))
        self.wait(2)

        # Presentar los dos polinomios con animación de aparición
        p_label = MathTex("P(x) =", font_size=44, color=WHITE)
        p_expr = MathTex("x^3 - 6x^2 + 2x + 4", font_size=44, color=YELLOW)
        polinomio_p = VGroup(p_label, p_expr).arrange(RIGHT, buff=0.3)
        polinomio_p.shift(UP * 1.5)

        q_label = MathTex("Q(x) =", font_size=44, color=WHITE)
        q_expr = MathTex("6x^2 + 2x + 4", font_size=44, color=YELLOW)
        polinomio_q = VGroup(q_label, q_expr).arrange(RIGHT, buff=0.3)
        polinomio_q.shift(UP * 0.5)

        # Animación: los polinomios entran desde los lados
        polinomio_p.shift(RIGHT * 10)
        self.play(
            polinomio_p.animate.shift(LEFT * 10),
            run_time=1
        )
        self.wait(1)

        polinomio_q.shift(LEFT * 10)
        self.play(
            polinomio_q.animate.shift(RIGHT * 10),
            run_time=1
        )
        self.wait(2)

        # Mostrar la operación de suma
        suma_symbol = MathTex("+", font_size=50, color=GREEN)
        suma_symbol.next_to(polinomio_q, LEFT, buff=0.5).shift(LEFT * 0.3)
        self.play(FadeIn(suma_symbol, scale=2))
        self.wait(1)

        # Línea divisoria animada
        linea = Line(LEFT * 3.5, RIGHT * 3.5, color=WHITE)
        linea.next_to(polinomio_q, DOWN, buff=0.3)
        self.play(Create(linea))
        self.wait(1.5)

        # Transformación: reorganizar términos por grado
        titulo_paso1 = Text("Alinear términos semejantes", font_size=32, color=ORANGE)
        titulo_paso1.to_edge(UP, buff=0.5)
        self.play(Transform(titulo, titulo_paso1))
        self.wait(1)

        # Reorganizar P(x) mostrando cada término
        p_terminos = VGroup(
            MathTex("x^3", color=RED).scale(1.1),
            MathTex("-6x^2", color=BLUE).scale(1.1),
            MathTex("+2x", color=GREEN).scale(1.1),
            MathTex("+4", color=PURPLE).scale(1.1)
        ).arrange(RIGHT, buff=0.5)
        p_terminos.move_to(polinomio_p).shift(RIGHT * 0.5)

        self.play(
            ReplacementTransform(p_expr, p_terminos),
            FadeOut(p_label)
        )
        self.wait(1)

        # Reorganizar Q(x) alineado con P(x)
        q_terminos = VGroup(
            MathTex("0", color=RED, fill_opacity=0.3).scale(1.1),
            MathTex("+6x^2", color=BLUE).scale(1.1),
            MathTex("+2x", color=GREEN).scale(1.1),
            MathTex("+4", color=PURPLE).scale(1.1)
        ).arrange(RIGHT, buff=0.5)
        q_terminos.move_to(polinomio_q).shift(RIGHT * 0.5)

        self.play(
            ReplacementTransform(q_expr, q_terminos),
            FadeOut(q_label),
            FadeOut(suma_symbol)
        )
        self.wait(2)

        # Destacar términos semejantes con animaciones de pulso
        for i in range(4):
            self.play(
                Indicate(p_terminos[i], color=WHITE, scale_factor=1.3),
                Indicate(q_terminos[i], color=WHITE, scale_factor=1.3),
                run_time=0.8
            )
            self.wait(0.5)

        self.wait(1)

        # Proceso de suma término por término
        titulo_paso2 = Text("Sumar términos", font_size=32, color=ORANGE)
        titulo_paso2.to_edge(UP, buff=0.5)
        self.play(Transform(titulo, titulo_paso2))
        self.wait(1)

        resultado_terminos = VGroup()
        resultado_y = linea.get_center()[1] - 0.8

        # Término x³ (solo hay uno)
        term1_proceso = MathTex("x^3", "+", "0", "=", "x^3", color=RED, font_size=36)
        term1_proceso.move_to([p_terminos[0].get_center()[0], resultado_y - 0.5, 0])
        self.play(Write(term1_proceso))
        self.wait(1)

        resultado1 = MathTex("x^3", color=RED).scale(1.1)
        resultado1.move_to([p_terminos[0].get_center()[0], resultado_y, 0])
        self.play(
            TransformFromCopy(term1_proceso[4], resultado1),
            FadeOut(term1_proceso)
        )
        resultado_terminos.add(resultado1)
        self.wait(1)

        # Término x² (suma real)
        term2_proceso = MathTex("-6x^2", "+", "6x^2", "=", "0", color=BLUE, font_size=36)
        term2_proceso.move_to([p_terminos[1].get_center()[0], resultado_y - 0.5, 0])
        self.play(Write(term2_proceso))
        self.wait(1.5)

        resultado2 = MathTex("0", color=BLUE, fill_opacity=0.3).scale(1.1)
        resultado2.move_to([p_terminos[1].get_center()[0], resultado_y, 0])
        self.play(
            TransformFromCopy(term2_proceso[4], resultado2),
            FadeOut(term2_proceso)
        )
        resultado_terminos.add(resultado2)
        self.wait(1)

        # Término x (suma)
        term3_proceso = MathTex("2x", "+", "2x", "=", "4x", color=GREEN, font_size=36)
        term3_proceso.move_to([p_terminos[2].get_center()[0], resultado_y - 0.5, 0])
        self.play(Write(term3_proceso))
        self.wait(1.5)

        resultado3 = MathTex("+4x", color=GREEN).scale(1.1)
        resultado3.move_to([p_terminos[2].get_center()[0], resultado_y, 0])
        self.play(
            TransformFromCopy(term3_proceso[4], resultado3),
            FadeOut(term3_proceso)
        )
        resultado_terminos.add(resultado3)
        self.wait(1)

        # Término independiente
        term4_proceso = MathTex("4", "+", "4", "=", "8", color=PURPLE, font_size=36)
        term4_proceso.move_to([p_terminos[3].get_center()[0], resultado_y - 0.5, 0])
        self.play(Write(term4_proceso))
        self.wait(1.5)

        resultado4 = MathTex("+8", color=PURPLE).scale(1.1)
        resultado4.move_to([p_terminos[3].get_center()[0], resultado_y, 0])
        self.play(
            TransformFromCopy(term4_proceso[4], resultado4),
            FadeOut(term4_proceso)
        )
        resultado_terminos.add(resultado4)
        self.wait(2)

        # Limpiar y mostrar resultado final
        self.play(
            FadeOut(p_terminos),
            FadeOut(q_terminos),
            FadeOut(linea),
            FadeOut(resultado2)  # El 0 desaparece
        )
        self.wait(1)

        # Reorganizar resultado final
        titulo_final = Text("Resultado Final", font_size=40, color=BLUE)
        titulo_final.to_edge(UP, buff=0.5)
        self.play(Transform(titulo, titulo_final))

        # Mover resultado al centro
        resultado_limpio = VGroup(resultado1, resultado3, resultado4)
        self.play(
            resultado_limpio.animate.arrange(RIGHT, buff=0.3).move_to(ORIGIN).scale(1.2)
        )
        self.wait(2)

        # Encuadrar el resultado final
        resultado_box = SurroundingRectangle(resultado_limpio, color=GOLD, buff=0.3, corner_radius=0.2)
        self.play(Create(resultado_box))
        self.wait(1)

        # Escribir la respuesta completa
        respuesta_final = MathTex("P(x) + Q(x) =", "x^3 + 4x + 8", font_size=50)
        respuesta_final[1].set_color(YELLOW)
        respuesta_final.move_to(ORIGIN)

        self.play(
            FadeOut(resultado_limpio),
            FadeOut(resultado_box),
            Write(respuesta_final)
        )
        self.wait(2)

        # Efecto final: destacar resultado con rotación
        self.play(
            respuesta_final[1].animate.scale(1.3).set_color(GOLD),
            rate_func=there_and_back,
            run_time=1.5
        )
        self.wait(1)

        # Desvanecimiento final
        self.play(
            FadeOut(respuesta_final),
            FadeOut(titulo)
        )
        self.wait(1)


class Escena3_RestaPolinomios(Scene):
    def construct(self):
        # Título con animación
        titulo = Text("Resta de Polinomios", font_size=48, color=BLUE)
        titulo.to_edge(UP)
        self.play(Write(titulo, run_time=1.5))
        self.wait(2)

        # Presentar los dos polinomios
        p_label = MathTex("P(x) =", font_size=44, color=WHITE)
        p_expr = MathTex("x^3 - 6x^2 + 2x + 4", font_size=44, color=YELLOW)
        polinomio_p = VGroup(p_label, p_expr).arrange(RIGHT, buff=0.3)
        polinomio_p.shift(UP * 1.5)

        q_label = MathTex("Q(x) =", font_size=44, color=WHITE)
        q_expr = MathTex("6x^2 + 2x + 4", font_size=44, color=YELLOW)
        polinomio_q = VGroup(q_label, q_expr).arrange(RIGHT, buff=0.3)
        polinomio_q.shift(UP * 0.5)

        # Animación: entrada desde arriba y abajo
        polinomio_p.shift(UP * 5)
        self.play(
            polinomio_p.animate.shift(DOWN * 5),
            run_time=1
        )
        self.wait(1)

        polinomio_q.shift(DOWN * 5)
        self.play(
            polinomio_q.animate.shift(UP * 5),
            run_time=1
        )
        self.wait(2)

        # Mostrar la operación de resta con efecto especial
        resta_symbol = MathTex("-", font_size=50, color=RED)
        resta_symbol.next_to(polinomio_q, LEFT, buff=0.5).shift(LEFT * 0.3)
        self.play(
            FadeIn(resta_symbol, scale=3),
            resta_symbol.animate.set_color(ORANGE)
        )
        self.wait(1)

        # Línea divisoria
        linea = Line(LEFT * 3.5, RIGHT * 3.5, color=WHITE)
        linea.next_to(polinomio_q, DOWN, buff=0.3)
        self.play(Create(linea))
        self.wait(1.5)

        # PASO 1: Cambiar signos de Q(x)
        titulo_paso1 = Text("Cambiar signos de Q(x)", font_size=32, color=ORANGE)
        titulo_paso1.to_edge(UP, buff=0.5)
        self.play(Transform(titulo, titulo_paso1))
        self.wait(1)

        # Destacar Q(x) para cambiar signos
        rect_q = SurroundingRectangle(q_expr, color=RED, buff=0.15)
        self.play(Create(rect_q))
        self.wait(1)

        # Mostrar el cambio de signos con animación
        q_expr_new = MathTex("-6x^2 - 2x - 4", font_size=44, color=ORANGE)
        q_expr_new.move_to(q_expr)

        self.play(
            TransformMatchingShapes(q_expr, q_expr_new),
            rect_q.animate.set_color(GREEN),
            run_time=1.5
        )
        self.wait(2)
        self.play(FadeOut(rect_q))

        # PASO 2: Alinear términos
        titulo_paso2 = Text("Alinear términos semejantes", font_size=32, color=ORANGE)
        titulo_paso2.to_edge(UP, buff=0.5)
        self.play(Transform(titulo, titulo_paso2))
        self.wait(1)

        # Reorganizar P(x)
        p_terminos = VGroup(
            MathTex("x^3", color=RED).scale(1.1),
            MathTex("-6x^2", color=BLUE).scale(1.1),
            MathTex("+2x", color=GREEN).scale(1.1),
            MathTex("+4", color=PURPLE).scale(1.1)
        ).arrange(RIGHT, buff=0.5)
        p_terminos.move_to(polinomio_p).shift(RIGHT * 0.5)

        self.play(
            ReplacementTransform(p_expr, p_terminos),
            FadeOut(p_label)
        )
        self.wait(1)

        # Reorganizar Q(x) con signos cambiados
        q_terminos = VGroup(
            MathTex("0", color=RED, fill_opacity=0.3).scale(1.1),
            MathTex("-6x^2", color=BLUE).scale(1.1),
            MathTex("-2x", color=GREEN).scale(1.1),
            MathTex("-4", color=PURPLE).scale(1.1)
        ).arrange(RIGHT, buff=0.5)
        q_terminos.move_to(polinomio_q).shift(RIGHT * 0.5)

        self.play(
            ReplacementTransform(q_expr, q_terminos),
            FadeOut(q_label),
            FadeOut(resta_symbol)
        )
        self.wait(2)

        # Destacar términos semejantes con efecto wave
        for i in range(4):
            self.play(
                Wiggle(p_terminos[i], scale_value=1.3, rotation_angle=0.02 * TAU),
                Wiggle(q_terminos[i], scale_value=1.3, rotation_angle=0.02 * TAU),
                run_time=0.8
            )
            self.wait(0.4)

        self.wait(1)

        # PASO 3: Sumar términos
        titulo_paso3 = Text("Sumar términos", font_size=32, color=ORANGE)
        titulo_paso3.to_edge(UP, buff=0.5)
        self.play(Transform(titulo, titulo_paso3))
        self.wait(1)

        resultado_terminos = VGroup()
        resultado_y = linea.get_center()[1] - 0.8

        # Término x³
        term1_proceso = MathTex("x^3", "+", "0", "=", "x^3", color=RED, font_size=36)
        term1_proceso.move_to([p_terminos[0].get_center()[0], resultado_y - 0.5, 0])
        self.play(Write(term1_proceso))
        self.wait(1)

        resultado1 = MathTex("x^3", color=RED).scale(1.1)
        resultado1.move_to([p_terminos[0].get_center()[0], resultado_y, 0])
        self.play(
            TransformFromCopy(term1_proceso[4], resultado1),
            FadeOut(term1_proceso)
        )
        resultado_terminos.add(resultado1)
        self.wait(1)

        # Término x² (se cancelan)
        term2_proceso = MathTex("-6x^2", "+", "(-6x^2)", "=", "-12x^2", color=BLUE, font_size=36)
        term2_proceso.move_to([p_terminos[1].get_center()[0], resultado_y - 0.5, 0])
        self.play(Write(term2_proceso))
        self.wait(1.5)

        resultado2 = MathTex("-12x^2", color=BLUE).scale(1.1)
        resultado2.move_to([p_terminos[1].get_center()[0], resultado_y, 0])
        self.play(
            TransformFromCopy(term2_proceso[4], resultado2),
            FadeOut(term2_proceso)
        )
        resultado_terminos.add(resultado2)
        self.wait(1)

        # Término x
        term3_proceso = MathTex("2x", "+", "(-2x)", "=", "0", color=GREEN, font_size=36)
        term3_proceso.move_to([p_terminos[2].get_center()[0], resultado_y - 0.5, 0])
        self.play(Write(term3_proceso))
        self.wait(1.5)

        resultado3 = MathTex("0", color=GREEN, fill_opacity=0.3).scale(1.1)
        resultado3.move_to([p_terminos[2].get_center()[0], resultado_y, 0])
        self.play(
            TransformFromCopy(term3_proceso[4], resultado3),
            FadeOut(term3_proceso)
        )
        resultado_terminos.add(resultado3)
        self.wait(1)

        # Término independiente
        term4_proceso = MathTex("4", "+", "(-4)", "=", "0", color=PURPLE, font_size=36)
        term4_proceso.move_to([p_terminos[3].get_center()[0], resultado_y - 0.5, 0])
        self.play(Write(term4_proceso))
        self.wait(1.5)

        resultado4 = MathTex("0", color=PURPLE, fill_opacity=0.3).scale(1.1)
        resultado4.move_to([p_terminos[3].get_center()[0], resultado_y, 0])
        self.play(
            TransformFromCopy(term4_proceso[4], resultado4),
            FadeOut(term4_proceso)
        )
        resultado_terminos.add(resultado4)
        self.wait(2)

        # Limpiar los ceros
        self.play(
            FadeOut(p_terminos),
            FadeOut(q_terminos),
            FadeOut(linea),
            FadeOut(resultado3),
            FadeOut(resultado4)
        )
        self.wait(1)

        # Resultado final
        titulo_final = Text("Resultado Final", font_size=40, color=BLUE)
        titulo_final.to_edge(UP, buff=0.5)
        self.play(Transform(titulo, titulo_final))

        # Mover resultado al centro
        resultado_limpio = VGroup(resultado1, resultado2)
        self.play(
            resultado_limpio.animate.arrange(RIGHT, buff=0.3).move_to(ORIGIN).scale(1.3)
        )
        self.wait(2)

        # Encuadrar con efecto pulsante
        resultado_box = SurroundingRectangle(resultado_limpio, color=GOLD, buff=0.3, corner_radius=0.2)
        self.play(Create(resultado_box))
        self.play(
            resultado_box.animate.set_color(RED),
            rate_func=there_and_back,
            run_time=1
        )
        self.wait(1)

        # Respuesta completa
        respuesta_final = MathTex("P(x) - Q(x) =", "x^3 - 12x^2", font_size=50)
        respuesta_final[1].set_color(YELLOW)
        respuesta_final.move_to(ORIGIN)

        self.play(
            FadeOut(resultado_limpio),
            FadeOut(resultado_box),
            Write(respuesta_final)
        )
        self.wait(2)

        # Efecto final: rotación completa
        self.play(
            Rotate(respuesta_final[1], angle=TAU, run_time=2),
            respuesta_final[1].animate.set_color(GOLD)
        )
        self.wait(1)

        # Desvanecimiento final
        self.play(
            FadeOut(respuesta_final),
            FadeOut(titulo)
        )
        self.wait(1)


class Escena4_ProductoPolinomios(Scene):
    def construct(self):
        # Título
        titulo = Text("Producto de Polinomios", font_size=48, color=BLUE)
        titulo.to_edge(UP)
        self.play(Write(titulo, run_time=1.5))
        self.wait(2)

        # Presentar el producto completo
        producto_completo = MathTex(
            "(x^3 - 6x^2 + 2x + 4)", "\\cdot", "(6x^2 + 2x + 4)",
            font_size=44,
            color=YELLOW
        )
        producto_completo.shift(UP * 2)

        # Entrada con escala
        self.play(GrowFromCenter(producto_completo))
        self.wait(2)

        # PASO 1: Aplicar distributiva
        titulo_paso1 = Text("Aplicar propiedad distributiva", font_size=32, color=ORANGE)
        titulo_paso1.to_edge(UP, buff=0.5)
        self.play(Transform(titulo, titulo_paso1))
        self.wait(1)

        # Reducir y mover arriba
        self.play(
            producto_completo.animate.scale(0.7).to_edge(UP, buff=1.2)
        )
        self.wait(1)

        # Mostrar las 3 multiplicaciones parciales - bien espaciadas
        producto1 = MathTex("6x^5", "-", "36x^4", "+", "12x^3", "+", "24x^2", font_size=36, color=RED)
        producto1.move_to([0, 1, 0])

        producto2 = MathTex("2x^4", "-", "12x^3", "+", "4x^2", "+", "8x", font_size=36, color=BLUE)
        producto2.next_to(producto1, DOWN, buff=0.5)

        producto3 = MathTex("4x^3", "+", "4x^2", "+", "8x", "+", "16", font_size=36, color=GREEN)
        producto3.next_to(producto2, DOWN, buff=0.5)

        # Animaciones de entrada
        self.play(Write(producto1))
        self.wait(1.5)
        self.play(Write(producto2))
        self.wait(1.5)
        self.play(Write(producto3))
        self.wait(2)

        # Línea para sumar
        linea = Line(LEFT * 5, RIGHT * 5, color=WHITE)
        linea.next_to(producto3, DOWN, buff=0.4)
        self.play(Create(linea))
        self.wait(1)

        # PASO 2: Sumar términos semejantes
        titulo_paso2 = Text("Sumar términos semejantes", font_size=32, color=ORANGE)
        titulo_paso2.to_edge(UP, buff=0.5)
        self.play(Transform(titulo, titulo_paso2))
        self.wait(1)

        # Destacar términos del mismo grado con pulsos
        # x^5
        self.play(Indicate(producto1[0], color=YELLOW, scale_factor=1.4))
        self.wait(0.5)

        # x^4
        self.play(
            Indicate(producto1[2], color=YELLOW, scale_factor=1.4),
            Indicate(producto2[0], color=YELLOW, scale_factor=1.4)
        )
        self.wait(0.5)

        # x^3
        self.play(
            Indicate(producto1[4], color=YELLOW, scale_factor=1.4),
            Indicate(producto2[2], color=YELLOW, scale_factor=1.4),
            Indicate(producto3[0], color=YELLOW, scale_factor=1.4)
        )
        self.wait(0.5)

        # x^2
        self.play(
            Indicate(producto1[6], color=YELLOW, scale_factor=1.4),
            Indicate(producto2[4], color=YELLOW, scale_factor=1.4),
            Indicate(producto3[2], color=YELLOW, scale_factor=1.4)
        )
        self.wait(0.5)

        # x
        self.play(
            Indicate(producto2[6], color=YELLOW, scale_factor=1.4),
            Indicate(producto3[4], color=YELLOW, scale_factor=1.4)
        )
        self.wait(0.5)

        # constante
        self.play(Indicate(producto3[6], color=YELLOW, scale_factor=1.4))
        self.wait(1)

        # Resultado final de la suma - bien abajo
        resultado_suma = MathTex(
            "6x^5", "-", "32x^4", "+", "4x^3", "+", "4x^2", "+", "16x", "+", "16",
            font_size=40,
            color=GOLD
        )
        resultado_suma.next_to(linea, DOWN, buff=0.6)

        self.play(Write(resultado_suma, run_time=2.5))
        self.wait(2)

        # Encuadrar resultado
        box_resultado = SurroundingRectangle(resultado_suma, color=GOLD, buff=0.3)
        self.play(Create(box_resultado))
        self.wait(1)

        # Limpiar todo
        self.play(
            FadeOut(producto_completo),
            FadeOut(producto1),
            FadeOut(producto2),
            FadeOut(producto3),
            FadeOut(linea),
            FadeOut(box_resultado)
        )
        self.wait(1)

        # RESULTADO FINAL - CENTRADO
        titulo_final = Text("Resultado Final", font_size=40, color=BLUE)
        titulo_final.to_edge(UP, buff=0.5)
        self.play(Transform(titulo, titulo_final))

        # Mover al centro y agrandar
        self.play(
            resultado_suma.animate.move_to(ORIGIN).scale(1.3)
        )
        self.wait(2)

        # Marco final brillante
        box_final = SurroundingRectangle(resultado_suma, color=GOLD, buff=0.4, corner_radius=0.2)
        self.play(Create(box_final))
        self.play(
            Flash(resultado_suma, color=GOLD, num_lines=20),
            box_final.animate.set_stroke(width=6)
        )
        self.wait(1)

        # Fórmula completa
        respuesta_completa = MathTex(
            "P(x) \\cdot Q(x) =",
            "6x^5 - 32x^4 + 4x^3 + 4x^2 + 16x + 16",
            font_size=38
        )
        respuesta_completa[1].set_color(YELLOW)
        respuesta_completa.move_to(ORIGIN)

        self.play(
            FadeOut(resultado_suma),
            FadeOut(box_final),
            Write(respuesta_completa, run_time=2)
        )
        self.wait(2)

        # Efecto final: pulso doble
        for _ in range(2):
            self.play(
                respuesta_completa[1].animate.scale(1.15).set_color(GOLD),
                rate_func=there_and_back,
                run_time=0.7
            )
            self.wait(0.2)

        self.wait(1)

        # Desvanecimiento
        self.play(
            FadeOut(respuesta_completa),
            FadeOut(titulo)
        )
        self.wait(1)


if __name__ == "__main__":
    print("Usa: manim -pqm src/expresiones_algebraicas.py Escena1_ExpresionesAlgebraicas (u otra escena)")
