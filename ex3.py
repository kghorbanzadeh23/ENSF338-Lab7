class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.height = 1
        self.balance = 0

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return Node(key)
        
        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        else:
            root.right = self._insert_recursive(root.right, key)

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))
        root.balance = self._get_balance(root)

        if root.balance > 1:
            if key < root.left.key:
                root = self._rotate_right(root)
            else:
                print("Case #3a: adding a node to an outside subtree")
                root.left = self._rotate_left(root.left)
                root = self._rotate_right(root)
        elif root.balance < -1:
            if key > root.right.key:
                root = self._rotate_left(root)
            else:
                print("Case #3a: adding a node to an outside subtree")
                root.right = self._rotate_right(root.right)
                root = self._rotate_left(root)

        return root

    def _get_height(self, node):
        if node is None:
            return 0
        return node.height

    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        z.balance = self._get_balance(z)
        y.balance = self._get_balance(y)
        return y

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        z.balance = self._get_balance(z)
        y.balance = self._get_balance(y)
        return y

    def print_tree(self):
        if self.root is not None:
            self._print_tree_recursive(self.root)

    def _print_tree_recursive(self, node):
        if node is not None:
            self._print_tree_recursive(node.left)
            print(f"({node.key}, Balance: {node.balance})", end=" ")
            self._print_tree_recursive(node.right)

if __name__ == "__main__":
    tree = AVLTree()

    print("Test Case 1: Adding a node resulting in case 1 (Right Rotation)")
    tree.insert(30)
    tree.insert(20)
    tree.insert(10)
    print("Test Case 1:")
    tree.print_tree()
    print("\n")

    print("Test Case 2: Adding a node resulting in case 2 (Left Rotation)")
    tree.insert(40)
    tree.insert(50)
    print("Test Case 2:")
    tree.print_tree()
    print("\n")

    print("Test Case 3a: Adding a node resulting in case 3a (Left-Right Rotation)")
    tree.insert(45)
    print("Test Case 3a:")
    tree.print_tree()
    print("\n")

    print("Test Case 3b: not supported")
    tree.insert(35)
    print("Test Case 3b:")
    tree.print_tree()
    print("\n")

    # Additional case to show the tree structure
    print("Test Case 4: More insertions to demonstrate AVL balancing")
    tree.insert(55)
    tree.insert(5)  # This may trigger another balancing rotation
    print("Test Case 4:")
    tree.print_tree()
    print()

