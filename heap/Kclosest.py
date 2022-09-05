from typing import List
import heapq as hq

def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
        heapKclosest= []
        for x,y in points:
            print(x,y)
            distance = x**2 + y**2
            print(distance)
            heapKclosest.append([distance,x,y])
        
        print(heapKclosest)
        hq.heapify(heapKclosest)
        res=[] #result 
        while k>0:
            dist,x,y=hq.heappop(heapKclosest)
            res.append([x,y])
            k-=1
            
        print(res)

        
        
        





points = [[3,3],[5,-1],[-2,4]] 
k = 2
kClosest(points,k)