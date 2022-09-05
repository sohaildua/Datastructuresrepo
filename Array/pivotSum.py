from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum_array =0
        right_sum_array = sum(nums)
        print(right_sum_array)
        
        for i,val in enumerate(nums):
            print(i, val)
            right_sum_array-=val
            if left_sum_array == right_sum_array:
                return i
            
            
            
            
        
        
        
        
        
sol = Solution()
print(sol.pivotIndex([1,7,3,6,5,6]))
        