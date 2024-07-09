class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        longest_prefix = min(strs, key=len)
        for i in range(len(strs)):
            pass