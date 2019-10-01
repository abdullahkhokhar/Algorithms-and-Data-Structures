# Given an n-ary tree, return the preorder traversal of its nodes' values.

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        final_arr = []
        if(root == None):
            return []

        final_arr.append(root.val)

        for c in root.children:
            final_arr.extend(self.preorder(c))

        return final_arr

        
