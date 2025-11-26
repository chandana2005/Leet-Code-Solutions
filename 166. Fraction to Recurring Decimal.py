'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses
If multiple answers are possible, return any of them.
It is guaranteed that the length of the answer string is less than 104 for all the given inputs.
Note that if the fraction can be represented as a finite length string, you must return it.

Example 1:
Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:
Input: numerator = 2, denominator = 1
Output: "2"
'''
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
