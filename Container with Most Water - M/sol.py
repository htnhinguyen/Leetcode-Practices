class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxVol = 0
        start = 0
        end = len(height) - 1
        while start < len(height) and end >= 0:
            vol = min(height[start], height[end]) * (end - start)
            maxVol = max(vol, maxVol)
            if height[start] < height[end]:
                start += 1
            else:
                end -=1
        return maxVol

        
