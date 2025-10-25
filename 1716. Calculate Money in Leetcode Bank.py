class Solution:
    def totalMoney(self, n: int) -> int:
        total =0
        for i in range(n):
            week = (i//7)+1
            day= week+(i%7)
            total+=day
        return total
