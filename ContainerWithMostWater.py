class Solution:
    def maxArea(self, heights: List[int]) -> int:
    

        i = 0
        j = len(heights) - 1

        l = heights[i]
        r = heights[j]

        maxAreas = (j - i) * min(l, r)
        while i < j:
            l = heights[i]
            r = heights[j]
            currentArea = (j - i) * min(l, r)
 
            if maxAreas < currentArea:
                maxAreas = currentArea
            
            if l <= r:
                i+=1
            elif r < l:
                j-=1
      

        
        return maxAreas