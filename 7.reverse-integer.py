#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.51%)
# Likes:    2505
# Dislikes: 3903
# Total Accepted:    829.6K
# Total Submissions: 3.3M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
# 
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        
        d = []
        sign = 1
        ans = 0
        if x<0:
            sign = -1
            x = x * sign

        while x>=10:
            d.append(x%10)
            x = int(x/10)
        d.append(x)

        for n in d:
            ans = ans * 10 + n
        ans = ans * sign

        if ans > 2147483647 or ans < -2147483648:
            return 0
        else:
            return ans

# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    print(Test.reverse(-123))

