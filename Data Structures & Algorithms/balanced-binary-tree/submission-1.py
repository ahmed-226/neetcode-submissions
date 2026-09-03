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
                return 0

            l_H = dfs(root.left)
            if l_H == -1:
                return -1

            r_H = dfs(root.right)

            if r_H == -1:
                return -1

            if abs(l_H - r_H) > 1:
                return -1
            
            return 1 + max(l_H,r_H)

        return dfs(root) != -1
        