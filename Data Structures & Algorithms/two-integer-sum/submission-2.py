class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            dif = (target - num)
            if dif in nums[i + 1:]:
                return [i, nums.index(dif, i + 1)]