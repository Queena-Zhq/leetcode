#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
#
# algorithms
# Easy (42.12%)
# Likes:    2224
# Dislikes: 4641
# Total Accepted:    866.2K
# Total Submissions: 2M
# Testcase Example:  '[1,1,2]'
#
# Given a sorted array nums, remove the duplicates in-place such that each
# element appear only once and return the new length.
# 
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
# 
# Example 1:
# 
# 
# Given nums = [1,1,2],
# 
# Your function should return length = 2, with the first two elements of nums
# being 1 and 2 respectively.
# 
# It doesn't matter what you leave beyond the returned length.
# 
# Example 2:
# 
# 
# Given nums = [0,0,1,1,1,2,2,3,3,4],
# 
# Your function should return length = 5, with the first five elements of nums
# being modified to 0, 1, 2, 3, and 4 respectively.
# 
# It doesn't matter what values are set beyond the returned length.
# 
# 
# Clarification:
# 
# Confused why the returned value is an integer but your answer is an array?
# 
# Note that the input array is passed in by reference, which means modification
# to the input array will be known to the caller as well.
# 
# Internally you can think of this:
# 
# 
# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeDuplicates(nums);
# 
# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len
# elements.
# for (int i = 0; i < len; i++) {
# print(nums[i]);
# }
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        else:
            ans = list(set(nums))
            ans.sort()
            for i in range(len(ans)):
                nums[i] = ans[i]
            return len(ans)

# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    print(Test.removeDuplicates([1,1,2]))
