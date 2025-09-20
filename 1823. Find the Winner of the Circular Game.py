class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        q=deque()
        for i in range(1,n+1):
            q.append(i)

        while len(q)!=1:
            for i in range(1,k+1):
                d= q.popleft()
                if i!=k:
                    q.append(d)
        winner=q[-1]
        return winner
