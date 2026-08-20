class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        lenght = 0
        seen = {}
        for r, val in enumerate(s):
            if val in seen and seen[val]>=l:
                l = seen[val] + 1
            seen[val] = r
            lenght = max(lenght, r-l+1)
        return lenght

            