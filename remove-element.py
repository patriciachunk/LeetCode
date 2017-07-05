class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :rtype: int
        """
        position = 0
        for num in nums:
            if num != val:
                nums[position] = num
                position = position + 1
        return position

if __name__ == '__main__':
    result = Solution().removeElement([1, 1, 2, 3, 2], 2)
    print result
