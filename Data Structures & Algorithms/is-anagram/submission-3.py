class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]] = 1
            else:
                count[s[i]] += 1

        for j in range(len(t)):
            if t[j] not in count:
                return False
            else: 
                count[t[j]] -= 1
        for k in count.keys():
            if count[k] != 0:
                return False
        return True