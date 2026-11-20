class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            remains = target - nums[i]
            if remains in nums[i + 1:]:
                ind = nums.index(remains, i + 1)
                return [i, ind]