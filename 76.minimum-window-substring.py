#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (34.01%)
# Likes:    4150
# Dislikes: 292
# Total Accepted:    378.3K
# Total Submissions: 1.1M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
# 
# Example:
# 
# 
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# 
# 
# Note:
# 
# 
# If there is no such window in S that covers all characters in T, return the
# empty string "".
# If there is such window, you are guaranteed that there will always be only
# one unique minimum window in S.
# 
# 
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        my_dict = {}
        for i in range(len(s)):
            if s[i] in t:
                if s[i] not in my_dict.keys():
                    my_dict[s[i]] = []
                    my_dict[s[i]].append(i)
                else:
                    my_dict[s[i]].append(i)
        
# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    Test.minWindow("dsad","ad")
