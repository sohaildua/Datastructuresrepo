#max heap from array


def heapify(arr, n, i):
  
  largest = i 
  leftNode = 2*i +1
  rightNode = 2*i + 2
  
  if n> leftNode and arr[leftNode] > arr[largest]:
    largest = leftNode
    
  if n> rightNode and arr[rightNode] > arr[largest]:
    largest = rightNode
    
  if largest!=i:
    arr[i],arr[largest] = arr[largest],arr[i]
    
    
    heapify(arr,n,largest)
    

def buildHeap(arr, n):
      
    # Index of last non-leaf node
    startIdx = n // 2 - 1
  
    # Perform reverse level order traversal
    # from last non-leaf node and heapify
    # each node
    for i in range(startIdx, -1, -1):
        heapify(arr, n, i)
  
  
def heapSort(arr,n):
    startIdx = n // 2 - 1
  
    # Perform reverse level order traversal
    # from last non-leaf node and heapify
    # each node
    for i in range(startIdx, -1, -1):
        heapify(arr, n, i)    
        
    for x in range(n-1 , 0 ,-1) :
          arr[0],arr[x]= arr[x],arr[0]
          heapify(arr, x, 0)
          
       

def printHeap(arr, n):
    print("Array representation of Heap is:")
  
    for i in range(n):
        print(arr[i], end=" ")
    print()
  
  


if __name__ == '__main__':
  arr = [1, 3, 5, 4, 6, 13,
           10, 9, 8, 15, 17]
  
  n = len(arr)
  
  buildHeap(arr, n)
  
  printHeap(arr, n) 
  
  heapSort(arr, n)
  
  printHeap(arr, n)