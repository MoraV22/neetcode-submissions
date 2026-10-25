class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        area=0
        def bfs(cord):
            nonlocal area
            q=[cord]
            grid[cord[0]][cord[1]]=0
            a=0
            while q:
                x,y= q.pop(0)
                a+=1
                if x-1 >=0:
                    if grid[x-1][y]==1:
                        q.append((x-1,y))
                        grid[x-1][y]=0
                if x+1 <n:
                    if grid[x+1][y]==1:
                        q.append((x+1,y))
                        grid[x+1][y]=0
                if y-1 >= 0:
                    if grid[x][y-1]==1:
                        q.append((x,y-1))
                        grid[x][y-1]=0
                if y+1 < m:
                    if grid[x][y+1]==1:
                        q.append((x,y+1))
                        grid[x][y+1]=0
            area=max(a,area)
                 
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    continue
                else:
                    bfs((i,j))
        return area