class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max = 0
        while l != r:
            if heights[l] > heights[r]:
                lower = heights[r]
            else:
                lower = heights[l]
            current = (r - l) * lower
            if current > max:
                max = current
            if heights[l] > heights[r]:
                r -= 1
            elif heights[r] >= heights[l]:
                l += 1
        return max
