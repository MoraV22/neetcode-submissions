# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        longest=[1]

        def bfs(node, curr_d):
            if node is None:
                return
            else:
                longest[0]=max(longest[0],curr_d)

                bfs(node.left,curr_d+1)
                bfs(node.right,curr_d+1)
        bfs(root,1)

        return longest[0]

        