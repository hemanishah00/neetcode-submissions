class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        c_s, c_t = {}, {}
        for i in range(len(s)):
            if s[i] not in c_s.keys():
                c_s[s[i]] = 1
            else:
                c_s[s[i]] += 1
            
            if t[i] not in c_t.keys():
                c_t[t[i]] = 1
            else:
                c_t[t[i]] += 1
        if c_s != c_t:
            return False
        return True
        