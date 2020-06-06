#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (28.96%)
# Likes:    8753
# Dislikes: 528
# Total Accepted:    1.5M
# Total Submissions: 4.9M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<1:
            return 0
        else:
            start = 0
            letter_dict = {}
            nums = 0
            ans = 0
            for i in range(len(s)):
                if s[i] not in letter_dict.keys():
                    letter_dict[s[i]] = i
                    nums = i - start + 1
                else:
                    if letter_dict[s[i]]<start:
                        letter_dict[s[i]] = i
                        nums = i - start + 1
                    else:         
                        start = letter_dict[s[i]]+1
                        letter_dict[s[i]] = i
                    if nums>ans:
                        ans = nums
        ans = max(ans,nums)
        return ans
        
# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    print(Test.lengthOfLongestSubstring("abba"))