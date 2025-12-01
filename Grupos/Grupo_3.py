from manim import *


class ReglasDerivadasScene(Scene):
    def construct(self):
        # Fondo oscuro
        self.camera.background_color = "#111111"

        # =========================
        # 1) TÍTULO E INTRODUCCIÓN
        # =========================
        titulo = Text(
            "Reglas de Derivación",
            font_size=64,
            color=WHITE
        )
        subtitulo = Text(
            "Suma, Producto y Cociente",
            font_size=36,
            color=GRAY_A
        ).next_to(titulo, DOWN)

        titulo_grupo = VGroup(titulo, subtitulo).move_to(ORIGIN)

        self.play(FadeIn(titulo_grupo, shift=UP), run_time=2)
        self.play(titulo_grupo.animate.scale(1.05), run_time=1)
        self.wait(3)

        # Encabezado arriba para dejar espacio
        self.play(
            titulo_grupo.animate.scale(0.7).to_edge(UP),
            run_time=1.5
        )
        self.wait(1)

        # =========================
        # 2) REGLA DE LA SUMA
        # =========================
        texto_intro_suma = Text(
            "Primero veremos la regla de la SUMA.",
            font_size=30,
            color=GRAY_A
        ).next_to(titulo_grupo, DOWN, buff=0.6)

        self.play(Write(texto_intro_suma), run_time=2)
        self.wait(2)

        regla_suma = MathTex(
            r"\frac{d}{dx}\big[f(x) + g(x)\big] = f'(x) + g'(x)",
            color=WHITE
        ).scale(0.9)
        regla_suma.next_to(texto_intro_suma, DOWN, buff=0.5)

        self.play(Write(regla_suma), run_time=2)
        self.wait(2)

        texto_suma_exp = Text(
            "La derivada de una suma es la suma de las derivadas.",
            font_size=28,
            color=GRAY_A
        ).next_to(regla_suma, DOWN, buff=0.5)

        self.play(Write(texto_suma_exp), run_time=2)
        self.wait(3)

        # Ejemplo polinómico
        ejemplo_suma_1 = MathTex(
            r"f(x) = x^{2}, \quad g(x) = 3x",
            color=WHITE
        ).scale(0.8)

        ejemplo_suma_2 = MathTex(
            r"\big(x^{2} + 3x\big)' = 2x + 3",
            color=YELLOW
        ).scale(0.9)

        grupo_suma_polinomio = VGroup(
            ejemplo_suma_1, ejemplo_suma_2
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        grupo_suma_polinomio.next_to(texto_suma_exp, DOWN, buff=0.6)

        self.play(
            LaggedStart(
                Write(ejemplo_suma_1),
                Write(ejemplo_suma_2),
                lag_ratio=0.4,
                run_time=3
            )
        )
        self.wait(3)

        texto_suma_pasos = Text(
            "Sumamos las funciones y luego derivamos término a término.",
            font_size=26,
            color=GRAY_A
        ).next_to(grupo_suma_polinomio, DOWN, buff=0.4)

        self.play(Write(texto_suma_pasos), run_time=2)
        self.wait(3)

        # Ejemplo trigonométrico
        ejemplo_suma_trig_1 = MathTex(
            r"h(x) = \sin(x) + \cos(x)",
            color=WHITE
        ).scale(0.8)
        ejemplo_suma_trig_2 = MathTex(
            r"h'(x) = \cos(x) - \sin(x)",
            color=GREEN_A
        ).scale(0.9)

        grupo_suma_trig = VGroup(
            ejemplo_suma_trig_1, ejemplo_suma_trig_2
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        grupo_suma_trig.next_to(texto_suma_pasos, DOWN, buff=0.5)

        self.play(
            LaggedStart(
                Write(ejemplo_suma_trig_1),
                Write(ejemplo_suma_trig_2),
                lag_ratio=0.4,
                run_time=3
            )
        )
        self.wait(4)

        # Pequeño indicativo
        self.play(
            Indicate(grupo_suma_trig, color=GREEN_A),
            run_time=2
        )
        self.wait(2)

        # =========================
        # LIMPIAR SECCIÓN SUMA
        # =========================
        self.play(
            FadeOut(texto_intro_suma),
            FadeOut(regla_suma),
            FadeOut(texto_suma_exp),
            FadeOut(grupo_suma_polinomio),
            FadeOut(texto_suma_pasos),
            FadeOut(grupo_suma_trig),
            run_time=2
        )
        self.wait(1)

        # =========================
        # 3) REGLA DEL PRODUCTO
        # =========================
        texto_intro_prod = Text(
            "Ahora vamos con la regla del PRODUCTO.",
            font_size=30,
            color=GRAY_A
        ).next_to(titulo_grupo, DOWN, buff=0.6)

        self.play(Write(texto_intro_prod), run_time=2)
        self.wait(2)

        regla_producto = MathTex(
            r"\frac{d}{dx}\big[f(x)\cdot g(x)\big] = f'(x)g(x) + f(x)g'(x)",
            color=WHITE
        ).scale(0.9)
        regla_producto.next_to(texto_intro_prod, DOWN, buff=0.5)

        self.play(Write(regla_producto), run_time=2)
        self.wait(2)

        texto_prod_exp = Text(
            "Cuando multiplicamos, derivamos una, dejamos la otra,\n"
            "y luego al revés, y sumamos esos dos resultados.",
            font_size=26,
            color=GRAY_A
        ).next_to(regla_producto, DOWN, buff=0.5)

        self.play(Write(texto_prod_exp), run_time=3)
        self.wait(3)

        # Ejemplo del producto: f(x)=x^2, g(x)=sen(x)
        f_g_def = MathTex(
            r"f(x) = x^{2}, \quad g(x) = \sin(x)",
            color=WHITE
        ).scale(0.8)

        derivadas_fg = MathTex(
            r"f'(x) = 2x, \quad g'(x) = \cos(x)",
            color=GREEN_A
        ).scale(0.8)

        grupo_fg = VGroup(f_g_def, derivadas_fg).arrange(
            DOWN, aligned_edge=LEFT, buff=0.3
        )
        grupo_fg.next_to(texto_prod_exp, DOWN, buff=0.5)

        self.play(
            LaggedStart(
                Write(f_g_def),
                Write(derivadas_fg),
                lag_ratio=0.4,
                run_time=3
            )
        )
        self.wait(3)

        # Pasos de la derivada del producto
        prod_paso1 = MathTex(
            r"\big(x^{2}\cdot \sin(x)\big)'",
            color=ORANGE
        ).scale(0.9)

        prod_paso2 = MathTex(
            r"= f'(x)g(x) + f(x)g'(x)",
            color=ORANGE
        ).scale(0.9)

        prod_paso3 = MathTex(
            r"= 2x\sin(x) + x^{2}\cos(x)",
            color=ORANGE
        ).scale(0.9)

        grupo_pasos_prod = VGroup(
            prod_paso1, prod_paso2, prod_paso3
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.25)

        grupo_pasos_prod.next_to(grupo_fg, DOWN, buff=0.6)

        self.play(Write(prod_paso1), run_time=2)
        self.wait(2)
        self.play(Write(prod_paso2), run_time=2)
        self.wait(2)
        self.play(Write(prod_paso3), run_time=3)
        self.wait(4)

        texto_prod_pasos = Text(
            "Primero usamos la fórmula con f y g,\n"
            "luego reemplazamos por 2x y sin(x), x² y cos(x).",
            font_size=26,
            color=GRAY_A
        ).next_to(grupo_pasos_prod, DOWN, buff=0.4)

        self.play(Write(texto_prod_pasos), run_time=3)
        self.wait(4)

        # =========================
        # LIMPIAR SECCIÓN PRODUCTO
        # =========================
        self.play(
            FadeOut(texto_intro_prod),
            FadeOut(regla_producto),
            FadeOut(texto_prod_exp),
            FadeOut(grupo_fg),
            FadeOut(grupo_pasos_prod),
            FadeOut(texto_prod_pasos),
            run_time=2
        )
        self.wait(1)

        # =========================
        # 4) REGLA DEL COCIENTE
        # =========================
        texto_intro_coc = Text(
            "Por último, la regla del COCIENTE.",
            font_size=30,
            color=GRAY_A
        ).next_to(titulo_grupo, DOWN, buff=0.6)

        self.play(Write(texto_intro_coc), run_time=2)
        self.wait(2)

        regla_cociente = MathTex(
            r"\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right]"
            r" = \frac{f'(x)g(x) - f(x)g'(x)}{\big(g(x)\big)^{2}}",
            color=WHITE
        ).scale(0.9)
        regla_cociente.next_to(texto_intro_coc, DOWN, buff=0.5)

        self.play(Write(regla_cociente), run_time=2)
        self.wait(2)

        texto_coc_exp = Text(
            "Aquí derivamos el de arriba y el de abajo,\n"
            "restamos en el numerador y abajo va g(x) al cuadrado.",
            font_size=26,
            color=GRAY_A
        ).next_to(regla_cociente, DOWN, buff=0.5)

        self.play(Write(texto_coc_exp), run_time=3)
        self.wait(3)

        # Ejemplo del cociente
        coc_ej_1 = MathTex(
            r"y = \frac{x^{2} + 1}{x - 1}",
            color=WHITE
        ).scale(0.8)
        coc_ej_2 = MathTex(
            r"y' = \frac{(2x)(x - 1) - (x^{2} + 1)(1)}{(x - 1)^{2}}",
            color=YELLOW
        ).scale(0.8)

        grupo_coc = VGroup(coc_ej_1, coc_ej_2).arrange(
            DOWN, aligned_edge=LEFT, buff=0.3
        )
        grupo_coc.next_to(texto_coc_exp, DOWN, buff=0.6)

        self.play(
            LaggedStart(
                Write(coc_ej_1),
                Write(coc_ej_2),
                lag_ratio=0.4,
                run_time=3
            )
        )
        self.wait(4)

        texto_coc_pasos = Text(
            "Arriba usamos f'(x)g(x) - f(x)g'(x),\n"
            "y todo eso lo dividimos por (x - 1)².",
            font_size=26,
            color=GRAY_A
        ).next_to(grupo_coc, DOWN, buff=0.4)

        self.play(Write(texto_coc_pasos), run_time=3)
        self.wait(4)

        # =========================
        # LIMPIAR SECCIÓN COCIENTE
        # =========================
        self.play(
            FadeOut(texto_intro_coc),
            FadeOut(regla_cociente),
            FadeOut(texto_coc_exp),
            FadeOut(grupo_coc),
            FadeOut(texto_coc_pasos),
            run_time=2
        )
        self.wait(1)

        # =========================
        # 5) RESUMEN FINAL
        # =========================
        titulo_resumen = Text(
            "Resumen de las Reglas",
            font_size=48,
            color=WHITE
        ).to_edge(UP)

        regla_suma_res = MathTex(
            r"\frac{d}{dx}\big[f(x) + g(x)\big] = f'(x) + g'(x)",
            color=WHITE
        ).scale(0.8)
        regla_prod_res = MathTex(
            r"\frac{d}{dx}\big[f(x)g(x)\big] = f'(x)g(x) + f(x)g'(x)",
            color=WHITE
        ).scale(0.8)
        regla_coc_res = MathTex(
            r"\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right]"
            r" = \frac{f'(x)g(x) - f(x)g'(x)}{\big(g(x)\big)^{2}}",
            color=WHITE
        ).scale(0.8)

        grupo_resumen = VGroup(
            regla_suma_res, regla_prod_res, regla_coc_res
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        grupo_resumen.next_to(titulo_resumen, DOWN, buff=0.6)

        texto_cierre = Text(
            "Con estas tres reglas podemos derivar muchas funciones diferentes.",
            font_size=30,
            color=GRAY_A
        ).next_to(grupo_resumen, DOWN, buff=0.6)

        self.play(FadeIn(titulo_resumen, shift=DOWN), run_time=2)
        self.play(
            LaggedStart(
                FadeIn(regla_suma_res, shift=RIGHT),
                FadeIn(regla_prod_res, shift=RIGHT),
                FadeIn(regla_coc_res, shift=RIGHT),
                lag_ratio=0.4,
                run_time=4
            )
        )
        self.wait(4)

        self.play(Write(texto_cierre), run_time=3)
        self.wait(8)

        # Espera extra para asegurar duración > 2 minutos
        self.wait(40)

        self.play(
            FadeOut(titulo_resumen),
            FadeOut(grupo_resumen),
            FadeOut(texto_cierre),
            run_time=2
        )
        self.wait(2)
