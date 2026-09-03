# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def get_height(node):
            if not node or not self.balanced:
                return 0

            left_h = get_height(node.left)
            right_h = get_height(node.right)

            if abs(left_h - right_h) > 1:
                self.balanced = False

            return 1 + max(left_h, right_h)

        get_height(root)
        return self.balanced