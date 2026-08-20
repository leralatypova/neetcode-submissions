class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numms = set(nums)
        max_l = 0
        for i in range(len(nums)):
            if nums[i]-1 in numms:
                continue
            else:
                l = 0
                while nums[i]+l in numms:
                    l += 1
                    max_l = max(max_l, l)
        return max_l
