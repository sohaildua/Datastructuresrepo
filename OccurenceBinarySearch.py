from array import array

class OccurenceBinarySearch():
    def __init__(self):
        pass
    
    def firstOccurence(self,arr:array,size: int, key :int ) -> int :
        
        start = 0 
        end = size - 1
        mid = int(start + (end - start)//2)
        ans=-1
        while end>=start:
            
            if arr[mid] == key:
                ans = mid 
                end = mid - 1
                
            elif arr[mid] > key:
                end = mid -1 
            else:
                start = mid +1 
                
            mid = int(start + (end - start)//2)
        
        return ans 
    
    def secondOccurence(self,arr:array,size: int, key :int ) -> int :
        
        start = 0 
        end = size - 1
        mid = int(start + (end - start)//2)
        ans=-1
        while end>=start:
            
            if arr[mid] == key:
                ans = mid 
                start = mid + 1
                
            elif arr[mid] > key:
                end = mid -1 
            else:
                start = mid +1 
                
            mid = int(start + (end - start)//2)
        
        return ans
    
classObject = OccurenceBinarySearch()
arr = [1,4,5,6,8,9,11,11,11,11,11,22]
print(len(arr))
data = classObject.firstOccurence(arr,len(arr), 11)
print(data)

data1 = classObject.secondOccurence(arr,len(arr), 11)
print(data1)


print(bin(5))
import math 
print(bin(18))
print(bin(-18))
print((18& -18) +1)
print(int(math.log2(18& -18)+1))