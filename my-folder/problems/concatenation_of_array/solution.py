class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums.extend(nums) or nums
        #return nums[:] + nums[:]