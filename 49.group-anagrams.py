#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (49.87%)
# Likes:    3095
# Dislikes: 166
# Total Accepted:    621.5K
# Total Submissions: 1.1M
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
# 
# Example:
# 
# 
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# Note:
# 
# 
# All inputs will be in lowercase.
# The order of your output does not matter.
# 
# 
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        my_dict = {}
        ans = []
        for i in strs:
            if str(sorted(i)) not in my_dict.keys():
                 my_dict[str(sorted(i))] = [i]
            else:
                my_dict[str(sorted(i))].append(i)
        return list(my_dict.values())
                    
# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    print(Test.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

