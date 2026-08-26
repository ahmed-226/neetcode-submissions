class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted_s1 = sorted(s1)
        n1, n2 = len(s1), len(s2)

        for l in range(n2 - n1 + 1):
            if sorted_s1 == sorted(s2[l : l + n1]):
                return True

        return False