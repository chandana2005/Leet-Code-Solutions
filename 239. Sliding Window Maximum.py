class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        dq=deque()
        for right in range(len(nums)):
            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()
            dq.append(right)
            if dq:
                if dq[0]<=right-k:
                    dq.popleft()
            if right>= k-1:
                res.append(nums[dq[0]])
        return res
