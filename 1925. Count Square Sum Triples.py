#using sqrt 
class Solution:
    def countTriples(self, n: int) -> int:
        count =0
        for a in range(1, n+1):
            for b in range(1, n+1):
                c_squared= a*a+b*b
                c= int(sqrt(c_squared))

                if c*c == c_squared and c<=n :
                    count+=1
        return count

#using set
class Solution:
    def countTriples(self, n: int) -> int:
        count =0
        square = set([i**2 for i in range(1, n+1)])
        for a in range(1, n+1):
            for b in range(1, n+1):
                c= a*a+b*b

                if c in square:
                    count+=1
        return count
