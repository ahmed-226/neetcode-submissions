class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict={}
        tdict={}
        for item in s:
            sdict[item]= sdict.get(item,0)+1
        for item in t:
            tdict[item]=tdict.get(item,0)+1
        return sdict==tdict
        
        