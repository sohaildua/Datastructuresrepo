import heapq as heapq
from collections import Counter

def frequencySort(s: str) -> str:
    
    v = Counter(s)
    print(type(v))
    list_char = [(-val, key) for key, val in v.items()]
    print(list_char)
    
    maxHeap = []
    heapq.heapify(list_char)
    print(list_char)
    res =""
    while len(list_char) > 0:
        freq ,char = list_char[0]
        res += -freq*char
        heapq.heappop(list_char)
        
    print(res) 
        
    
    
    
    


s = "cccaaaa"
frequencySort(s)
