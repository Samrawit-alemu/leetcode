# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        nums = []
        def to_list(root):
            if not root:
                return None

            to_list(root.left)
            nums.append(root.val)
            to_list(root.right)

        to_list(root)

        def to_Tree(nums):
            mid = len(nums) // 2

            if not nums:
                return None

            root = TreeNode(nums[mid])
            root.right = to_Tree(nums[mid + 1:])
            root.left = to_Tree(nums[:mid])
                
            return root

        return to_Tree(nums)


