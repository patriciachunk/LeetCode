class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0, 0
        for i in nums:
            last, now = now, max(last + i, now)

        return now

if __name__ == '__main__':
    result = Solution().hammingWeight(010000)
    print result
