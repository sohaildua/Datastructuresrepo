from array import array


class pivotArray():
    def __init__(self):
        pass
    
    
    def findPivot(self,arr:array,size:int)-> int:
        start = 0
        end = size - 1
        mid = int(start + (end - start)/2)
        
        while end>start:
            if arr[mid]>=arr[0]:
                start = mid + 1
            else:
                end = mid
            mid =int( start + (end - start)/2)
        
        return start
    def binarySearch(self,arr: array, start:int, end:int,size: int, target : int) -> int : 
       
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
    
    def findPivotValue(self,arr:array,size: int ,target:int)-> int:
        
        pivot = self.findPivot(arr,size)
        if target>arr[pivot] and target<=arr[size-1]:
            return self.binarySearch(arr,pivot,size-1,len(arr),target)
        else:
            return self.binarySearch(arr,0,pivot-1,len(arr),target)
    
valueObj = pivotArray()
print(valueObj.findPivotValue([8,10,17,1,3],5,17))

    



    
