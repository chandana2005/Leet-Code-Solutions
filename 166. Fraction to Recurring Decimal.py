class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator ==0:
            return "0"
        res=[]
        if (numerator<0) ^ (denominator<0):
            res.append("-")
        num, den= abs(numerator), abs(denominator)
        res.append(str(num//den))
        rem= num%den
        if rem==0:
            return ''.join(res)
        res.append('.')
        seen={}
        while rem!=0:
            if rem in seen:
                indx=seen[rem]
                res.insert(indx,'(')
                res.append(')')
                break
            seen[rem]=len(res)
            rem *=10
            dig= rem//den
            res.append(str(dig))
            rem%=den
        return ''.join(res)
