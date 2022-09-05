
from typing import Optional, List
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result =collections.deque()
        if root is None:
            return result
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            currentsize = len(queue)
            currentList =  collections.deque()
            
            while currentsize > 0:
                currentNode =queue.pop()
                currentList.append(currentNode.val)
                currentsize-=1
                
                
                if currentNode.left is not None:
                    queue.appendleft(currentNode.left)
                
                if currentNode.right is not None:
                    queue.appendleft(currentNode.right)
            
            
            result.appendleft(currentList)
        return result
    
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
sol =Solution()
 
# Check if the algorithm work
print(sol.levelOrder(root))