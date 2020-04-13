#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (44.77%)
# Likes:    6927
# Dislikes: 318
# Total Accepted:    904.6K
# Total Submissions: 2M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
# 
# Example:
# 
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
# 
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        my_max = 0
        my_ans = nums[0]
        for i in range(len(nums)):
            my_max = max(nums[i],my_max+nums[i])
            my_ans = max(my_max,my_ans)
        return my_ans
# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

