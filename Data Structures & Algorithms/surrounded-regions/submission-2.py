class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        n,m = len(board), len(board[0])
        def bfs(cord):

            q=[cord]

            while q:
                x,y = q.pop(0)
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if (nx <0 or nx >=n) or (ny <0 or ny>=m):
                        continue
        
                    if board[nx][ny]=="O":
                        q.append((nx, ny))
                        board[nx][ny]="V"

            

        for i in range(n):
            if board[i][0]=="O":
                board[i][0]="V"
                bfs((i,0))
            if board[i][m-1]=="O":
                board[i][m-1]="V"
                bfs((i,m-1))
            
        for i in range(m):
            if board[0][i]=="O":
                board[0][i]="V"
                bfs((0,i))
            if board[n-1][i]=="O":
                board[n-1][i]="V"
                bfs((n-1,i))
        for i in range(n):
            for j in range(m):
                if board[i][j]=="O":
                    board[i][j]="X"
                if board[i][j]=="V":
                    board[i][j]="O"

            