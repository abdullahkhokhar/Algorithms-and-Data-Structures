# Given an n-ary tree, return the postorder traversal of its nodes' values.

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        result=[]
        if not root:
            return []

        for child in root.children:
            result.extend(self.postorder(child))
        result.append(root.val)
        return result
