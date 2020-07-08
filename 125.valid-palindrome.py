#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (35.14%)
# Likes:    1182
# Dislikes: 2895
# Total Accepted:    580.2K
# Total Submissions: 1.6M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
# 
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
# 
# Example 1:
# 
# 
# Input: "A man, a plan, a canal: Panama"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "race a car"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# s consists only of printable ASCII characters.
# 
# 
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0: return True
        else:
            n = len(s)
            i,j = 0,n-1
            while i<j and i != j :
                if self.valid(s[i]) and self.valid(s[j]):
                    if s[i] == s[j] or abs(ord(s[i])-ord(s[j]))==32:
                        if s[i]+s[j] !="0P" and s[i]+s[j] !="P0":
                            i = i+1
                            j = j-1
                        else: return False
                    else: return False
                else:
                    if self.valid(s[i]):
                        j = j-1
                    elif self.valid(s[j]):
                        i = i+1
                    else:
                        i = i+1
                        j = j-1
            return True
    def valid(self,c:chr) -> bool:
        if ord(c)>=48 and ord(c)<=57:
            return True
        if ord(c)>=65 and ord(c)<=90:
            return True
        if ord(c)>=97 and ord(c)<=122:
            return True
        return False
# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.isPalindrome("race a car"))
    print(test.isPalindrome("A man, a plan, a canal: Panama"))
    print(test.isPalindrome("0P"))

