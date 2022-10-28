class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        current = strs[0]
        for s in strs:
            if len(s) < len(current):
                current = current[:len(s)]
            if current != s:
                for i in range(len(current)):
                    if s[i] != current[i]:
                        current = s[:i]
                        break
        return current
        