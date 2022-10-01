# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        begin = 1
        
        while begin <= n:
            middle = (begin + n)//2
            pick = guess(middle)

            if pick == 0:
                return middle
            elif pick == 1:
                begin = middle+1
            else:
                n = middle-1
        

        
