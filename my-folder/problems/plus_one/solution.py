class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 1:
            if digits[0] == 9:
                digits = [1, 0]
            else:
                digits = [digit+1 for digit in digits]
            return digits
        
        tail = digits[-1]
        if tail == 9:
            tail = 0
            digits = self.plusOne(digits[:-1])
        else:
            tail += 1
            digits = digits[:-1]
        digits.append(tail)
        return digits
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #if digits[-1] != 9:
        #    digits[-1] += 1
        #elif len(digits) > 1:
        #    digits = self.plusOne(digits[:-1])
        #    digits.append(0)
        #else:
        #    digits = [1, 0]
        #return digits