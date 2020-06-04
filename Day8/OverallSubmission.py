INT_MAX = 4294967296
INT_MIN = -4294967296

class Node: 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
        
def is_bst_satisfied(self):
    pass
    x = is_bst(self.node, INT_MAX, INT_MIN)
    return x

def is_bst(self, node, maxi, mini):
    if self.node is None:
        return True
    if self.node.left<mini or self.node.right>maxi:
        return False
    return (is_bst(node.left, mini, node.data -1) and is_bst(node.right, node.data+1, maxi))

