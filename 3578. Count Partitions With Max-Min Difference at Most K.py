import collections
class Solution(object):
    def countPartitions(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9+7
        dq1 = collections.deque()
        dq2 = collections.deque()
        dp = [0]*(len(nums)+1)
        dp[0] = 1
        suffix = left = 0
        for right in xrange(len(nums)):
            suffix = (suffix+dp[right])%MOD
            while dq1 and nums[dq1[-1]] >= nums[right]:
                dq1.pop()
            while dq2 and nums[dq2[-1]] <= nums[right]:
                dq2.pop()
            dq1.append(right)
            dq2.append(right)
            while nums[dq2[0]]-nums[dq1[0]] > k:
                if left == dq1[0]:
                    dq1.popleft()
                if left == dq2[0]:
                    dq2.popleft()
                suffix = (suffix-dp[left])%MOD
                left += 1
            dp[right+1] = suffix
        return dp[-1]
