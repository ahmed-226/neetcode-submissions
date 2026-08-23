class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # brute force ( my solution)
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if  nums[j]+nums[i]== target:
        #             return [i,j]

        # sorting
        sortedA= []
        for i, num in enumerate(nums):
            sortedA.append([num,i])
        
        sortedA.sort()
        
        i,j=0,len(nums)-1

        while i < j:
            curr = sortedA[i][0] + sortedA[j][0]
            if curr == target:
                return [min(sortedA[i][1],sortedA[j][1]),max(sortedA[i][1],sortedA[j][1])]
            elif curr > target:
                j -=1
            else:
                i+=1