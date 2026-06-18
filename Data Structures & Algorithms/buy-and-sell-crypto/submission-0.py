class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxVal=0
        i=0
        j=1
        while j<len(prices):
            if prices[j]-prices[i]>0:
                maxVal=max(maxVal,prices[j]-prices[i])
               
                j+=1
            else:
                i=j
                j+=1
        return maxVal