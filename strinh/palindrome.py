class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        print(s)
        b = ""
        for i in s:
            if i.isalpha():
                b+= i 
        print(b)


        if b == b[::-1]:
            return "true"
        else:
            return "false"
        
sol = Solution()
print(sol.isPalindrome("race a car"))