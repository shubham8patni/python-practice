# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def trav(self,temp,ls):
        ls.append(temp.val)
        if temp.left:
            
            self.trav(temp.left,ls)
        if temp.right:
       
            self.trav(temp.right,ls)
        return ls
        
    def preorderTraversal(self, root):
        ls = []
        temp=root
        if root == None:
            return None
        if root.left==None and root.right==None:
            ls.append(root.val)
            return ls
        
        ans = self.trav(temp,ls)
        return ans