class Solution:
    def romanToInt(self, s: str) -> int:
        # Variables
        output = 0
        next_index = 0
        nums_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        values = [nums_dict.get(i) for i in s]

        for value in values:
            next_index += 1
            try:
                if value < values[next_index]:
                    output -= value
                else:
                    output += value
            except IndexError:
                output += value
        return output
    
test = Solution()
            