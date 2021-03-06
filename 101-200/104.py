'''
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursive Method
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        return max(leftDepth,rightDepth) + 1

# class Solution(object):
#     def maxDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         queue = [root]
#         depth = 0
#         while queue:
#             size = len(queue)
#             depth += 1
#             while size > 0:
#                 item = queue.pop(0)
#                 if item.left:
#                     queue.append(item.left)
#                 if item.right:
#                     queue.append(item.right)
#                 size -= 1
#         return depth
                


