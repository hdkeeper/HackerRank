class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 


class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
    # Enter your code here
    def addParent(node):
        if node.left:
            node.left.parent = node
            addParent(node.left)
        if node.right:
            node.right.parent = node
            addParent(node.right)

    def findNode(node, v):
        if node.info == v:
            return node
        elif v < node.info and node.left:
            return findNode(node.left, v)
        elif v > node.info and node.right:
            return findNode(node.right, v)
        else:
            raise Exception('Not found: %d' % v)

    def traceUp(node, process):
        process(node)
        if node.parent:
            traceUp(node.parent, process)        

    root.parent = None
    addParent(root)
    path = []
    resultNode = None

    def buildPath(node):
        path.append(node.info)

    def checkPath(node):
        nonlocal resultNode
        if node.info in path and resultNode is None:
            resultNode = node

    traceUp(findNode(root, v1), buildPath)
    traceUp(findNode(root, v2), checkPath)

    return resultNode



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print(ans.info)
