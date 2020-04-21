#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (55.33%)
# Likes:    3389
# Dislikes: 110
# Total Accepted:    755K
# Total Submissions: 1.3M
# Testcase Example:  '[0,1,0,3,12]'
#
# Given an array nums, write a function to move all 0's to the end of it while
# maintaining the relative order of the non-zero elements.
# 
# Example:
# 
# 
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# 
# Note:
# 
# 
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# 
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        record = 0
        n = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                record +=1
            else:
                if record == 0:
                    pass
                else:
                    n = nums[i-record]
                    nums[i-record] = nums[i]
                    nums[i] = n

# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    t = [0,1,0,3,12]
    Test.moveZeroes(t)
    print(t)

