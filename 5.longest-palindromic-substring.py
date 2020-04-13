#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (28.05%)
# Likes:    5941
# Dislikes: 488
# Total Accepted:    852.4K
# Total Submissions: 2.9M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        else:
            ans = ""
            for i in range(len(s)):
                ans1 = self.judge(s,i,i)
                ans2 = self.judge(s,i,i+1)
                if len(ans1)>len(ans):
                    ans = ans1
                if len(ans2)>len(ans):
                    ans = ans2
            return ans
    def judge(self,s,i,j):
        while i>-1 and j<len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[(i+1):j]


# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    print(Test.longestPalindrome("bb"))
