# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0)
        curr = dummyNode
        carry =  0
        l1val = 0
        l2val =0 
        while l1!=None and l2!=None or carry!=0:
            if l1:
                l1val = l1.val
            else:
                0
            if l2:
                l2val = l2.val
            else:
                0
            columnSum =l1val + l2val + carry
            carry = columnSum//10
            newNode = ListNode(columnSum%10)
            curr.next = newNode
            newNode = curr
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyNode.next
    
    
l1 = [2,4,3]
    
l2 = [5,6,4]

sol = Solution()
sol.addTwoNumbers(l1, l2)
print(sol.addTwoNumbers(l1, l2))
        
        