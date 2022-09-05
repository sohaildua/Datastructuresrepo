import collections
 
# Code to implement a binary tree
class TreeNode: 
    def __init__(self, val):
         self.val = val
         self.left = None
         self.right = None
 
# Function for level Order Traversal
    def rightOrderTransversal(self,root):
    
        ans = []
    
        if root is None:
            return ans
       
        queue = collections.deque()
        queue.append(root)
    
        while queue:
            currentSize = len(queue)
            currentList = []
        
            while currentSize > 0:
            
                currentNode = queue.popleft()
                currentList.append(currentNode.val)
                currentSize-=1
            
                if currentNode.left is not None:
                    queue.append(currentNode.left)
                if currentNode.right is not None:
                    queue.append(currentNode.right)
                
                
            
            ans.append(currentList)
        return ans
     
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
sol =TreeNode(root)
# Check if the algorithm work
print(sol.rightOrderTransversal(root))