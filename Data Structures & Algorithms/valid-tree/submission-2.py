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
        print(self.parent)
        return self.find(p)==self.find(q)
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        uf=UF(n)
        for edge in edges:
            p,q=edge[0],edge[1]
            if uf.connected(p,q):
                return False
            else:
                uf.union(p,q)
        prev=0
        for node in range(1,n):
            prev= node-1
            if not uf.connected(prev,node):
                return False
        return True
        