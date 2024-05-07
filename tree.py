from manim import *


class BinaryTreeVisualization(Scene):
    def construct(self):
        title = Text("Binary Tree Operations").scale(0.9)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Initialize an empty list to hold nodes and their positions
        tree_nodes = {}
        lines = {}
        root_pos = UP * 2

        # Function to add nodes
        def add_node(value, pos=root_pos, parent=None, side=None):
            node = Circle(radius=0.5, color=WHITE).move_to(pos)
            num = Text(str(value), color=WHITE).scale(0.8).move_to(node.get_center())
            tree_nodes[value] = (node, num, pos)
            if parent:
                line = Line(tree_nodes[parent][0].get_center(), node.get_center(), color=WHITE)
                lines[(parent, value)] = line
                self.play(Create(line))
            self.play(Create(node), Write(num))
            return node

        # Add nodes to the tree
        root = add_node(10)  # Root node
        node5 = add_node(5, pos=root_pos + LEFT + DOWN, parent=10)
        node15 = add_node(15, pos=root_pos + RIGHT + DOWN, parent=10)
        node3 = add_node(3, pos=root_pos + 2 * LEFT + 2 * DOWN, parent=5)
        node7 = add_node(7, pos=root_pos + LEFT / 2 + 2 * DOWN, parent=5)

        self.wait(2)

        # Function to delete nodes
        def delete_node(value):
            if value in tree_nodes:
                node, num, _ = tree_nodes[value]
                self.play(Indicate(node, color=RED))
                self.wait(1)
                self.play(FadeOut(node), FadeOut(num))
                if (10, value) in lines:
                    self.play(FadeOut(lines[(10, value)]))
                del tree_nodes[value]
                return True
            return False

        # Function to move nodes
        def move_node(value, new_pos):
            if value in tree_nodes:
                node, num, _ = tree_nodes[value]
                tree_nodes[value] = (node, num, new_pos)  # Update position in the tree_nodes dictionary
                self.play(node.animate.move_to(new_pos), num.animate.move_to(new_pos))
                if (5, value) in lines:  # Redraw line from parent if exists
                    self.play(Transform(lines[(5, value)], Line(tree_nodes[10][0].get_center(), new_pos)))

        # Deleting node 5 and moving node 7 to its position
        if delete_node(5):
            move_node(7, root_pos + LEFT + DOWN)

        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])

# To run the scene, use the following command in your terminal:
# manim -pql binary_tree_visualization.py BinaryTreeVisualization
