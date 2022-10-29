class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {i: value for i,value in enumerate(nums)}
        for intgr, num in nums_dict.items():
            for i, n in nums_dict.items():
                if num + n == target and intgr != i:
                    return [intgr, i]
                