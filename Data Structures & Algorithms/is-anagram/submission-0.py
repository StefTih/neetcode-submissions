class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            for i in range(len(s)):
                letterInS = s.count(s[i])
                letterInT = t.count(s[i])
                if letterInS == letterInT:
                    continue
                else:
                    return False
            return True
        return False
                
            