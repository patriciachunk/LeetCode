class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp = x
        temp2 = 0
        result = ""
        if str(temp)[0] == '-':
            result = result + '-'
            temp = temp * -1
        if temp == 0:
            return 0
        while temp >= 1:
            temp2 = temp % 10
            temp = temp / 10
            result = result + str(temp2)
        result = int(result)
        return result if result.bit_length() < 32 else 0

if __name__ == '__main__':
    result = Solution().reverse(1)
    print result
