class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        for k in range(n - 1, 1, -1):
            l, r = 0, k - 1
            while l < r:
                if nums[l] + nums[r] > nums[k]:
                    count += (r - l)
                    r -= 1
                else:
                    l += 1
        return count
