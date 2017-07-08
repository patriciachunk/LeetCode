class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        minv = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] < minv:
                minv = prices[i]
            else:
                if prices[i] - minv > profit:
                    profit = prices[i] - minv

        return profit



if __name__ == '__main__':
    result = Solution().maxProfit([7, 1, 5, 3, 6, 4])
    print result
