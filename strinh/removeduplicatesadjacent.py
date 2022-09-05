class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return "false"
        
        val = s + s
        if goal in val:
            return "true"
        else:
            return "false"
        

sol = Solution()
print(sol.rotateString("abcde","abced"))