import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answr = np.ones(n)
        k=1
        m = 1
        for i in range (n):
            answr[i] *= k
            k *= nums[i]
        for j in range (n-1, -1, -1):
            answr[j] *= m
            m *= nums[j]

        return list(map(int, answr))

