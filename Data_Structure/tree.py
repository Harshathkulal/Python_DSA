class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

# Example Usage:
# Creating a tree with a root node and two child nodes
root = TreeNode("Root")
child1 = TreeNode("Child 1")
child2 = TreeNode("Child 2")

root.add_child(child1)
root.add_child(child2)

# Adding more child nodes to Child 1
child1.add_child(TreeNode("Child 1.1"))
child1.add_child(TreeNode("Child 1.2"))

# Adding a child node to Child 2
child2.add_child(TreeNode("Child 2.1"))

# Traversing the tree (a simple depth-first traversal)
def traverse(node):
    print(node.data)
    for child in node.children:
        traverse(child)

# Traversing the tree starting from the root
traverse(root)
