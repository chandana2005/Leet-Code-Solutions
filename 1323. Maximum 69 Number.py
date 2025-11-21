'''
You are given a positive integer num consisting only of digits 6 and 9.
Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

Example 1:
Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.

Example 2:
Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.
'''
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
