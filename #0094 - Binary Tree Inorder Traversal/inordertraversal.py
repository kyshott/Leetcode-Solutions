# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        endlist = []

        def traversal(root):
            if(root == None):
                return []
            traversal(root.left)
            endlist.append(root.val)
            traversal(root.right)

        traversal(root)
        return endlist
