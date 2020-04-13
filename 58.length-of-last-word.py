#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
# https://leetcode.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (32.32%)
# Likes:    558
# Dislikes: 2204
# Total Accepted:    348.2K
# Total Submissions: 1.1M
# Testcase Example:  '"Hello World"'
#
# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word (last word means the last
# appearing word if we loop from left to right) in the string.
# 
# If the last word does not exist, return 0.
# 
# Note: A word is defined as a maximal substring consisting of non-space
# characters only.
# 
# Example:
# 
# 
# Input: "Hello World"
# Output: 5
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif " " not in s:
            return len(s)
        else:
            start = -1
            end = -1
            for i in range(len(s)):
                if s[i-1] == " " and s[i]!=" ":
                    start = i
                    end = 0
                elif s[i] ==" " and s[i-1] != " ":
                    end = i
                else:
                    pass
            if end == 0:
                return i-start+1
            else:
                return end - start

# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    print(Test.lengthOfLastWord("   "))

