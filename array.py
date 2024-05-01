from manim import *


class ArrayVisualization(Scene):
    def construct(self):
        title = Text("Array Operations Visualization").scale(0.9)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Create an array container
        elements = [5, 3, 8, 1, 4]  # Initial elements in the array
        array_cells = VGroup()  # Group for array elements

        # Generate array cells with numbers inside
        for elem in elements:
            cell = Square(side_length=1).set_stroke(color=WHITE, width=3)
            num = Text(str(elem), color=WHITE).move_to(cell.get_center())
            array_cells.add(VGroup(cell, num))

        # Position the array cells in a row
        array_cells.arrange(RIGHT, buff=0.1)
        array_cells.to_edge(UP)

        # Animate creation of the array cells
        self.play(Create(array_cells))
        self.wait(1)

        # Adding an element to the array
        new_element = 6
        new_cell = Square(side_length=1).set_stroke(color=WHITE, width=3)
        new_num = Text(str(new_element), color=WHITE).move_to(new_cell.get_center())
        new_group = VGroup(new_cell, new_num)
        new_group.next_to(array_cells, RIGHT, buff=0.1)

        self.play(Write(Text("Adding 6 to the array").next_to(array_cells, DOWN, buff=0.5)))
        self.play(AnimationGroup(Create(new_cell), Write(new_num), lag_ratio=0.5))
        array_cells.add(new_group)
        self.wait(2)

        # Deleting an element from the array (element 8)
        delete_index = 2
        delete_highlight = SurroundingRectangle(array_cells[delete_index], color=RED, buff=0.1)

        self.play(Write(Text("Deleting 8 from the array").next_to(array_cells, DOWN, buff=1.5)))
        self.play(Create(delete_highlight))
        self.wait(1)
        self.play(FadeOut(array_cells[delete_index]), FadeOut(delete_highlight))
        array_cells.remove(array_cells[delete_index])

        # Rearrange cells after deletion and ensure new element is correctly positioned
        self.play(array_cells.animate.arrange(RIGHT, buff=0.1).to_edge(UP))
        self.wait(2)

        # Cleanup
        self.play(FadeOut(array_cells))

# To run the scene, use the following command in your terminal:
# manim -pql array_visualization.py ArrayVisualization
