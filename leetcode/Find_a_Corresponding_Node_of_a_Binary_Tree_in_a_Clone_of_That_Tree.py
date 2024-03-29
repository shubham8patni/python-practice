# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        lis = []
        def rec(cloned):
            if cloned == None:
                return
            if cloned.val == target.val:
                lis.append(cloned)
           
            rec(cloned.left)
            rec(cloned.right)
        
        rec(cloned)
    
        return lis[0]