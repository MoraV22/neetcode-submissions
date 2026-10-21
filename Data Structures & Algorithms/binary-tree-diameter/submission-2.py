# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.l=0

        def bfs(node):
            if not node:
                return 0
            
            ld=bfs(node.left)
            rd=bfs(node.right)
            self.l=max(self.l,ld+rd)
            return 1+ max(ld,rd)
        bfs(root)

        return self.l





