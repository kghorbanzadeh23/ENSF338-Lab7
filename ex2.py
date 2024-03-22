class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.height = 1  # Height of the node
        self.balance = 0  # Balance factor

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

        # Update height and balance factor
        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))
        root.balance = self._get_balance(root)

        # Check for balance factor and rotate if necessary
        if root.balance > 1:
            if key < root.left.key:
                print("case 3 not supported")
            else:
                print("case 3 not supported")

        elif root.balance < -1:
            if key > root.right.key:
                print("case 3 not supported")
            else:
                print("case 3 not supported")


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

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        # Update balance factors
        z.balance = self._get_balance(z)
        y.balance = self._get_balance(y)

        return y

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        # Update balance factors
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

    # Test Case 1: Adding a node resulting in case 1
    tree.insert(20)
    tree.insert(30)
    tree.insert(10)
    print("Test Case 1:")
    tree.print_tree()
    print()

    # Test Case 2: Adding a node resulting in case 2
    tree.insert(15)
    print("Test Case 2:")
    tree.print_tree()
    print()

    # Test Case 3: Adding a node resulting in case 3 (Not supported in this implementation)
    print("Test Case 3 (Not supported):")
    tree.insert(16)
    tree.print_tree()
    print()

    # Test Case 4: Another case 2 example
    tree.insert(25)
    print("Test Case 4:")
    tree.print_tree()
    print()
