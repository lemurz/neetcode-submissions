# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, node, res):
        if not node:
            return

        self.inorderTraversal(node.left, res)
        
        value = node.val
        res.append(value)

        self.inorderTraversal(node.right, res)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        self.inorderTraversal(root, res)

        for i in range(len(res)):
            if i > 0 and res[i] <= res[i-1]:
                return False
        
        return True

