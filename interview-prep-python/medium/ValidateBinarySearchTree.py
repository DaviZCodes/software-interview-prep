# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        '''
        left and right are constraints. 
        left < node.val < right

        e.g node is 3
        if we move to the left subtree, the value has to be smaller than 3, so
        we put 3 as the right constraint. left < node.val < 3
        '''
        def isValidBST_helper(node, left, right):
            if not node: #empty BST is valid
                return True
            
            if not (node.val > left and node.val < right):
                return False
            
            return isValidBST_helper(node.left, left, node.val) and             isValidBST_helper(node.right, node.val, right)
        
        return isValidBST_helper(root, float("-inf"), float("inf"))
