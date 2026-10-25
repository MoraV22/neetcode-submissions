class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        q=deque()
        time=0
        fresh=0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        if not q:
            if fresh>0:
                return -1
            else:
                return 0 
        while q:
            for i in range(len(q)):
                x,y= q.popleft()
                print(x,y,"rot")
                print(time,"time")

                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    
                    if 0 <= nx < n and 0 <= ny < m:
                        if grid[nx][ny]!=1:
                            continue
                        print(nx,ny,"rotting")
                        grid[nx][ny]=2
                        q.append((nx, ny))
                        fresh-=1
            time+=1
        return time-1 if fresh==0 else -1
        
            