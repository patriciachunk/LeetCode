class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, element in enumerate(numbers):
            if target-element is in dic:
                return (dic[target-element]+1, i+1)
            dic[element] = i

if __name__ == '__main__':
    result = Solution().twoSum([2, 7, 11, 15], 9)
    print result
