class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return diameter(root)


def diameter(node):
    if node is None:
        return 0
    height_l = diameter(node.left)
    height_r = diameter(node.right)
    # balanced = balanced_l and balanced_r and abs(height_l - height_r) <=1
    height = 1 + max(height_l, height_r)
    return height


obj = Solution()
print(obj.diameterOfBinaryTree([1,2,3,4,5]))