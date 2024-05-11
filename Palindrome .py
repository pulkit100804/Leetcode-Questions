class Solution:
    def isPalindrome(self, x):
        
        if x<0 or (x!=0 and x%10==0):
            return False
        
        half = 0
        while x> half:
            half=(half*10)+ (x%10)
            x=x//10
        
        return x==half or x==half//10

no=Solution(121)
print(no.isPalindrome())