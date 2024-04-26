from manim import *


class QueueVisualization(Scene):
    def construct(self):
        title = Text("Queue Visualization", font_size=24)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        queue = []
        texts = []
        action_text = Text('', font_size=36).to_corner(UP + RIGHT)

        def create_box(text, color=WHITE):
            box = Rectangle(width=2, height=1, color=color)
            txt = Text(text, color=BLACK, font_size=32).move_to(box.get_center())
            return box, txt

        # Function to visualize enqueuing an element onto the queue
        def enqueue(element):
            new_action_text = Text(f'Enqueue({element})', font_size=36).to_corner(UP + RIGHT)
            self.play(Transform(action_text, new_action_text))
            box, txt = create_box(element)

            # Start offscreen to the right
            start_position = RIGHT * (4 + len(queue))
            box.move_to(start_position)
            txt.move_to(start_position)

            end_position = ORIGIN
            if queue:  # if there are already boxes, position to the right of the last one
                end_position = queue[-1].get_right() + RIGHT * 1.5
            else:  # if this is the first box, start from the original position
                end_position = 2 * LEFT

            # Slide in the new element from the right to the correct position in the queue
            self.play(
                box.animate.move_to(end_position),
                txt.animate.move_to(end_position)
            )

            queue.append(box)
            texts.append(txt)
            # Shift all boxes to the left to make space for the new element
            if len(queue) > 1:
                self.play(*[box.animate.shift(LEFT * 2) for box in queue[:-1]])
            self.play(Create(box), Write(txt))

        # Function to visualize dequeuing an element from the queue
        def dequeue():
            if queue:
                box = queue.pop(0)
                txt = texts.pop(0)
                element = txt.text
                new_action_text = Text(f'Dequeue({element})', font_size=36).to_corner(UP + RIGHT)
                self.play(Transform(action_text, new_action_text))
                # Shift remaining elements to the left
                self.play(*[box.animate.shift(LEFT * 2.1) for box in queue])
                self.play(FadeOut(box), FadeOut(txt))

        # Enqueue and dequeue elements onto the queue with operation text
        enqueue("5")
        self.wait(1)
        enqueue("3")
        self.wait(1)
        enqueue("8")
        self.wait(1)
        dequeue()
        self.wait(1)
        enqueue("2")
        self.wait(1)
        dequeue()
        self.wait(2)

# To run the scene, use the following command in your terminal:
# manim -pql queue_visualization.py QueueVisualization
