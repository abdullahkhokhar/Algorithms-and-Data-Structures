# A binary tree is univalued if every node in the tree has the same value.
# Return true if and only if the given tree is univalued.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if(root == None):
            return True
        master_value = root.val
        if(root.left != None and (root.left.val != master_value)):
            return False
        if(root.right != None and (root.right.val != master_value)):
            return False

        left_child = self.isUnivalTree(root.left)
        right_child = self.isUnivalTree(root.right)
        return left_child and right_child

        
