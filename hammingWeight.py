class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')

        # c = 0
        # while n:
        #     n &= n - 1
        #     c += 1
        # return c


if __name__ == '__main__':
    result = Solution().hammingWeight(010000)
    print result
