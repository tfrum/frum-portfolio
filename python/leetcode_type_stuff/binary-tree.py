class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._add_recursive(key, self.root)

    def _add_recursive(self, key, node):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._add_recursive(key, node.left)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._add_recursive(key, node.right)

    def update(self, old_key, new_key):
        self.remove(old_key)
        self.add(new_key)

    def remove(self, key):
        self.root = self._remove_recursive(key, self.root)

    def _remove_recursive(self, key, node):
        if node is None:
            return node
        if key < node.val:
            node.left = self._remove_recursive(key, node.left)
        elif key > node.val:
            node.right = self._remove_recursive(key, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            temp = self._min_value_node(node.right)
            node.val = temp.val
            node.right = self._remove_recursive(temp.val, node.right)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        elements = []
        self._inorder_traversal_recursive(self.root, elements)
        return elements

    def _inorder_traversal_recursive(self, node, elements):
        if node:
            self._inorder_traversal_recursive(node.left, elements)
            elements.append(node.val)
            self._inorder_traversal_recursive(node.right, elements)

# Testing isn't just a city in England
tree = BinaryTree()
tree.add(5)
tree.add(3)
tree.add(8)
tree.add(2)
tree.add(4)
tree.add(7)
tree.add(9)

# Initial inorder traversal test
assert tree.inorder_traversal() == [2, 3, 4, 5, 7, 8, 9], "Initial inorder traversal failed"

# Update operation test
tree.update(3, 6)
assert tree.inorder_traversal() == [2, 4, 5, 6, 7, 8, 9], "Inorder traversal after update failed"

# Remove operation test
tree.remove(6)
assert tree.inorder_traversal() == [2, 4, 5, 7, 8, 9], "Inorder traversal after remove failed"
