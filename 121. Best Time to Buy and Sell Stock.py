class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # count = 0
        # for i in range(len(prices) - 1, 0, -1):
        #     for j in range(i - 1, -1, -1):
        #         if prices[i] - prices[j] > count:
        #             count = prices[i] - prices[j]
        # return count
        
        min_price = prices[0]
        max_diff = 0
        
        for price in prices[1:]:
            max_diff = max(max_diff, price - min_price)
            min_price = min(min_price, price)
        return max_diff
        
        
        

a = Solution()
print(a.maxProfit(prices = [2,4,1]))