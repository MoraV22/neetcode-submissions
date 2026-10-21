# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        l=0

        def bfs(node):
            nonlocal l
            if not node:
                return 0
            
            ld=bfs(node.left)
            rd=bfs(node.right)
            l=max(l,ld+rd)
            return 1+ max(ld,rd)
        bfs(root)

        return l





