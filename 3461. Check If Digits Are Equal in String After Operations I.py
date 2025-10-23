class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)>2:
            res=""      
            for i in range(1,len(s)):
                a= int(s[i-1])
                b= int(s[i])
                val= (a+b)%10
                res+= str(val)
            s=res
        return s[0]== s[-1]
