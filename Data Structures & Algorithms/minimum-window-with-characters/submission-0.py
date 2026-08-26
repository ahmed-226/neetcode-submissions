from collections import Counter


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(s) < len(t):
            return ""

        target_counts = Counter(t)
        window_counts = {}

        have, need = 0, len(target_counts)
        res, res_len = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1

            # check if i got the target freq of the char 
            if char in target_counts and window_counts[char] == target_counts[char]:
                have += 1

            # if my window have all i need it might have unessary and need to check the sortest substr
            while have == need:
                # if I have all i need but with shorter length than previous one
                if (r - l + 1) < res_len:
                    # update the substr
                    res = [l, r]
                    # shrink the shortest length
                    res_len = r - l + 1

                # remove the items in left till I violated target frequency
                window_counts[s[l]] -= 1
                if (
                    s[l] in target_counts
                    and window_counts[s[l]] < target_counts[s[l]]
                ):
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if res_len != float("inf") else ""