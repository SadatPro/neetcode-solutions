class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        result = 0

        charSet = set()

        for c in range(len(s)):
            while s[c] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[c])
            result = max(result, c - l + 1)
        return result
        