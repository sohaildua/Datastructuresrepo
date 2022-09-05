from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        val = dict(Counter(s))
        print(val)
        for i in val:
            print(i)
        
        
        
        
    
    
    
    
sol = Solution()
sol.minDeletions("aaabbbcc")