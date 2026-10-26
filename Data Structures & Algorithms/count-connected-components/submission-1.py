class UF:
    def __init__(self, n):
        self.parent={i:i for i in range(n)}
    
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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf=UF(n)

        for edge in edges:
            p,q = edge
            uf.union(p,q)
        
        for node in range(n):
            uf.find(node)
        

        return len(set(uf.parent.values()))