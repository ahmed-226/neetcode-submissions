class Solution:
    def isPalindrome(self, s: str) -> bool:
        # tow pointers
        # l, r = 0, len(s) - 1
        # s = s.upper()
        # while l < r:
        #     while l < r and not s[l].isalnum():
        #         l += 1
        #     while l < r and not s[r].isalnum():
        #         r -= 1
        #     if s[l] != s[r]:
        #         return False
        #     l += 1
        #     r -= 1
        # return True

        # reverse string
        new_str=""
        for c in s:
            if c.isalnum():
                new_str+=c.lower()
        return new_str==new_str[::-1]