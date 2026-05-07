class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        k = 1

        while True:
            pref = [i[:k] for i in strs]
            if len(set(pref)) != 1:
                return strs[0][:k-1]
            
            k += 1
