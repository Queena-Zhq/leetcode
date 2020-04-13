#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr/description/
#
# algorithms
# Easy (33.05%)
# Likes:    1359
# Dislikes: 1742
# Total Accepted:    605.8K
# Total Submissions: 1.8M
# Testcase Example:  '"hello"\n"ll"'
#
# Implement strStr().
# 
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
# 
# Example 1:
# 
# 
# Input: haystack = "hello", needle = "ll"
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# 
# 
# Clarification:
# 
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
# 
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().
# 
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        elif needle not in haystack:
            return -1
        else:
            first = -1
            nxt = 0
            n = 0
            while n <len(needle):
                if haystack[nxt] == needle[n]:
                    if first == -1:
                        first = nxt
                    n = n + 1
                    nxt = nxt + 1
                else:
                    if first > -1:
                        nxt = first + 1
                        first = -1
                        n = 0
                    else:
                        nxt = nxt + 1
            return first
                

# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    print(Test.strStr("mississippi","issip"))
