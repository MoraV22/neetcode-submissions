# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        ls=[]
        lr=[]

        def dfs(node,vals):
            
            if not node:
                return 
            
            vals.append(node.val)
            dfs(node.left,vals)
            dfs(node.right,vals)
        
        dfs(subRoot,ls)
        
        q=[root]
        visited=[root]
        while q:
            n=q.pop(0)
            dfs(n,lr)
            print(ls,lr)
            if ls==lr:
                return True
            lr=[]
            l,r=n.left,n.right
            if l not in visited and l:
                visited.append(l)
                q.append(l)
            if r not in visited and r:
                visited.append(r)
                q.append(r)
        return False