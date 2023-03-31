class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i1, num1 in enumerate(nums):
            for i2, num2 in enumerate(nums):
                if i1 != i2 and num1 + num2 == target:
                    return [i1, i2]
