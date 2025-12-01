from manim import *


class LimitesAnimation(Scene):
    def construct(self):
        self.show_title()
        self.show_index()
        self.method_substitution()
        self.method_factorization()
        self.method_rationalization()
        self.show_summary()

    def show_title(self):
        """Presenta el título principal y lo fija en la parte superior."""
        main_title = Text("Métodos para Resolver Límites", font_size=48, weight=BOLD)
        subtitle = Text("Limits Solution Methods", font_size=28, color=GRAY)
        subtitle.next_to(main_title, DOWN, buff=0.3)

        self.play(Write(main_title), Write(subtitle))
        self.wait(2)
        self.play(FadeOut(subtitle), main_title.animate.scale(0.7).to_edge(UP))
        self.wait(0.5)

        self.main_title = main_title

    def show_index(self):
        """Muestra los tres métodos que se explicarán."""
        index_title = Text("Contenido:", font_size=32, color=YELLOW).shift(UP * 1.5)
        method1 = Text("1. Sustitución directa", font_size=28, color=BLUE).shift(UP * 0.3)
        method2 = Text("2. Factorización (caso 0/0)", font_size=28, color=GREEN).shift(DOWN * 0.5)
        method3 = Text("3. Racionalización (raíces)", font_size=28, color=RED).shift(DOWN * 1.3)

        self.play(Write(index_title))
        self.wait(0.5)
        for mob in (method1, method2, method3):
            self.play(Write(mob))
            self.wait(0.5)
        self.wait(2)

        self.play(*[FadeOut(mob) for mob in (index_title, method1, method2, method3)])
        self.wait(0.5)

    def method_substitution(self):
        """Desarrollo del método de sustitución directa."""
        self.new_section("Método 1: Sustitución Directa", BLUE)

        explanation = self.build_text_block(
            [
                "Cuando el límite NO es indeterminado,",
                "solo reemplazamos el valor de x.",
            ],
            font_size=26,
        )
        explanation.next_to(self.main_title, DOWN, buff=0.4).to_edge(LEFT, buff=1)
        self.play(LaggedStart(*[Write(line) for line in explanation], lag_ratio=0.4))
        self.wait(1.5)
        self.play(FadeOut(explanation))

        example_group = self.build_example_block(
            Text("Ejemplo:", font_size=28, color=LIGHT_GRAY),
            MathTex(r"\lim_{x \to 2} \left(3x^2 + 2x - 1\right)", font_size=44, color=BLUE),
        )
        example_group.next_to(self.main_title, DOWN, buff=0.8).to_edge(LEFT, buff=1)
        self.play(Write(example_group))
        self.wait(1.5)

        step1 = self.build_step_block(
            "Paso 1: Sustituimos x = 2",
            MathTex(r"= 3(2)^2 + 2(2) - 1", font_size=40, color=BLUE),
        )
        step1.to_edge(RIGHT, buff=1).align_to(example_group, UP)
        self.play(Write(step1))
        self.wait(0.8)

        step2 = self.build_step_block(
            "Paso 2: Evaluamos la expresión",
            MathTex(r"= 12 + 4 - 1 = 15", font_size=40, color=YELLOW),
        )
        step2.to_edge(RIGHT, buff=1)
        step2.next_to(step1, DOWN, aligned_edge=LEFT, buff=0.6)
        self.play(Write(step2))
        self.wait(1)

        result_group = self.build_example_block(
            Text("Resultado:", font_size=26, color=YELLOW),
            MathTex(r"15", font_size=62, color=YELLOW),
        )
        result_group.to_edge(RIGHT, buff=1)
        result_group.next_to(step2, DOWN, aligned_edge=LEFT, buff=0.7)
        result_box = SurroundingRectangle(result_group[1], color=YELLOW, buff=0.25, corner_radius=0.15)
        self.play(Write(result_group[0]))
        self.play(Write(result_group[1]), Create(result_box))
        self.wait(1.5)

        self.play(
            FadeOut(example_group),
            FadeOut(step1),
            FadeOut(step2),
            FadeOut(result_group),
            FadeOut(result_box),
        )
        self.wait(0.5)

    def method_factorization(self):
        """Explica el caso indeterminado 0/0 resuelto por factorización."""
        self.new_section("Método 2: Factorización", GREEN)

        explanation = self.build_text_block(
            ["Si al sustituir obtenemos 0/0,", "factorizamos y simplificamos."],
            font_size=26,
        )
        explanation.next_to(self.main_title, DOWN, buff=0.4).to_edge(LEFT, buff=1)
        self.play(LaggedStart(*[Write(line) for line in explanation], lag_ratio=0.4))
        self.wait(1.2)
        self.play(FadeOut(explanation))

        example_group = self.build_example_block(
            Text("Ejemplo:", font_size=28, color=LIGHT_GRAY),
            MathTex(r"\lim_{x \to 3} \frac{x^2 - 9}{x - 3}", font_size=44, color=GREEN),
        )
        example_group.next_to(self.main_title, DOWN, buff=0.8).to_edge(LEFT, buff=1)
        self.play(Write(example_group))
        self.wait(1.5)

        verify_block = self.build_step_block(
            "Paso 1: Verificar indeterminación",
            MathTex(r"\frac{3^2 - 9}{3 - 3} = \frac{0}{0}", font_size=36, color=YELLOW),
        )
        verify_block.to_edge(RIGHT, buff=1).align_to(example_group, UP)
        highlight = SurroundingRectangle(verify_block[1], color=YELLOW, buff=0.2, corner_radius=0.1)
        self.play(Write(verify_block))
        self.play(Create(highlight))
        self.wait(1.5)
        self.play(FadeOut(verify_block), FadeOut(highlight))

        factor_block = self.build_step_block(
            "Paso 2: Factorizamos el numerador",
            MathTex(r"= \lim_{x \to 3} \frac{(x + 3)(x - 3)}{x - 3}", font_size=40, color=GREEN),
        )
        factor_block.to_edge(RIGHT, buff=1).align_to(example_group, UP)
        self.play(Write(factor_block))
        self.wait(1)

        simplify_block = self.build_step_block(
            "Paso 3: Cancelamos términos comunes",
            MathTex(r"= \lim_{x \to 3} (x + 3)", font_size=40, color=GREEN),
        )
        simplify_block.to_edge(RIGHT, buff=1)
        simplify_block.next_to(factor_block, DOWN, aligned_edge=LEFT, buff=0.6)
        self.play(Write(simplify_block))
        self.wait(1)

        substitute_block = self.build_step_block(
            "Paso 4: Sustituimos x = 3",
            MathTex(r"= 3 + 3 = 6", font_size=42, color=GREEN),
        )
        substitute_block.to_edge(RIGHT, buff=1)
        substitute_block.next_to(simplify_block, DOWN, aligned_edge=LEFT, buff=0.6)
        self.play(Write(substitute_block))
        self.wait(1)

        result_group = self.build_example_block(
            Text("Resultado:", font_size=26, color=YELLOW),
            MathTex(r"6", font_size=58, color=YELLOW),
        )
        result_group.to_edge(RIGHT, buff=1)
        result_group.next_to(substitute_block, DOWN, aligned_edge=LEFT, buff=0.7)
        result_box = SurroundingRectangle(result_group[1], color=YELLOW, buff=0.25, corner_radius=0.15)
        self.play(Write(result_group[0]))
        self.play(Write(result_group[1]), Create(result_box))
        self.wait(1.5)

        self.play(
            FadeOut(example_group),
            FadeOut(factor_block),
            FadeOut(simplify_block),
            FadeOut(substitute_block),
            FadeOut(result_group),
            FadeOut(result_box),
        )
        self.wait(0.5)

    def method_rationalization(self):
        """Ilustra la racionalización en límites con raíces."""
        self.new_section("Método 3: Racionalización", RED)

        explanation = self.build_text_block(
            ["Si una raíz provoca 0/0,", "multiplicamos por el conjugado."],
            font_size=26,
        )
        explanation.next_to(self.main_title, DOWN, buff=0.4).to_edge(LEFT, buff=1)
        self.play(LaggedStart(*[Write(line) for line in explanation], lag_ratio=0.4))
        self.wait(1.2)
        self.play(FadeOut(explanation))

        example_group = self.build_example_block(
            Text("Ejemplo:", font_size=28, color=LIGHT_GRAY),
            MathTex(r"\lim_{x \to 4} \frac{\sqrt{x} - 2}{x - 4}", font_size=42, color=RED),
        )
        example_group.next_to(self.main_title, DOWN, buff=0.8).to_edge(LEFT, buff=1)
        self.play(Write(example_group))
        self.wait(1.4)

        verify_block = self.build_step_block(
            "Paso 1: Revisamos la indeterminación",
            MathTex(r"\frac{\sqrt{4} - 2}{4 - 4} = \frac{0}{0}", font_size=34, color=YELLOW),
        )
        verify_block.to_edge(RIGHT, buff=1).align_to(example_group, UP)
        highlight = SurroundingRectangle(verify_block[1], color=YELLOW, buff=0.2, corner_radius=0.1)
        self.play(Write(verify_block))
        self.play(Create(highlight))
        self.wait(1.2)
        self.play(FadeOut(verify_block), FadeOut(highlight))

        conjugate_block = self.build_step_block(
            "Paso 2: Identificamos el conjugado",
            MathTex(r"\sqrt{x} + 2", font_size=36, color=ORANGE),
        )
        conjugate_block.to_edge(RIGHT, buff=1).align_to(example_group, UP)
        self.play(Write(conjugate_block))
        self.wait(1)
        self.play(FadeOut(conjugate_block))

        multiply_block = self.build_step_block(
            "Paso 3: Multiplicamos por el conjugado",
            MathTex(
            r"\frac{\sqrt{x} - 2}{x - 4} \cdot \frac{\sqrt{x} + 2}{\sqrt{x} + 2}",
            font_size=34,
            color=RED,
        ),
        )
        multiply_block.to_edge(RIGHT, buff=1).align_to(example_group, UP)
        self.play(Write(multiply_block))
        self.wait(1.2)

        diff_block = self.build_step_block(
            "Paso 4: Aplicamos diferencia de cuadrados",
            MathTex(
            r"= \frac{x - 4}{(x - 4)(\sqrt{x} + 2)}",
            font_size=36,
            color=RED,
        ),
        )
        diff_block.to_edge(RIGHT, buff=1)
        diff_block.next_to(multiply_block, DOWN, aligned_edge=LEFT, buff=0.6)
        self.play(Write(diff_block))
        self.wait(1)

        simplify_block = self.build_step_block(
            "Paso 5: Simplificamos términos",
            MathTex(
            r"= \frac{1}{\sqrt{x} + 2}",
            font_size=38,
            color=RED,
        ),
        )
        simplify_block.to_edge(RIGHT, buff=1)
        simplify_block.next_to(diff_block, DOWN, aligned_edge=LEFT, buff=0.6)
        self.play(Write(simplify_block))
        self.wait(1)

        substitute_block = self.build_step_block(
            "Paso 6: Sustituimos x = 4",
            MathTex(
            r"= \frac{1}{\sqrt{4} + 2} = \frac{1}{4}",
            font_size=38,
            color=YELLOW,
        ),
        )
        substitute_block.to_edge(RIGHT, buff=1)
        substitute_block.next_to(simplify_block, DOWN, aligned_edge=LEFT, buff=0.6)
        self.play(Write(substitute_block))
        self.wait(1.4)

        result_group = self.build_example_block(
            Text("Resultado:", font_size=26, color=YELLOW),
            MathTex(r"\frac{1}{4}", font_size=58, color=YELLOW),
        )
        result_group.to_edge(RIGHT, buff=1)
        result_group.next_to(substitute_block, DOWN, aligned_edge=LEFT, buff=0.7)
        result_box = SurroundingRectangle(result_group[1], color=YELLOW, buff=0.25, corner_radius=0.15)
        self.play(Write(result_group[0]))
        self.play(Write(result_group[1]), Create(result_box))
        self.wait(1.6)

        self.play(
            FadeOut(example_group),
            FadeOut(multiply_block),
            FadeOut(diff_block),
            FadeOut(simplify_block),
            FadeOut(substitute_block),
            FadeOut(result_group),
            FadeOut(result_box),
        )
        self.wait(0.5)

    def show_summary(self):
        """Cierra el video con un resumen de los métodos."""
        self.clear_scene(keep_title=False)

        summary_title = Text("Resumen de Métodos", font_size=42, weight=BOLD, color=YELLOW).to_edge(UP)
        summary1 = Text("1. Sustitución directa: úsala cuando no haya indeterminaciones.", font_size=24, color=BLUE).shift(
            UP * 0.8
        )
        summary2 = Text("2. Factorización: elimina expresiones que generen 0/0.", font_size=24, color=GREEN).shift(
            UP * 0.1
        )
        summary3 = Text("3. Racionalización: multiplica por el conjugado para raíces.", font_size=24, color=RED).shift(
            DOWN * 0.6
        )
        conclusion = Text("¡Elige el método según el tipo de límite!", font_size=26, color=YELLOW).shift(DOWN * 1.6)

        self.play(Write(summary_title))
        self.wait(0.5)
        for item in (summary1, summary2, summary3, conclusion):
            self.play(Write(item))
            self.wait(0.5)
        self.wait(3)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)

    def clear_scene(self, keep_title=True):
        """Elimina los objetos de la escena, conservando el título si se requiere."""
        to_fade = []
        for mob in list(self.mobjects):
            if keep_title and mob is self.main_title:
                continue
            to_fade.append(mob)

        if to_fade:
            self.play(*[FadeOut(mob) for mob in to_fade])
        if not keep_title:
            self.main_title = None
        self.wait(0.5)

    def new_section(self, title_text, color):
        """Limpia la escena y coloca el nuevo título del método."""
        self.clear_scene(keep_title=True)
        new_title = Text(title_text, font_size=36, color=color)
        new_title.to_edge(UP).shift(DOWN * 0.5)
        self.play(Transform(self.main_title, new_title))
        self.wait(0.5)

    def build_text_block(self, lines, font_size=26, color=WHITE, max_width=11):
        block = VGroup(
            *[Text(line, font_size=font_size, color=color) for line in lines]
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        self.fit_width(block, max_width)
        block.set_x(0)
        return block

    def build_example_block(self, label, expression, max_width=11):
        self.fit_width(label, max_width)
        self.fit_width(expression, max_width)
        block = VGroup(label, expression).arrange(DOWN, buff=0.3)
        self.fit_width(block, max_width)
        block.set_x(0)
        return block

    def build_step_block(self, title, expression, max_width=10.5):
        header = Text(title, font_size=24)
        self.fit_width(header, max_width)
        self.fit_width(expression, max_width)
        block = VGroup(header, expression).arrange(DOWN, buff=0.3)
        self.fit_width(block, max_width)
        block.set_x(0)
        return block

    def fit_width(self, mob, max_width):
        if mob.width > max_width:
            mob.scale(max_width / mob.width)
        return mob
