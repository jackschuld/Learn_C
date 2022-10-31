class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = None
        for i in nums:
            if i == target:
                return nums.index(i)
            elif i > target and index == None:
                index = nums.index(i)
        if index == None:
            return len(nums)
        return index