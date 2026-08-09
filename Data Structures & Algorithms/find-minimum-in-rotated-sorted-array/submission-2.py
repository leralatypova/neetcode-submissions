class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        else:
            l = 0 
            r = len(nums) - 1
            while l<=r:
                mid = (l+r)//2
                val = nums[mid]
                if val  < nums[0]:
                    r = mid - 1
                else:
                    l = mid + 1
        if l<=len(nums)-1:
             return nums[l]
        else:
            return nums[r]
