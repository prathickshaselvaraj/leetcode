# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # stack = []
        # curr = root
        # prev = None

        # while stack or curr:
            
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left

        #     curr = stack.pop()
        #     if prev is not None and curr.val <= prev:
        #         return False

        #     prev = curr.val
        #     curr = curr.right

        # return True

        result=[]

        def inorder(node):
            if node==None:
                return 
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        inorder(root)

        if len(set(result)) != len(result):
            return False

        if result == sorted(result):
            return True
        else:
            return False