# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return True, 0

            left_balance, left_H = dfs(root.left)
            right_balance, right_H = dfs(root.right)

            curr_balance = left_balance and right_balance and abs(left_H - right_H) <= 1
            curr_H = 1 + max(left_H, right_H)


            return curr_balance, curr_H

        return dfs(root)[0]