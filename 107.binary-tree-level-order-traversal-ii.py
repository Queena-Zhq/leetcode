#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (51.00%)
# Likes:    1380
# Dislikes: 208
# Total Accepted:    324.9K
# Total Submissions: 621.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the bottom-up level order traversal of its nodes'
# values. (ie, from left to right, level by level from leaf to root).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its bottom-up level order traversal as:
# 
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
# ]
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
    def levelOrderBottom(self, root: TreeNode) -> [[int]]:
        if root:
            next_list = []
            current_list = []
            ans = []
            next_list.append(root)
            while len(next_list) !=0:
                current_list = next_list
                next_list = []
                level = []
                while len(current_list) !=0:
                    node = current_list.pop(0)
                    if node:
                        next_list.append(node.left)
                        next_list.append(node.right)
                        level.append(node.val)
                if len(level) !=0:
                    ans.append(level)
            ans.reverse()
            return ans

# @lc code=end
if __name__ == "__main__":
    
    Test = Solution()
    T1 = TreeNode(3)
    T2 = TreeNode(9)
    T3 = TreeNode(20)
    T4 = TreeNode(15)
    T5 = TreeNode(7)
    T1.left = T2
    T1.right = T3
    T3.left = T4
    T3.right = T5
    print(Test.levelOrderBottom(T1))

