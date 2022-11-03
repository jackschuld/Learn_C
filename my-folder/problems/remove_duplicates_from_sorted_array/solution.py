class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        check = 1
        while check < len(nums):
            if nums[check] == nums[check - 1]:
                nums.pop(check)
            else:
                check += 1

        return len(nums)