class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for i in strs:
            k = "".join(sorted(i))
            if k not in result:
                result[k] = []
            result[k].append(i)
        return list(result.values())