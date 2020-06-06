#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#
# https://leetcode.com/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (47.55%)
# Likes:    2641
# Dislikes: 167
# Total Accepted:    295.8K
# Total Submissions: 616.2K
# Testcase Example:  '[1,2,3,4,5]'
#
# 
# Given a binary tree, you need to compute the length of the diameter of the
# tree. The diameter of a binary tree is the length of the longest path between
# any two nodes in a tree. This path may or may not pass through the root.
# 
# 
# 
# Example:
# Given a binary tree 
# 
# ⁠         1
# ⁠        / \
# ⁠       2   3
# ⁠      / \     
# ⁠     4   5    
# 
# 
# 
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
# 
# 
# Note:
# The length of path between two nodes is represented by the number of edges
# between them.
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            nl = self.diameterOfBinaryTree(root.left)
            nr = self.diameterOfBinaryTree(root.right)
            ll = self.length(root.left)
            lr = self.length(root.right)
            return max(nl,max(nr,ll+lr))
    def length(self,root2:TreeNode):
        if not root2:
            return 0
        else:
            l = self.length(root2.left)+1
            r = self.length(root2.right)+1
            return max(l,r)
# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    T1 = TreeNode(1)
    T2 = TreeNode(2)
    T3 = TreeNode(3)
    T4 = TreeNode(4)
    T5 = TreeNode(5)
    T1.left = T2
    T1.right = T3
    T2.left = T4
    # T2.right = T5
    print(Test.diameterOfBinaryTree(T1))
