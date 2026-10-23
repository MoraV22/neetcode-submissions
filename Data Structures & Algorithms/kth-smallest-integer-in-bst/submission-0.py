# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals=[]

        def bfs(node):
            nonlocal vals
            if not node:
                return

            vals.append(node.val)
            bfs(node.left)
            bfs(node.right)
        bfs(root)
        vals.sort()
        return vals[k-1]

