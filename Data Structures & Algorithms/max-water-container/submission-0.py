class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # l,r pointers and maxarea=0
        # while l<r
        # calc at each iteraion = max(old,new)
        # if [l]<=[r] l-=1 and if [r]<[l] r+=1
        # retur  maxarea

        l,r=0, len(heights)-1
        maxArea=0
        while l<r:
            maxArea= max(maxArea,(r-l) * min(heights[r],heights[l]))
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return maxArea