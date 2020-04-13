#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (37.37%)
# Likes:    4414
# Dislikes: 203
# Total Accepted:    906.1K
# Total Submissions: 2.4M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# Note that an empty string is also considered valid.
# 
# Example 1:
# 
# 
# Input: "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: "{[]}"
# Output: true
# 
# 
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        diet = {}
        diet['('] = 1
        diet[')'] = 4
        diet['{'] = 2
        diet['}'] = 5
        diet['['] = 3
        diet[']'] = 6
        l = []
        if len(s) == 0:
            return True
        elif len(s)%2 != 0:
            return False
        else:
            for i in range(len(s)):
                if diet[s[i]] < 4:
                    l.append(s[i])
                elif diet[s[i]] > 3 and len(l) == 0:
                    return False
                else:
                    c = l.pop()
                    if diet[s[i]] - diet[c] != 3:
                        return False
            if len(l) == 0:
                return True
            else:
                return False

# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    print(Test.isValid("{[]}"))
