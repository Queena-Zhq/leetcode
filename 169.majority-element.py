#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (54.41%)
# Likes:    2657
# Dislikes: 207
# Total Accepted:    533.8K
# Total Submissions: 947.7K
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always
# exist in the array.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: 3
# 
# Example 2:
# 
# 
# Input: [2,2,1,1,1,2,2]
# Output: 2
# 
# 
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: [int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            nums.sort()
            return nums[int((len(nums)-1)/2)]

# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    print(Test.majorityElement([2,2,1,1,1,2,2]))
