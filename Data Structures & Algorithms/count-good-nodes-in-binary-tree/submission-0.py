# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def preorderTraversal(self, node, MAX):
        if not node:
            return 0

        if node.val >= MAX:
            count = 1
        else: 
            count = 0

        MAX = max(node.val, MAX)

        count += self.preorderTraversal(node.left, MAX)
        count += self.preorderTraversal(node.right, MAX)

        return count

    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        MAX = root.val
        result = self.preorderTraversal(root, MAX)
        return result
