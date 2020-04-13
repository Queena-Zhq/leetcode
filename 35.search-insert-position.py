#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (41.23%)
# Likes:    1923
# Dislikes: 228
# Total Accepted:    543.6K
# Total Submissions: 1.3M
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in
# order.
# 
# You may assume no duplicates in the array.
# 
# Example 1:
# 
# 
# Input: [1,3,5,6], 5
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [1,3,5,6], 2
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: [1,3,5,6], 7
# Output: 4
# 
# 
# Example 4:
# 
# 
# Input: [1,3,5,6], 0
# Output: 0
# 
# 
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        if target < nums[0]:
            return 0
        else:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
                else:
                    if i == len(nums) - 1:
                        return i + 1
                    else:
                        if nums[i] < target and nums[i+1] > target:
                            return i + 1


# @lc code=end
if __name__ == "__main__":
    Test=Solution()
    print(Test.searchInsert([1,3,5,6],0))
