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

def getPath(node, v):
    if node.info == v:
        return [node.info]
    elif v < node.info and node.left:
        return [node.info] + getPath(node.left, v)
    elif v > node.info and node.right:
        return [node.info] + getPath(node.right, v)
    else:
        raise Exception('Not found: %d' % v)

def getNode(node, v):
    if node.info == v:
        return node
    elif v < node.info and node.left:
        return getNode(node.left, v)
    elif v > node.info and node.right:
        return getNode(node.right, v)
    else:
        raise Exception('Not found: %d' % v)

def lca(root, v1, v2):
    # Enter your code here
    path1 = getPath(root, v1)
    path2 = getPath(root, v2)
    for v in reversed(path2):
        if v in path1:
            return getNode(root, v)

    return None


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print(ans.info)
