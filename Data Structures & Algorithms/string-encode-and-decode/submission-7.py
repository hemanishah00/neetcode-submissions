class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes= ",".join([str(len(s)) for s in strs])
        return "#".join(["".join(strs),sizes])
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes = [int(n) for n in s.split("#")[-1].split(",")]
        ptr = 0
        res = []
        for si in sizes:
            res.append(s[ptr:ptr+si])
            ptr+=si
        return res