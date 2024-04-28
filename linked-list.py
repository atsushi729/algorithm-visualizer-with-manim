from manim import *

class LinkedListVisualization(Scene):
    def construct(self):
        title = Text("Linked List Visualization", font_size=24)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        linked_list = []
        texts = []
        arrows = []
        action_text = Text('', font_size=36).to_corner(UP + RIGHT)

        def create_node(text, color=WHITE):
            node = Circle(radius=0.75, color=color)
            txt = Text(text, color=BLACK, font_size=32).move_to(node.get_center())
            return node, txt

        def create_arrow(from_node, to_node):
            return Arrow(from_node.get_right(), to_node.get_left(), buff=0.1)

        # Function to visualize adding an element to the linked list
        def add_element(element):
            new_action_text = Text(f'Add({element})', font_size=36).to_corner(UP + RIGHT)
            self.play(Transform(action_text, new_action_text))
            node, txt = create_node(element)
            if linked_list:
                node.next_to(linked_list[-1], RIGHT, buff=1)
                arrow = create_arrow(linked_list[-1], node)
                arrows.append(arrow)
                self.play(Create(arrow))
            else:
                node.move_to(ORIGIN)
            txt.move_to(node.get_center())
            linked_list.append(node)
            texts.append(txt)
            self.play(Create(node), Write(txt))

        # Function to visualize removing an element from the linked list
        def remove_element():
            if linked_list:
                node = linked_list.pop()
                txt = texts.pop()
                if arrows:
                    arrow = arrows.pop()
                    self.play(FadeOut(arrow))
                new_action_text = Text(f'Remove({txt.text})', font_size=36).to_corner(UP + RIGHT)
                self.play(Transform(action_text, new_action_text))
                self.play(FadeOut(node), FadeOut(txt))

        # Add and remove elements from the linked list with operation text
        add_element("5")
        self.wait(1)
        add_element("3")
        self.wait(1)
        add_element("8")
        self.wait(1)
        remove_element()
        self.wait(1)
        add_element("2")
        self.wait(1)
        remove_element()
        self.wait(2)

# To run the scene, use the following command in your terminal:
# manim -pql linked_list_visualization.py LinkedListVisualization
