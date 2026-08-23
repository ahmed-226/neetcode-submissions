class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force
        counts={}
        for num in nums:
            counts[num]= counts.get(num,0) + 1

        arr=[]
        for num, count in counts.items():
            arr.append((count,num))
        arr.sort()
        
        res = [pair[1] for pair in arr[-k:]]
        return res

