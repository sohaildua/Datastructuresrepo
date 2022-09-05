class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

ans_inorder =[]
ans_preorder =[]
ans_postorder =[]
def inorderTraversal(root):
    
    if root is  None:
        return
    else:
        inorderTraversal(root.left)
        ans_inorder.append(root.data)
        inorderTraversal(root.right)
    return ans_inorder

def preorderTraversal(root):
    
    if root is  None:
        return
    else:
        ans_preorder.append(root.data)
        preorderTraversal(root.left)
        preorderTraversal(root.right)
    return ans_preorder

def postorderTraversal(root):
    
    if root is  None:
        return
    else:
        postorderTraversal(root.left)
        postorderTraversal(root.right)
        ans_postorder.append(root.data)
    return ans_postorder
        
        
def maxDepthHeight(root):
    if root is None:
        return 0
    else:
        ldepth = maxDepthHeight(root.left)
        rdepth = maxDepthHeight(root.right)
        return max(ldepth,rdepth) + 1
        
        
node  = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)
node.right.right = TreeNode(6)


print(inorderTraversal(node))
print(preorderTraversal(node))
print(postorderTraversal(node))

print(maxDepthHeight(node))