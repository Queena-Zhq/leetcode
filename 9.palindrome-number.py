#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# https://leetcode.com/problems/palindrome-number/description/
#
# algorithms
# Easy (45.20%)
# Likes:    2059
# Dislikes: 1500
# Total Accepted:    848.7K
# Total Submissions: 1.8M
# Testcase Example:  '121'
#
# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backward as forward.
# 
# Example 1:
# 
# 
# Input: 121
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it
# becomes 121-. Therefore it is not a palindrome.
# 
# 
# Example 3:
# 
# 
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# 
# 
# Follow up:
# 
# Coud you solve it without converting the integer to a string?
# 
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            _x = x
            ans = 0
            while x>0:
                ans = ans*10 + x%10
                x = int(x/10)
            
            if ans == _x:
                return True
            else:
                return False
# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    print(Test.isPalindrome(12211))

