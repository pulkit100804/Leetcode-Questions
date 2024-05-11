class Solution:
    def findDuplicate(self, nums):
        n=len(nums)
        for i in range (0,n):                       ##brute force two pointer method
            for j in range (i+1,n):
                if (nums[i]==nums[j]):
                    result=nums[i]
                else:
                    pass
        return result
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:                            set approach if i isin set then it send the i back to as repeated
            if num in seen:
                return num
            seen.add(num)
"""
