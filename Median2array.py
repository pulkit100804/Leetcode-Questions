class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums3=nums1+nums2
        nums3.sort()
        n=len(nums3)
        if n%2==1:
            return nums3[n//2]
        else:
            m1=nums3[n//2 -1]
            m2=nums3[n//2]
            return (float(m1)+float(m2))/2
