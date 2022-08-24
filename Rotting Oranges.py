class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time=0
        rows=len(grid)
        cols=len(grid[0])
        Que=deque()
        fresh=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    Que.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        if fresh==0:
            return time
        while Que:
            length=len(Que)
            time+=1
            directions=[(-1,0),(1,0),(0,-1),(0,1)]
            for i in range(length):
                r,c=Que.popleft()
                for nr,nc in directions:
                    nr,nc=nr+r,nc+c
                    if nr>=0 and nr<rows and nc>=0 and nc<cols:
                        if grid[nr][nc]==1:
                            grid[nr][nc]=2
                            Que.append((nr,nc))
                            fresh-=1
                if fresh==0:
                    return time;
        return -1;