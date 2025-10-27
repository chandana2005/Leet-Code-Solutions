class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n= len(nums)
        all_nums= set(range(1,n+1))
        return list(all_nums - set(nums))
