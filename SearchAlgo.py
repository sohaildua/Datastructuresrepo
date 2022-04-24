from array import array


class SearchAlgo():
    def __init__(self):
       pass
   
    def binarySearch(self,arr: array, size: int, target : int) -> int : 
       
        start = 0
        end = size - 1
        mid = int(start + (end - start)//2)
        while end>=start:
            if arr[mid]==target:
                return mid
        
            if arr[mid]>target:
            #left code 
                end = mid - 1
        
            if arr[mid]<target:
                start = mid+1
        
            mid = int(start + (end - start)//2)
    
        return -1
    
    def binarySearchWithRecursion(self,arr: array, start: int, end: int ,target)-> int :
        
        if  end>=start:
            mid = int(start + (end - start)//2)
            if arr[mid]==target:
                return mid
        
            if arr[mid]>target:
            #left code 
                self.binarySearchWithRecursion(arr,start , mid - 1 ,target)
        
            if arr[mid]<target:
                self.binarySearchWithRecursion(arr,mid+1 ,end ,target)
            
    
        return -1
        
    
val = SearchAlgo()

arr = [2, 3, 4, 10, 40]
x = 10
 
data1 = val.binarySearchWithRecursion([3,7,12,14,16,18,19,22], 0,len(arr)-1, 12)
print(data1)

