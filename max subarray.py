class Solution:
    def maxSubArray(self, nums):
        maxsum=nums[0]
        current=nums[0]
        for i in nums[1:]:
            current = max(i,(current+i))
            maxsum=max(maxsum,current)
        return maxsum
