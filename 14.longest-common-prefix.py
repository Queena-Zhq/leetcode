#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (34.22%)
# Likes:    2189
# Dislikes: 1724
# Total Accepted:    678.3K
# Total Submissions: 1.9M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
# 
# If there is no common prefix, return an empty string "".
# 
# Example 1:
# 
# 
# Input: ["flower","flow","flight"]
# Output: "fl"
# 
# 
# Example 2:
# 
# 
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# 
# 
# Note:
# 
# All given inputs are in lowercase letters a-z.
# 
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs : [str]) -> str:
        ans = ""
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            len_list = [len(s) for s in strs]
            less_list = len_list.index(min(len_list))
            comp = strs[less_list]
            for i in range(len(comp)):
                ans = ans + comp[i]
                num = 0
                for s in strs:
                    if ans in s:
                        num = num + 1
                if num < len(strs):
                    ans = ans[:-1]
            return ans

# @lc code=end
# Wrong Answer
# 106/118 cases passed (N/A)
# Testcase
# ["ca","a"]
# Answer
# "a"
# Expected Answer
# ""

if __name__ == "__main__":
    Test = Solution()
    print(Test.longestCommonPrefix(["ca","a"]))
