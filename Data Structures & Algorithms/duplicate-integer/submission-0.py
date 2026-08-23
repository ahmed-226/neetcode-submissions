class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # dict
        freq = {}
        for num in nums:
            if num in freq:
                return True
            else:
                freq[num]=1
        return False

        # brute force
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j]:
        #             return True
        # return False

        # sorting
        # nums.sort()
        # for i in range(1,len(nums)):
        #     if nums[i]==nums[i-1]:
        #         return True
        # return False

        # hash set
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     else:
        #         seen.add(num)
        # return False

        # hash set length
        # return len(set(nums)) < len(nums)

