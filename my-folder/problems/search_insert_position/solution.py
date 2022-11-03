class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for num in nums:
            if num >= target:
                return nums.index(num)
        return len(nums)