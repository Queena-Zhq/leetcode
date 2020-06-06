#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (47.17%)
# Likes:    3078
# Dislikes: 87
# Total Accepted:    342.2K
# Total Submissions: 720.7K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# Given preorder and inorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.
# 
# For example, given
# 
# 
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# 
# Return the following binary tree:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
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
    def buildTree(self, preorder: [int], inorder: [int]) -> TreeNode:
        if len(preorder) == 0 and len(inorder) == 0:
            return None
        else:
            
# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    L1 = [3,9,20,15,7]
    L2 = [9,3,15,20,7]

    Node = Test.buildTree(L1,L2)

    list_node = [Node]
    while list_node:
        new_list = []
        for i in list_node:
            print(i.val)
            if i.left:
                new_list.append(i.val)
            if i.right:
                new_list.append(i.right)
        list_node = new_list

