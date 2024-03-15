import timeit
import random


class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right
        self.height = 1

    
class BinarySearchTree:
    def insert(self, data, root=None):
        current = root
        parent = None

        while current is not None:
            parent = current
            if data <= current.data:
                current = current.left
            else:
                current = current.right

        newNode = Node(data, parent)    
        if root is None:
            root = newNode
        elif data <= parent.data:
            parent.left = newNode
        else:
            parent.right = newNode

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balenceFactor = self.getBalence(root)
        return newNode
    
    def getBalence(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def search(self, data, root):
        current = root
        while current is not None:
            if data == current.data:
                return current
            elif data <= current.data:
                current = current.left
            else:
                current = current.right
        return None
    
    def getHeight(self, root):
        if not root:
            return 0
        return root.height



# Build binary search tree
root = None
tree = BinarySearchTree()
numbers = []
for data in range(1,1000):
    numbers.append(data)

for i in range(1000):
    random.shuffle(numbers)

for i in numbers:
    root = tree.insert(i,root)


task = []
for i in range(0,1000):
    ranInt = random.randint(0,999)
    task.append(ranInt)
times = []
greatestBalanceValue = 0


for i in task:
    times.append(timeit.timeit(lambda: tree.search(i,root)))
    node = tree.search(i,root)
    balance = tree.getBalence(root)
    print("hi")
    if balance > greatestBalanceValue:
        greatestBalanceValue = balance
    
