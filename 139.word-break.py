#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (36.86%)
# Likes:    3645
# Dislikes: 197
# Total Accepted:    490.1K
# Total Submissions: 1.3M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, determine if s can be segmented into a space-separated
# sequence of one or more dictionary words.
# 
# Note:
# 
# 
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
# 
# 
# Example 1:
# 
# 
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
# 
# 
# Example 2:
# 
# 
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
# 
# 
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        if len(s) == 0: return True
        else:
            label = []
            for i in range(len(s)):
                for j in range(0,i+1):
                    new_str = s[j:i+1]
                    if new_str in wordDict and (j==0 or j-1 in label):
                        label.append(i)
            # print(label)
            if len(s)-1 in label:
                return True
            else: return False

# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.wordBreak("leetcode",["leet","code"]))
    print(test.wordBreak("applepenapple",["apple","pen"]))
    print(test.wordBreak("catsandog",["cats","dog","sand","and","cat"]))
