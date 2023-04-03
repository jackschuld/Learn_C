class Solution:
    def isPalindrome(self, s: str) -> bool:
        sList = []
        for i in range(len(s)):
            if s[i].isalnum():
                sList.append(s[i].lower())
        if len(sList) % 2 != 0:
            sList.pop(len(sList) // 2)
        for i in range(len(sList)//2):
            if sList[i] != sList[-(i+1)]:
                return False
        return True
