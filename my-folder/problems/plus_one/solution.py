class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
        elif len(digits) > 1:
            digits = self.plusOne(digits[:-1])
            digits.append(0)
        else:
            digits = [1, 0]
        return digits