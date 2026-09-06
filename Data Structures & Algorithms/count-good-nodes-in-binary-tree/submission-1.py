# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,max_so_far):
            if not node:
                return 0

            curr_count = 1 if node.val >= max_so_far else 0
            max_so_far = max(node.val,max_so_far)

            left_count = dfs(node.left,max_so_far)
            right_count = dfs(node.right,max_so_far)

            return curr_count + left_count + right_count

        return dfs(root,root.val)
