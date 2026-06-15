class Solution:
    def romanToInt(self, s: str) -> int:

        val = 0
        n = len(s)

        romandict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        }
        
        i = 0
        while i < n:
            if i < n-1 and romandict[s[i+1]] > romandict[s[i]]:
                val += romandict[s[i+1]] - romandict[s[i]]
                i += 2
            else:
                val += romandict[s[i]]
                i += 1

        return val
        