#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#
# https://leetcode.com/problems/backspace-string-compare/description/
#
# algorithms
# Easy (46.67%)
# Likes:    1449
# Dislikes: 75
# Total Accepted:    189.4K
# Total Submissions: 407.4K
# Testcase Example:  '"ab#c"\n"ad#c"'
#
# Given two strings S and T, return if they are equal when both are typed into
# empty text editors. # means a backspace character.
# 
# Note that after backspacing an empty text, the text will continue empty.
# 
# 
# Example 1:
# 
# 
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# 
# 
# 
# Example 2:
# 
# 
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# 
# 
# 
# Example 3:
# 
# 
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# 
# 
# 
# Example 4:
# 
# 
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
# 
# 
# Note:
# 
# 
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.
# 
# 
# Follow up:
# 
# 
# Can you solve it in O(N) time and O(1) space?
# 
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        str1 = self.tackle(S)
        # print(str1)
        str2 = self.tackle(T)
        # print(str2)
        if str1 == str2:
            return True
        else:
            return False
        
    def tackle(self,S: str):
        list1 = list(S)
        for i in range(len(list1)):
            # print(list1)
            if list1[i] == '#':
                list1[i] = '0'
                num = 1
                j = 1
                while i-j>-1 and num == 1:
                    if list1[i-j] != '0':
                        list1[i-j] = '0'
                        num = 0
                    j += 1
        
        return [i for i in list1 if i != '0' ]
        
# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    S = "y#fo##f"
    T = "y#f#o##f"
    print(Test.backspaceCompare(S,T))
