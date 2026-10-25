class UF:
    def __init__(self, grid):
        self.parent={(i,j):(i,j) for i in range(len(grid)) for j in range(len(grid[0]))}
        
    def find(self, p):
        """Find the root of the set containing p, with path compression."""
        if self.parent[p] != p:
            # Path compression: attach the node directly to the root
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        """Merge the sets containing p and q. Returns True if merged, False if already connected."""
        root_p = self.find(p)
        root_q = self.find(q)

        # They are already in the same set
        if root_p == root_q:
            return False

        self.parent[root_q] = root_p            
        return True

    def connected(self, p, q):
        """Check if p and q are in the same set."""
        return self.find(p) == self.find(q)



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n=len(grid)
        m=len(grid[0])
        islands=0
        def bfs(cord):
            q=[cord]
            while q:
                x,y= q.pop(0)
                if x-1 >=0:
                    if grid[x-1][y]=="1":
                        q.append((x-1,y))
                        grid[x-1][y]="0"
                if x+1 <n:
                    if grid[x+1][y]=="1":
                        q.append((x+1,y))
                        grid[x+1][y]="0"
                if y-1 >= 0:
                    if grid[x][y-1]=="1":
                        q.append((x,y-1))
                        grid[x][y-1]="0"
                if y+1 < m:
                    if grid[x][y+1]=="1":
                        q.append((x,y+1))
                        grid[x][y+1]="0"
                 
            



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="0":
                    continue
                else:
                    bfs((i,j))
                    islands+=1
        return islands








        