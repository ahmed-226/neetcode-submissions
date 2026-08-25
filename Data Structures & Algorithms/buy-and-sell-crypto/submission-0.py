class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l,r pointers to 0,1 and maxprofit=0
        # while l,n and r,n where n =size of rpices
            # if [l]<=[r] : maxprofit=max(old,new)
            # else l=r and r=l+1
        # return maxprofit

        l,r =0,1
        maxProfit=0
        while prices and l<len(prices) and r<len(prices):
            if prices[l]<prices[r]:
                maxProfit=max(maxProfit,prices[r]-prices[l])
                r+=1
            else:
                l=r
                r=l+1
        return maxProfit