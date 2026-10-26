class UF:
    def __init__(self, n):
        self.parent={i:i for i in range(1,n+1)}
    
    def find(self, node):
        if node != self.parent[node]:
            self.parent[node]= self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, p, q):
        pp=self.find(p)
        pq=self.find(q)
        if pp!=pq:
            self.parent[pp]= pq
    
    def connected(self, p,q):
        return self.find(p)==self.find(q)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n=len(edges)
        uf=UF(n)
        candidate=None

        for edge in edges:
            p,q = edge
            if uf.connected(p,q):
                candidate=edge
            else:
                uf.union(p,q)
        return candidate
