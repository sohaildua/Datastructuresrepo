import math
class setBit():
    def __init__(self) -> None:
        pass
    
    def valueSet(self,val:int) -> int:
        c = -1
        if val == 0:
            return -1
        if val & (val-1) == 0 :
            c = int(math.log2(val)) +1
            return c
        return -1
    
    def valueSetter(self,val:int) -> int:
        if val < 2: return val
        c =int(math.log2(val))
        ans = c* int(math.pow(2,c-1))
        ans = ans + int(val - math.pow(2, c)) + 1
        print( int(val - math.pow(2, c)))
        return ans
    
val = setBit()
print(val.valueSetter(12))



