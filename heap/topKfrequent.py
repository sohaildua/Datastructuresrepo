from typing import List
import heapq as hq
from zmq import has

def topKFrequent(nums: List[int], k: int) -> List[int]:
    hashmap = {}
    for val in nums:
        print(val)
        if val in hashmap:
            hashmap[val] +=1
        else:
            hashmap[val] = 1
    print(hashmap)
    res=[]
    for key , val in hashmap.items():
        print(key , val)
        res.append([-val, key])
        
    hq.heapify(res)
    print(res)
    data=[]
    for _ in range(k):
      i,j=  hq.heappop(res)
      data.append(j)
    
    print(data)
        

 
    
    
    



nums = [1,1,1,2,2,3]
k = 2

print(topKFrequent(nums, k))