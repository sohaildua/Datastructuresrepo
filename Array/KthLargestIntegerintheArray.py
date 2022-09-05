from typing import List

def containsDuplicate( nums: List[int]) -> bool:
        
        map ={}
        for x in nums:
            if x in map:
                map[x] +=1
            else:
                map[x] =1
            
            
        for item,value in map.items():
            if value>1:
                return "false"
        return "true"


print(containsDuplicate([1,2,3,4]))