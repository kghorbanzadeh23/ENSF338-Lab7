import timeit
import random
import matplotlib.pyplot as plt



class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def balance(self):
        return self._balance(self.root)

    def _balance(self, node):
        if node is None:
            return 0
        return abs(self._height(node.left) - self._height(node.right))

    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))


# Build binary search tree
tree = BinarySearchTree()
numbers = []
for data in range(0,1000):
    numbers.append(data)

for i in range(1000):
    random.shuffle(numbers)

for i in numbers:
    tree.insert(i)


task = []
for i in range(0,1000):
    task.append(i)
    random.shuffle(task)
times = []
balanceValues = []

for i in task:
    times.append(timeit.timeit(lambda: tree.search(i),number=1))
    node = tree.search(i)
    balance = tree._balance(node)
    balanceValues.append(balance)
    
max = max(balanceValues)
print(max)

# Plotting the distribution of times
plt.scatter(balanceValues, times)
plt.xlabel('Balance')
plt.ylabel('Search Time')
plt.title('Comparison between Balance and Time')
plt.savefig('ex1.jpeg')
