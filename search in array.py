class Solution:
    def search(self, nums, target):
        for i in nums:
            if nums[i]==target:
                return i
            else:
                return -1
            