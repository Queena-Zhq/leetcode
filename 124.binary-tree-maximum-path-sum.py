#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (33.69%)
# Likes:    3588
# Dislikes: 287
# Total Accepted:    364.9K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty binary tree, find the maximum path sum.
# 
# For this problem, a path is defined as any sequence of nodes from some
# starting node to any node in the tree along the parent-child connections. The
# path must contain at least one node and does not need to go through the
# root.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# Output: 6
# 
# 
# Example 2:
# 
# 
# Input: [-10,9,20,null,null,15,7]
# 
# -10
# / \
# 9  20
# /  \
# 15   7
# 
# Output: 42
# 
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
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_path = -10000
        self.maxPath(root)
        return self.max_path
    def maxPath(self,root:TreeNode) ->int:
        if root:
            if root.right and root.left:
                left_max = self.maxPath(root.left)
                right_max = self.maxPath(root.right)
                self.max_path = max(self.max_path,left_max+right_max+root.val,root.val,left_max+root.val,right_max+root.val)

                return max(root.val,max(left_max,right_max)+root.val)
            elif root.left and root.right == None:
                left_max = self.maxPath(root.left)
                self.max_path = max(self.max_path,left_max+root.val,root.val)
                return max(left_max+root.val,root.val)
            elif root.right and root.left == None:
                right_max = self.maxPath(root.right)
                self.max_path = max(self.max_path,right_max+root.val,root.val)
                return max(right_max+root.val,root.val)
            else: 
                self.max_path = max(self.max_path,root.val)
                return root.val
        else: return 0

# @lc code=end
if __name__ == "__main__":
    test = Solution()
    T1 = TreeNode(-10)
    T2 = TreeNode(9)
    T3 = TreeNode(20)
    T1.left = T2
    T1.right = T3
    T4 = TreeNode(15)
    T5 = TreeNode(7)
    T3.left = T4
    T3.right = T5
    
    T6 = TreeNode(-3)
    T11 = TreeNode(-1)
    T12 = TreeNode(5)
    T13 = TreeNode(4)
    T14 = TreeNode(2)
    T15 = TreeNode(-4)
    T11.left = T12
    T12.left = T13
    T13.right = T14
    T14.left = T15
    print(test.maxPathSum(T1))
