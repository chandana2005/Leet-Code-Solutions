class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s={''.join(sorted(str(1<<i)))for i in range(31)}
        return ''.join(sorted(str(n))) in s
