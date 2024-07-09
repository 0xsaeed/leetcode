class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        prev = 0
        for i in range(len(s) - 1, -1, -1):
            curr = roman_dict[s[i]]
            if curr < prev:
                total -= curr
            else:
                total += curr
            prev = curr
        return total