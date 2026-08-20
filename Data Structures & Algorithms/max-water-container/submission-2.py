class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        m = 0
        while l<r:
            h = min(heights[l], heights[r])
            area = (r-l)* h
            if h == heights[l]:
                l+=1
            else:
                r-=1
            m = max(m, area)
        return m

        