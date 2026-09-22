class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            dif = (target - num)
            if dif in seen.keys():
                return [seen[dif], i]
            seen[num] = i