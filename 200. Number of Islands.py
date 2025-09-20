class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        row=len(grid)
        col=len(grid[0])
        def dfs(i,j):
            if i<0 or j<0 or i>=row or j>= col or grid[i][j]=='0':
                return 
            grid[i][j]='0'
            dir=[[0,1],[1,0],[-1,0],[0,-1]]
            for di,dj in dir:
                ni,nj=i+di, j+dj
                dfs(ni,nj)

        count=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1':
                    dfs(i,j)
                    count+=1
        return count
