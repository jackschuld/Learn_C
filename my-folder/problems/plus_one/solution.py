class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # If list length is only 1
        if len(digits) <= 1:
            if 9 in digits:
                return [1, 0]
            else:
                digits = [x+1 for x in digits]
        
        # If last number is not 9, then add 1 and return
        elif digits[-1] != 9:
            digits[-1] += 1
        
        # If last number is 9, change to zero and check rest of list
        else:
            digits = self.plusOne(digits[:-1])
            digits.append(0)
            
        return digits