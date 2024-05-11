class Solution:
    def binarys(target, array):
        right=len(array)-1
        left=0
        mid=0
        while left<=right:
            mid=(left+right)//2
            if(array[mid]==target):
                return mid
            elif(array[mid]>target):
                right=mid-1
            else:
                left=mid+1
        return -1