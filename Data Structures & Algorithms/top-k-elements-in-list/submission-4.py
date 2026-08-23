class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force
        # counts={}
        # for num in nums:
        #     counts[num]= counts.get(num,0) + 1

        # arr=[]
        # for num, count in counts.items():
        #     arr.append((count,num))
        # arr.sort()
        
        # res = [pair[1] for pair in arr[-k:]]
        # return res

        # bucket sort
        counts={}
        freq=[[] for i in range(len(nums)+1)]

        for num in nums:
            counts[num]= counts.get(num,0) +1
        for num,count in counts.items():
            freq[count].append(num)
        
        res=[]
        for i in range(len(freq)-1,0,-1):
            for num in freq [i]:
                res.append(num)
                if len(res) == k:
                    return res

