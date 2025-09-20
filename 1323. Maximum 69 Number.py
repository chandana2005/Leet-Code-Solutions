class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        numstr=str(num)
        maxn= num
        for i,ch in enumerate(numstr):
            if ch=='6':
                cand=numstr[:i]+'9'+numstr[i+1:]
            else:
                cand=numstr[:i]+'6'+numstr[i+1:]
            candval=int(cand)
            if candval>maxn:
                maxn=candval
        return maxn
