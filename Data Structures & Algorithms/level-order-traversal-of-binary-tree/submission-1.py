# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        

        def bfs(root):
            q=[[root,1]]
            res=[]
            level=1
            while q:
                node,level= q.pop(0)
                if len(res)<level:
                    res.append([])
                res[level-1].append(node.val)
                l,r= node.left,node.right
                if l:
                    q.append([l,level+1])
                if r:
                    q.append([r,level+1]) 
            return res
        if not root:
            return []
        return bfs(root)   
