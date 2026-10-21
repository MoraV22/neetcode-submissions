# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        balanced=True

        def bfs(node):
            nonlocal balanced
            if not node:
                return 0
            
            left= bfs(node.left)
            right=bfs(node.right)
            balanced = balanced and (abs(left-right)<=1)
            return 1 + max(left,right)

        bfs(root)

        return balanced