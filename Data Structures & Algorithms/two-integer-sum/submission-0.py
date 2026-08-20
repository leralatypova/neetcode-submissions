class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, val in enumerate(nums):
            cur = target - val
            if cur in seen.keys():
                return [seen[cur], idx]
                break
            seen[val] = idx
        