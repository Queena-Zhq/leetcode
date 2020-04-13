#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (41.71%)
# Likes:    1296
# Dislikes: 2134
# Total Accepted:    540.2K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty array of digits representing a non-negative integer, plus
# one to the integer.
# 
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contain a single digit.
# 
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# 
# 
# Example 2:
# 
# 
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# 
#

# @lc code=start
class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        digits.reverse()
        rent = 1
        num = 0
        for i in range(len(digits)):
            num = digits[i]
            digits[i] = int((num+rent)%10)
            rent = int((num+rent)/10)
        if rent != 0:
            digits.append(rent)
        digits.reverse()
        return digits
# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    print(Test.plusOne([1,2,3]))
