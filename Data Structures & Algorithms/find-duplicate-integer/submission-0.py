class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_dict = dict()

        for num in nums:
            nums_dict[num] = nums_dict.get(num,0) + 1
        
        for key, value in nums_dict.items():
            if value > 1:
                return key