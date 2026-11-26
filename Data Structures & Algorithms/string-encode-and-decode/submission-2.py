import random as ran

class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""
        delimiter = str(ord("a"))
        for s in strs:
            st+=s+delimiter
        return st

    def decode(self, s: str) -> List[str]:
        delimiter = str(ord("a"))
        strs = s.split(delimiter)
        return strs[:-1]
