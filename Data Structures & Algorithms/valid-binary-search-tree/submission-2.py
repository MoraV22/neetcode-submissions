# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def bfs(node, minn,maxx):
            if not node:
                return True
            valid=True 
            if node.left:
                valid= valid and (node.left.val< node.val) and (node.left.val > minn)
            if node.right:
                valid= valid and (node.right.val > node.val) and (node.right.val < maxx)
            return valid and bfs(node.left, minn, node.val) and bfs(node.right, node.val, maxx)
        return bfs(root, float("-inf"), float("inf"))
