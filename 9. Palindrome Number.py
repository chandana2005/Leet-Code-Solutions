class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        if x<0 :
            return False
        og =x
        rev =0
        while x!=0:
            d=x%10
            rev=rev*10+ d
            x//=10
        if rev==og:
            return True
        else:
            return False
            '''
        num=str(x)
        rev=num[::-1]
        return rev== num


