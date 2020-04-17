#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (46.91%)
# Likes:    1834
# Dislikes: 392
# Total Accepted:    457.1K
# Total Submissions: 914.6K
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number n is "happy".
# 
# A happy number is a number defined by the following process: Starting with
# any positive integer, replace the number by the sum of the squares of its
# digits, and repeat the process until the number equals 1 (where it will
# stay), or it loops endlessly in a cycle which does not include 1. Those
# numbers for which this process ends in 1 are happy numbers.
# 
# Return True if n is a happy number, and False if not.
# 
# Example: 
# 
# 
# Input: 19
# Output: true
# Explanation: 
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# 
# 
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        my_dict = []
        ans = n
        while ans != 1 and ans not in my_dict:
            my_dict.append(ans)
            num = list(str(ans))
            ans = self.calculate(num)
        if ans == 1:
            return True
        else:
            return False
    def calculate(self,n : [int]):
        ans = 0
        for i in n:
            ans += int(i)*int(i)
        return ans
        

# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    print(Test.isHappy(18))

