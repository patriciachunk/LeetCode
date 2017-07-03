class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        ht = {}
        for i in range(len(nums)):
            if nums[i] in ht:
                return [ht[nums[i]], i]
            else:
                ht[target-nums[i]] = i

if __name__ == '__main__':
    result = Solution().twoSum([1, 2, 3, 4], 3)
    print result
