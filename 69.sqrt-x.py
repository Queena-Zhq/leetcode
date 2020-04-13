#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (32.23%)
# Likes:    1128
# Dislikes: 1750
# Total Accepted:    503.4K
# Total Submissions: 1.5M
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
# 
# Compute and return the square root of x, where x is guaranteed to be a
# non-negative integer.
# 
# Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
# 
# Example 1:
# 
# 
# Input: 4
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
# the decimal part is truncated, 2 is returned.
# 
# 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            my_min = 0
            my_max = x
            n = int((my_max-my_min)/2)+my_min
            while n:
                if n*n == x:
                    return n
                elif n*n<x and (n+1)*(n+1)>x:
                    return n
                else:
                    if n*n<x:
                        my_min = n
                        n = int((my_max-my_min)/2)+my_min
                    else:
                        my_max = n
                        n = int((my_max-my_min)/2)+my_min
                                           
# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    print(Test.mySqrt(6))

