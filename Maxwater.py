class Solution:
    def maxArea(self, height):
        right = len(height)-1
        left=0
        maxarea=0
        while left<right:
            current=min(height[left],height[right])*(right-left)
            maxarea=max(current,maxarea)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxarea
        
