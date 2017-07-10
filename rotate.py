class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        nums[:] = nums[length-k:]+nums[:length-k]



if __name__ == '__main__':
    result = Solution().twoSum([2, 7, 11, 15], 9)
    print result
