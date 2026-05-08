class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix_length = 1

        while True:
            current_prefixes = [word[:prefix_length] for word in strs]

            if len(set(current_prefixes)) != 1:
                return strs[0][:prefix_length - 1]

            if prefix_length >= min(len(word) for word in strs):
                return strs[0][:prefix_length]

            prefix_length += 1
