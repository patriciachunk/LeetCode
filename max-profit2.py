class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if len(prices) == 0:
            return 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                profit = profit + (prices[i+1]-prices[i])
        return profit



if __name__ == '__main__':
    result = Solution().maxProfit([2, 1, 2, 0, 1])
    print result
