from manim import *


class StackVisualization(Scene):
    def construct(self):
        title = Text("Stack Visualization", font_size=24)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        stack = []
        texts = []
        action_text = Text('', font_size=36).to_corner(UP + RIGHT)

        def create_box(text, color=WHITE):
            box = Rectangle(width=2, height=1, color=color)
            txt = Text(text, color=BLACK, font_size=32).move_to(box.get_center())
            return box, txt

        # Function to visualize pushing an element onto the stack
        def push(element):
            # Update action text to show Push operation
            new_action_text = Text(f'Push({element})', font_size=36).to_corner(UP + RIGHT)
            self.play(Transform(action_text, new_action_text))
            box, txt = create_box(element)
            if stack:  # if there are already boxes, position above the last one
                box.next_to(stack[-1], UP, buff=0)
            else:  # if this is the first box, position it at the center
                box.move_to(ORIGIN)
            txt.move_to(box.get_center())
            stack.append(box)
            texts.append(txt)
            self.play(Create(box), Write(txt))

        # Function to visualize popping an element from the stack
        def pop():
            if stack:
                # Update action text to show Pop operation
                element = texts[-1].text
                new_action_text = Text(f'Pop({element})', font_size=36).to_corner(UP + RIGHT)
                self.play(Transform(action_text, new_action_text))
                box = stack.pop()
                txt = texts.pop()
                self.play(FadeOut(box), FadeOut(txt))

        # Push and pop elements onto the stack with operation text
        push("5")
        self.wait(1)
        push("3")
        self.wait(1)
        push("8")
        self.wait(1)
        pop()
        self.wait(1)
        push("2")
        self.wait(1)
        pop()
        self.wait(2)

# To run the scene, use the following command in your terminal:
# manim -pql stack_visualization.py StackVisualization
