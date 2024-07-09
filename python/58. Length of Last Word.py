class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        word = False
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                counter += 1
                word = True
            elif word and s[i] == ' ':
                break
        return counter