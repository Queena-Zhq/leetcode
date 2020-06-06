#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (53.35%)
# Likes:    2748
# Dislikes: 66
# Total Accepted:    584.7K
# Total Submissions: 1.1M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
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
# return its level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
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
    def levelOrder(self, root: TreeNode) -> [[int]]:
        if root == None:
            return []
        else:
            ans = []
            my_list1 = []
            if root.left:
                my_list1.append(root.left)
            if root.right:
                my_list1.append(root.right)
            my_list2 = []
            i = 1
            level_list = [root.val]
            while (len(my_list1) + len(my_list2)) != 0:
                if len(my_list1) ==0 or len(my_list2) == 0:
                    ans.append(level_list)
                    level_list = []
                if i ==1:
                    for my_node in my_list1:
                        level_list.append(my_node.val)
                        if my_node.left:
                            my_list2.append(my_node.left)
                        if my_node.right:
                            my_list2.append(my_node.right)
                    i =2
                    my_list1 = []
                else:
                    for my_node in my_list2:
                        level_list.append(my_node.val)
                        if my_node.left:
                            my_list1.append(my_node.left)
                        if my_node.right:
                            my_list1.append(my_node.right)
                    i = 1
                    my_list2 = []
            ans.append(level_list)
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
    print(Test.levelOrder(T1))

