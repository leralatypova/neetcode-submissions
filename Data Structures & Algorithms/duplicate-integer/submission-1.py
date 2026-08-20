class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for val in nums:
            if val in seen:
                return True
                break
            else:
                seen.add(val)
        return False