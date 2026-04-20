# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, node, orderedArr):
        if not node:
            return

        self.inorderTraversal(node.left, orderedArr)
        orderedArr.append(node.val)
        print(orderedArr)
        self.inorderTraversal(node.right, orderedArr)


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        
        orderedArr = []

        self.inorderTraversal(root, orderedArr)

        return orderedArr[k-1]


