class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        c = {}

        for ch in s:
            if ch not in c:
                c[ch] = 1
            else:
                c[ch] += 1

        for ch in t:
            if ch not in c:
                return False
            c[ch] -= 1
            if c[ch] < 0:
                return False

        return True