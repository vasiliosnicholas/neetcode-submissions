class Solution:
    def calculateArea(self, heights:List[int], left:int, right:int) -> int:
        width = right - left
        height = min(heights[left], heights[right])
        return height * width

    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        #start out with max container width, unknown height
        area = self.calculateArea(heights, left, right)
        while left < right:
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            area = max(area, self.calculateArea(heights, left, right))
        return area