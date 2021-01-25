#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def minimumDepthBinaryTree(root):
    if root is None:
        return 0
    if root.right is None:
        return minimumDepthBinaryTree(root.left) + 1
    if root.left is None:
        return minimumDepthBinaryTree(root.right) + 1
    
    left_dept = minimumDepthBinaryTree(root.left)
    right_dept = minimumDepthBinaryTree(root.right)
    
    return min(left_dept, right_dept) + 1
