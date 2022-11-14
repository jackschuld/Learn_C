class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        while len(x) > 1:
            print(x)
            if x[0] != x[-1]:
                return False
            else:
                x = x[1:-1]
        return True