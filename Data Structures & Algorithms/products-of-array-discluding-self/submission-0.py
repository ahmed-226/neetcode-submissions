class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[1]*len(nums)
        post=[1]*len(nums)

        curr=1
        for i in range(len(nums)):
            pre[i]=curr
            curr *=nums[i]

        curr=1
        for i in range(len(nums)-1,-1,-1):
            post[i]=curr
            curr *=nums[i]

        res=[]
        for i in range(len(nums)):
            res.append(pre[i]*post[i])
        return res