class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        brack_dict = {'(': ')', '{': '}', '[': ']'}
        for i in s:
            if check != [] and i == check[-1]:
                check.pop()
            elif i in brack_dict.values():
                return False
            elif i in brack_dict:
                check += brack_dict.get(i)
        if check == []:
            return True