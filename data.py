from array import array 

class Solution:
    def singleNumber(self, nums:array):
        # Code here
        s=0
        first =0
        second = 0
        for i in range(0,len(nums)):
            s=s^nums[i]
        
        x = s & -s
       
        for i in range(0, len(nums)):
            
            if(nums[i] & x == 0):
                
                first = first ^ nums[i]
            else:
                
                second = second ^ nums[i]
                
        return sorted((first, second))
        
val = Solution()
d= val.singleNumber([7 ,6,25,4,25,15,15,7,4,3,29,6])
print(d)

print(25&2 )
print(bin(25))
print(bin(6))