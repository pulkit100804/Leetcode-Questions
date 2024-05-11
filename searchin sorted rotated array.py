
def pivot(nums,target):
        n=len(nums)
        right=n-1
        left=0
        mid=0
        while left<=right:
            mid=(left+right)//2
            if (nums[mid]>=nums[0]):
                left=mid+1
            else:right=mid-1
        left1=0
        while left1<right:
            mid=(left1+right) // 2
            if (nums[left]==target):
                return left
            elif(nums[left]<target):
                left1=mid+1
            else:right=mid-1
        return -1
    
    
arr=[1,3]
target=1
print(pivot(arr,target))
