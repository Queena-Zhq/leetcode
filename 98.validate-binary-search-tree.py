#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (27.44%)
# Likes:    3619
# Dislikes: 516
# Total Accepted:    662.4K
# Total Submissions: 2.4M
# Testcase Example:  '[2,1,3]'
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
# 
# Assume a BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# 
# Example 1:
# 
# 
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 
# Input: [2,1,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# 
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
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
    def isValidBST(self, root: TreeNode, my_min = float('-inf'), my_max = float('inf')) -> bool:
        if root == None:
            return True
        else:
            if my_min<root.val<my_max:
                return self.isValidBST(root.left,my_min,min(root.val,my_max)) and self.isValidBST(root.right,max(root.val,my_min),my_max)
            else:
                return False

# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    T3 = TreeNode(3)
    T2 = TreeNode(1)
    T1 = TreeNode(2,T2,T3)
    T21 = TreeNode(5)
    T22 = TreeNode(1)
    T23 = TreeNode(4)
    T24 = TreeNode(3)
    T25 = TreeNode(6)
    T21.left = T22
    T21.right = T23
    T23.left = T24
    T23.right = T25
    T31 = TreeNode(10)
    T32 = TreeNode(5)
    T33 = TreeNode(15)
    T34 = TreeNode(6)
    T35 = TreeNode(20)
    T31.left = T32
    T31.right = T33
    T33.left = T34
    T33.right = T35
    print(Test.isValidBST(T1))
    print(Test.isValidBST(T21))
    print(Test.isValidBST(T2))
    print(Test.isValidBST(T31))
