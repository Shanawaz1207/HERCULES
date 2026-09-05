class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        mx=0
        left=0
        right=len(height)-1
        while left<right:
            wid=right-left
            h=min(height[left],height[right])
            mx=max(mx,wid*h)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return mx
        
      
        
        
            

        