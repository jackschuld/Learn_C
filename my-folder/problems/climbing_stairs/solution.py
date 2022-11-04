class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 0
        curr = 1
        for i in range(n):
            curr += prev
            prev = curr - prev
        return curr
        
        
        
        
        
        
        
        
        
        
        
        #prev = 0
        #current = 1
        #for i in range(n):
        #    current += prev
        #    prev = current - prev
        #return current