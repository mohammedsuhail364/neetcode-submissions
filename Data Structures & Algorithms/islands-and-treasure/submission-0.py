from typing import List
from collections import deque

class Solution:
    def islandsAndTreasure(self, board: List[List[int]]) -> None:
        def bfs(row,col):
            q=deque([(row,col,0)])
            visit=set([(row,col)])
            
            while q:
                r,c,near=q.popleft()
                if board[r][c] == 0:
                    return near
                
                for nr,nc in [(r+1,c),(r-1,c),(r,c-1),(r,c+1)]:
                    if (nr>=0 and nc>=0 and nr < rows and nc < cols and board[r][c] != -1 and (nr,nc) not in visit ):
                        q.append((nr,nc,near+1))
                        visit.add((nr,nc))      
        rows=len(board)
        cols=len(board[0])
        res=[[0]*cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if board[r][c]==2147483647:
                    res[r][c]=bfs(r,c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]==2147483647:
                    board[r][c]=res[r][c]
        