class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c,c2 = {}, {}
        for i in s:
            if i in c.keys():
                c[i] += 1
            else:
                c[i] = 1

        for i in t:
            if i in c2.keys():
                c2[i] += 1
            else:
                c2[i] = 1
        if c==c2:
            return True
        return False
        