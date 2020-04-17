#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#
# https://leetcode.com/problems/range-sum-query-immutable/description/
#
# algorithms
# Easy (40.17%)
# Likes:    748
# Dislikes: 970
# Total Accepted:    183.5K
# Total Submissions: 430.7K
# Testcase Example:  '["NumArray","sumRange","sumRange","sumRange"]\n[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]'
#
# Given an integer array nums, find the sum of the elements between indices i
# and j (i ≤ j), inclusive.
# 
# Example:
# 
# Given nums = [-2, 0, 3, -5, 2, -1]
# 
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# 
# 
# 
# Note:
# 
# You may assume that the array does not change.
# There are many calls to sumRange function.
# 
# 
#

# @lc code=start
class NumArray:
    def __init__(self, nums: [int]):
        self.new_num = []
        if len(nums) == 0:
            self.new_num = None
        elif len(nums) == 1:
            self.new_num.append(nums[0])
        else:
            self.new_num.append(nums[0])
            for i in range(len(nums)-1):
                self.new_num.append(self.new_num[i]+nums[i+1])

    def sumRange(self, i: int, j: int) -> int:
        if self.new_num == None:
            return None
        else:
            if i == 0:
                return self.new_num[j]
            else:
                
                return self.new_num[j]- self.new_num[i-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end
if __name__ == "__main__":
    Test = NumArray([-1])
    print(Test.sumRange(0,0))
