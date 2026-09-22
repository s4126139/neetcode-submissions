class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k = 0
        for char_s in s:
            if char_s not in t[k:]:
                return False
            for j in range(k,len(t)):
                if char_s == t[j]:
                    k = j + 1
                    break
        return True