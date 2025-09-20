class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row=len(grid)
        col=len(grid[0])
        queue=deque()
        freshor=0
        minutes=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    freshor+=1
                elif grid[i][j]==2:
                    queue.append([i,j])
        dir=[[0,-1],[0,1],[1,0],[-1,0]]
        while queue and freshor>0:
            size=len(queue)
            for i in range(size):
                x,y=queue.popleft()
                for dx,dy in dir:
                    nx=x+dx
                    ny=y+dy
                    if nx>=0 and ny>=0 and nx<row and ny<col and grid[nx][ny]==1:
                        freshor-=1
                        grid[nx][ny]=2
                        queue.append([nx,ny])
            minutes+=1
        if freshor==0:
            return minutes
        else:
            return -1
