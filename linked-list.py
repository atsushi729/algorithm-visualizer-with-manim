from manim import *


class LinkedListVisualization(Scene):
    def construct(self):
        title = Text("Linked List Operations Visualization").scale(0.9)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Initial elements in the linked list
        elements = [5, 3, 8, 1, 4]
        linked_list = VGroup()  # Group for linked list elements

        # Generate linked list nodes with numbers inside
        for i, elem in enumerate(elements):
            node = Square(side_length=1).set_stroke(color=WHITE, width=3)
            num = Text(str(elem), color=WHITE).move_to(node.get_center())
            node_group = VGroup(node, num)

            # Create arrow if not the last element
            if i < len(elements):
                arrow = Arrow(start=node.get_right(), end=node.get_right() + RIGHT * 0.8, buff=0.1, stroke_width=2)
                node_group.add(arrow)

            linked_list.add(node_group)

        # Position the linked list nodes in a row
        linked_list.arrange(RIGHT, buff=0.1)
        linked_list.to_edge(UP)

        # Animate creation of the linked list nodes
        self.play(Create(linked_list))
        self.wait(1)

        # Highlight the head of the linked list
        head_highlight = SurroundingRectangle(linked_list[0], color=BLUE, buff=0.1)
        head_text = Text("Head", color=BLUE).scale(0.7).next_to(linked_list[0], UP)
        self.play(Create(head_highlight), Write(head_text))
        self.wait(1)

        # Adding an element to the linked list
        new_element = 6
        new_node = Square(side_length=1).set_stroke(color=WHITE, width=3)
        new_num = Text(str(new_element), color=WHITE).move_to(new_node.get_center())
        new_group = VGroup(new_node, new_num)
        new_group.next_to(linked_list, RIGHT, buff=0.1)

        self.play(Write(Text("Adding 6 to the linked list").next_to(linked_list, DOWN, buff=0.5)))
        self.play(AnimationGroup(Create(new_node), Write(new_num), lag_ratio=0.5))
        linked_list.add(new_group)
        self.wait(2)

        # Update the tail highlight
        tail_highlight = SurroundingRectangle(new_group, color=GREEN, buff=0.1)
        tail_text = Text("Tail", color=GREEN).scale(0.7).next_to(new_group, UP)
        self.play(Create(tail_highlight), Write(tail_text))
        self.wait(1)

        # Deleting an element from the linked list (element 8)
        delete_index = 2
        delete_highlight = SurroundingRectangle(linked_list[delete_index], color=RED, buff=0.1)

        self.play(Write(Text("Deleting 8 from the linked list").next_to(linked_list, DOWN, buff=1.5)))
        self.play(Create(delete_highlight))
        self.wait(1)
        self.play(FadeOut(linked_list[delete_index]), FadeOut(delete_highlight))

        # Update arrows
        if delete_index > 0:
            previous_node = linked_list[delete_index - 1]
            next_node = linked_list[delete_index + 1]
            new_arrow = Arrow(start=previous_node[0].get_right(), end=next_node[0].get_left(), buff=0.1, stroke_width=2)
            self.play(Create(new_arrow))
            previous_node.add(new_arrow)

        linked_list.remove(linked_list[delete_index])

        # Rearrange nodes after deletion and ensure new element is correctly positioned
        self.play(linked_list.animate.arrange(RIGHT, buff=0.1).to_edge(UP))

        # Move highlights together with nodes
        self.play(head_highlight.animate.move_to(linked_list[0]), head_text.animate.next_to(linked_list[0], UP))
        self.play(tail_highlight.animate.move_to(linked_list[-1]), tail_text.animate.next_to(linked_list[-1], UP))

        self.wait(2)

        # Cleanup
        self.play(FadeOut(linked_list), FadeOut(head_highlight), FadeOut(head_text), FadeOut(tail_highlight),
                  FadeOut(tail_text))

# To run the scene, use the following command in your terminal:
# manim -pql linked_list_visualization.py LinkedListVisualization
