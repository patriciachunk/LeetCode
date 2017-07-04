class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = list(set(nums))
        res = sorted(res)

        nums[:] = res
        return len(nums)

if __name__ == '__main__':
    result = Solution().removeDuplicates([1])
    print result
