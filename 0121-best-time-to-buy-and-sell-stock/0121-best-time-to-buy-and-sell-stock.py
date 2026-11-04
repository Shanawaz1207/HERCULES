class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        bestbuy=prices[0]
        maxprofit=0
        for i in range(1,len(prices)):
            profit=prices[i]-bestbuy
            bestbuy=min(prices[i],bestbuy)
            maxprofit=max(maxprofit,profit)
        return maxprofit