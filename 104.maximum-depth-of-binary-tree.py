#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (65.04%)
# Likes:    2336
# Dislikes: 69
# Total Accepted:    788.4K
# Total Submissions: 1.2M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given binary tree [3,9,20,null,null,15,7],
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# return its depth = 3.
# 
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            if root.left == None and root.right == None:
                return 1
            else:
                left_length = 0
                right_length = 0
                if root.left:
                    left_length = self.maxDepth(root.left)
                if root.right:
                    right_length = self.maxDepth(root.right)
                return max(left_length,right_length)+1
        else:
            return 0
# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    T1 = TreeNode(3)
    T2 = TreeNode(9)
    T3 = TreeNode(20)
    T4 = TreeNode(15)
    T5 = TreeNode(7)
    T6 = TreeNode(10)
    T1.left = T2
    T1.right = T3
    T3.left = T4
    T3.right = T5
    T5.right = T6
    print(Test.maxDepth(T1))
