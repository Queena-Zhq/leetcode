#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (44.62%)
# Likes:    3495
# Dislikes: 83
# Total Accepted:    583.7K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
# 
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 
# 
# But the following [1,2,2,null,3,null,3] is not:
# 
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 
# 
# Follow up: Solve it both recursively and iteratively.
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
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        elif not root.left and not root.right:
            return True
        else:
            if not root.left or not root.right:
                return False
            else:
                my_left = root.left
                my_right = root.right
                if my_left.val == my_right.val and self.isSym(my_left.left,my_right.right) and self.isSym(my_left.right,my_right.left):
                    return True
                else:
                    return False
    def isSym(self,left,right):
        if not left and not right:
            return True
        else:
            if not left or not right:
                return False
            else:
                if left.val == right.val and self.isSym(left.left,right.right) and self.isSym(left.right,right.left):
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
    t1.right = t3

    t4 = TreeNode(1)
    t5 = TreeNode(2)
    t6 = TreeNode(2)
    t4.left = t5
    t4.right = t6

    print(Test.isSymmetric(t1))
    print(Test.isSymmetric(t4))
