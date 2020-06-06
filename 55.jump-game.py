#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (34.26%)
# Likes:    3877
# Dislikes: 316
# Total Accepted:    450.9K
# Total Submissions: 1.3M
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Determine if you are able to reach the last index.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
# jump length is 0, which makes it impossible to reach the last index.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 3 * 10^4
# 0 <= nums[i][j] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def canJump(self, nums: [int]) -> bool:
        if len(nums) <= 1:
            return True
        else:
            if nums[0] == 0:
                return False
            else:
                n = len(nums)-1
                ans = 1
                step = 0
                for i in range(len(nums)):
                    if step >= n :
                        break
                    else:
                        if i <= step:
                            step = max(step, i + nums[i])
                        else:
                            ans = 0
                            break
                if ans == 1:
                    return True
                else:
                    return False
# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    print(Test.canJump([2,3,1,1,4]))
    print(Test.canJump([3,2,1,0,4]))
    print(Test.canJump([]))
    print(Test.canJump([0]))
    print(Test.canJump([2,0]))
    print(Test.canJump([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]))
    print(Test.canJump([3,0,8,2,0,0,1]))
    print(Test.canJump([5,9,3,2,1,0,2,3,3,1,0,0]))