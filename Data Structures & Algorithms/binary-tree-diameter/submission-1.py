# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_dim=0

        def getHeight(root):
            if not root:
                return 0

            left_H = getHeight(root.left)
            right_H = getHeight(root.right)
            curr_dim = left_H + right_H
            self.max_dim = max(self.max_dim, curr_dim)

            return 1 + max(left_H, right_H)

        getHeight(root)
        return self.max_dim