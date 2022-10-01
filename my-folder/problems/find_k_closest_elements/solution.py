class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
      
        # Base cases
        if len(arr) == k:
            return arr
        
        if x < arr[0]:
            return arr[:k]
        elif x > arr[-1]:
            return arr[-k:]
        
        distances = [abs(x - n) for n in arr]
        Z = [a for _,a in sorted(zip(distances,arr))]
        return sorted(Z[:k])
           
            
        

            