class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numDict = {}
        for num in nums:
            if num in numDict:
                numDict[num] = True
            else:
                numDict[num] = False
        for num in numDict:
            if numDict[num] == False:
                return num