from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return [[]]
        
        result = []
        for i in range(1,numRows+1):
            row = []
            for j in range(0,i):
                if j == 0 or j == i-1:
                    row.append(1) 
                else:
                    
                    row.append(result[i-2][j-1] + result[i-2][j])
                    
            result.append(row) 
                 
            print(result)   
        return result 
            
            
    


Sol = Solution()
Sol.generate(5)