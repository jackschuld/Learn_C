class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        columnLetters = ""
        while columnNumber > 0:
            columnNumber -= 1
            columnLetters += chr((columnNumber % 26) + 65)
            columnNumber //= 26
        return columnLetters[::-1]
    