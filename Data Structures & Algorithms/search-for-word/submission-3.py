class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        f= len(word)
        n=len(board)
        m=len(board[0])
        flag=False
        if f>n*m:
            return flag
        def bfs(cord, curr, prev):
            nonlocal flag
            if curr==f:
                flag=True
                return
            
            x,y=cord

            if x-1>=0:
                if board[x-1][y]==word[curr] and (x-1,y)!=prev:
                    bfs((x-1,y),curr+1,(x,y))
            if x+1<n:
                if board[x+1][y]==word[curr] and (x+1,y)!=prev:
                    bfs((x+1,y),curr+1,(x,y))
            if y-1 >= 0:
                if board[x][y-1]==word[curr] and (x,y-1)!=prev:
                    bfs((x,y-1),curr+1,(x,y))
            if y+1 < m:
                if board[x][y+1]==word[curr] and (x,y+1)!=prev:
                    bfs((x,y+1),curr+1,(x,y))

        for i in range(n):
            for j in range(m):
                
                if board[i][j]==word[0]:
                    bfs((i,j),1,(-1,-1))
        return flag
