class Solution(object):
    def minPrice(self, prices, discounts):
        """
        :type prices: List[int]
        :type discounts: List[int]
        :rtype: float
        """
           
        prices.sort()
        discounts.sort()
        n= min(len(prices),len(discounts))
        total= 0
        for i in range(-1,-n-1,-1):
            total += prices[i] * float((100-discounts[i]))/100 # (100-discount[i])/100.00

        total += sum(prices[-len(prices):-n])
        return total