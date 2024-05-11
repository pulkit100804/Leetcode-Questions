class Solution:
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]

        # Binary search to find the leftmost occurrence of target
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if nums[left] != target:
            return [-1, -1]
        leftmost = left

        # Binary search to find the rightmost occurrence of target
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2  # Make mid biased to the right
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        rightmost = left

        return [leftmost, rightmost]
sol=Solution()
num=[1,2,2,2,5,5,4,5]
x=5
print(sol.searchRange(num,x))
