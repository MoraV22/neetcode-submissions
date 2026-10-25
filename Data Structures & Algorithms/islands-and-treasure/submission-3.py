class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n=len(grid)
        m=len(grid[0])
        q=deque()
        visited=set()
        d=0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    q.append((i,j))
        
        while q:
            for i in range(len(q)):
                x,y= q.popleft()

                grid[x][y]=d

                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] > 0 and (nx, ny) not in visited:
                            visited.add((nx, ny))
                            q.append((nx, ny))
            d+=1

            



