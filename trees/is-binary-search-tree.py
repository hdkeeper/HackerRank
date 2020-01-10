""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    seen = set()

    def checkSubtree(tree):
        if tree.data in seen:
            raise Exception('Duplicate found')
        seen.add(tree.data)
        treeMin = treeMax = tree.data
        if tree.left:
            leftMin, leftMax = checkSubtree(tree.left)
            if not leftMax < tree.data:
                raise Exception('Invalid ordering')
            treeMin = leftMin

        if tree.right:
            rightMin, rightMax = checkSubtree(tree.right)
            if not tree.data < rightMin:
                raise Exception('Invalid ordering')
            treeMax = rightMax
            
        return (treeMin, treeMax)

    try:
        checkSubtree(root)
        return True
    except:
        return False
