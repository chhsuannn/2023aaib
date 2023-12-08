# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root == None: return ""

        now = str(root.val)
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)
        
        if left=="" and right=="": return now
        if right=="": return now + "(" + left + ")"
        return now + "(" + left + ")(" + right + ")"