class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        start=0
        currs=0
        minl=float('inf')
        for end in range(n):
            currs+=nums[end]
            while currs>=target:
                minl=min(minl, end-start+1)
                currs-=nums[start]
                start+=1
        return 0 if minl==float('inf') else minl
