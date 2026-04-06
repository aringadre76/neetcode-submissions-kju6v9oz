class Solution:
    def trap(self, height: List[int]) -> int:
        maxArea = 0
        lMax, rMax = 0, 0
        for idx, val in enumerate(height):
            if idx != 0:
                lMax = max(height[0:idx])
            rMax = max(height[idx:len(height)])
            
            minHeight = min(lMax, rMax)
            if minHeight - val > 0: maxArea += minHeight - val
        
        return maxArea