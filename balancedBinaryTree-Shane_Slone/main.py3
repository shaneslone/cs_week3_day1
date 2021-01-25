#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def balancedBinaryTree(root):
    def max_depth(root):
        if root is None:
            return 0
        left_depth = max_depth(root.left)
        right_depth = max_depth(root.right)
        
        return max(left_depth, right_depth) + 1
        
    if root is None: # A None node is balanced
        return True
    height_diff = abs(max_depth(root.left) - max_depth(root.right)) #find the difference between the left and right subtree
    
    left_tree = False
    right_tree = False
    
    if height_diff < 2: # If root is balanced, check to see if the left and right subtrees are also blanced
        left_tree = balancedBinaryTree(root.left)
        right_tree = balancedBinaryTree(root.right)
    else:
        return False
    return left_tree and right_tree # Returns true if both subtrees of the node are balanced


