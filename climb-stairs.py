class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return n

        s1 = 0
        s2 = 1
        result = 0
        while n > 0:
            result = s1 + s2
            s1 = s2
            s2 = result
            n -= 1
        return result

if __name__ == '__main__':
    result = Solution().climbStairs(3)
    print result
