#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#
# https://leetcode.com/problems/same-tree/description/
#
# algorithms
# Easy (50.92%)
# Likes:    1789
# Dislikes: 53
# Total Accepted:    504.6K
# Total Submissions: 969K
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# Given two binary trees, write a function to check if they are the same or
# not.
# 
# Two binary trees are considered the same if they are structurally identical
# and the nodes have the same value.
# 
# Example 1:
# 
# 
# Input:     1         1
# ⁠         / \       / \
# ⁠        2   3     2   3
# 
# ⁠       [1,2,3],   [1,2,3]
# 
# Output: true
# 
# 
# Example 2:
# 
# 
# Input:     1         1
# ⁠         /           \
# ⁠        2             2
# 
# ⁠       [1,2],     [1,null,2]
# 
# Output: false
# 
# 
# Example 3:
# 
# 
# Input:     1         1
# ⁠         / \       / \
# ⁠        2   1     1   2
# 
# ⁠       [1,2,1],   [1,1,2]
# 
# Output: false
# 
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
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        else:
            if not p or not q:
                return False
            elif not p.left and not p.right and not q.left and not q.right:
                if p.val == q.val:
                    return True
                else:
                    return False
            else:
                p_left = p.left
                p_right = p.right
                q_left = q.left
                q_right = q.right
                if p.val != q.val:
                    return False
                else:
                    if self.isSameTree(p_left,q_left) and self.isSameTree(p_right,q_right) :
                        return True
                    else:
                        return False
            

            
# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    t1 = TreeNode(1)
    t2 = TreeNode(1)
    t3 = TreeNode(2)
    t1.left = t2
    # t1.right = t3

    t4 = TreeNode(1)
    t5 = TreeNode(1)
    t6 = TreeNode(2)
    t4.left = t5
    t4.right = t6
    print(Test.isSameTree(t1,t4))

