class Solution:
    def mySqrt(self, x: int) -> int:
        sq = 1
        while sq <= x:
            if sq*sq > x:
                return (sq-1)
            else:
                sq+=1
        return x
        

        #l, r = 0, x
        #while l <= r:
        #    mid = l + (r-l)//2
        #    if mid * mid <= x < (mid+1)*(mid+1):
        #        return mid
        #    elif x < mid * mid:
        #        r = mid - 1
        #    else:
        #        l = mid + 1
