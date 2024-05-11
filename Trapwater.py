class solution:
    def trap(self,height):
        water=0
        for i in range (1,len(height)):
            minheight=min(max((height[1:i]),max(height[i:len(height)])))
            if (minheight-height[i]>0):
                water+=(minheight-height[i])
        return water


