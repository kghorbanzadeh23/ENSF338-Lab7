import timeit
import random
import matplotlib.pyplot as plt



class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right
        self.height = 1
        self.balance = 0

    
class BinarySearchTree:
    def insert(self, data, root=None):
        current = root
        parent = None

        while current is not None:
            parent = current
            if data <= current.data:
                current.balance = current.balance - 1
                current = current.left
                
            else:
                current.balance += 1
                current = current.right


        newNode = Node(data, parent)
        if root is None:
            root = newNode
            return newNode
        elif data <= parent.data:
            parent.left = newNode
        else:
            parent.right = newNode

        balenceFactor = self.getBalance(root)
    
    def getBalance(self, root):
        return root.balance

    def search(self, data, root):
        current = root
        while current is not None:
            if data == current.data:
                return current
            elif data <= current.data:
                current = current.left
            else:
                current = current.right
        return current
    
    def getHeight(self, root):
        if not root:
            return 0
        return root.height



# Build binary search tree
tree = BinarySearchTree()
numbers = []
for data in range(0,1000):
    numbers.append(data)

for i in range(1000):
    random.shuffle(numbers)
rand = random.randint(0,999)
root = Node(rand)
numbers.remove(rand)
for i in numbers:
    tree.insert(i,root)


task = []
for i in range(0,1000):
    ranInt = random.randint(0,999)
    task.append(ranInt)
times = []
balanceValues = []

for i in task:
    times.append(timeit.timeit(lambda: tree.search(i,root),number=1))
    node = tree.search(i,root)
    balance = tree.getBalance(node)
    balanceValues.append(balance)
    
max = max(balanceValues)


# Plotting the distribution of times
plt.scatter(balanceValues, times)
plt.xlabel('Balance')
plt.ylabel('Search Time')
plt.title('Comparison between Balance and Time')
plt.savefig('ex1.jpeg')
