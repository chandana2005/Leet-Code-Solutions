class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ms=cs=nums[0]
        for n in nums[1:]:
            cs=max(n,cs+n)
            ms=max(cs,ms)
        return ms
        
