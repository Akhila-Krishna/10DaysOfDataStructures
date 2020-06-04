# Size of a binary tree
class Node: 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None

def size_(self, node):
  pass
  if node is None:
    return 0
  else:
    return (size_(node.left) + 1 + size_(node.right))