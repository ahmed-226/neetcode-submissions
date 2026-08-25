class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # brute force ( limit exceeded )
        # res=0
        # for i in range(len(s)):
        #     count,maxf={},0
        #     for j in range(i,len(s)):
        #         count[s[j]]=1+count.get(s[j],0)
        #         maxf= max(maxf,count[s[j]])
        #         if ( j-i + 1) - maxf <= k:
        #             res = max(res, j-i+1)
        # return res

        # sliding window
        # idea behind it is to calc the freq of the target char at eah iteration, and calc if current length - this freq = k which ask about the char that is not our target, if so start move l boundry till this optmial length even if we lose same char the k replacement will solve it, then update the final length because it might be the old one or the current actual length we got
        res = 0
        charSet = set(s)

        for c in charSet:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    # this mean c is a new index with same char we work ( freq of our number in the acutal length
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1

                res = max(res, r - l + 1)
        return res