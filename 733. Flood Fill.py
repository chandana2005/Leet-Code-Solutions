class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        row=len(image)
        col=len(image[0])
        old=image[sr][sc]
        if old==color:
            return image
        def dfs(sr,sc):
            if sr<0 or sc<0 or sr>=row or sc>=col or image[sr][sc]!=old:
                return image
            image[sr][sc]=color
            dir=[[0,1],[1,0],[-1,0],[0,-1]]
            for di,dj in dir:
                ni,nj=sr+di,sc+dj
                dfs(ni,nj)
        
        dfs(sr,sc)
        return image
