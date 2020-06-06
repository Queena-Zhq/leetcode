#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways/description/
#
# algorithms
# Medium (23.01%)
# Likes:    2264
# Dislikes: 2504
# Total Accepted:    359.6K
# Total Submissions: 1.5M
# Testcase Example:  '"12"'
#
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
# 
# 
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# 
# 
# Given a non-empty string containing only digits, determine the total number
# of ways to decode it.
# 
# Example 1:
# 
# 
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# 
# 
# Example 2:
# 
# 
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2
# 6).
# 
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            if int(s) == 0:
                return 0
            else:
                return 1
        elif len(s) == 2:
            if int(s) <=26 and int(s)>=10:
                if int(s[1]) == 0:
                    return 1
                else:
                    return 2
            elif int(s)>0 and int(s)<10:
                return 0
            else:
                if int(s[1]) == 0:
                    return 0
                else:
                    return 1
        else:
            ans = []
            ans.append(self.numDecodings(s[0]))
            ans.append(self.numDecodings(s[0:2]))
            for i in range(2,len(s)):
                if int(s[i]) != 0:
                    ans1 = ans[i-1]
                else:
                    ans1 = 0

                if int(s[i-1:i+1])>=10 and int(s[i-1:i+1])<=26:
                    ans2 = ans[i-2]
                else:
                        ans2 = 0
                ans.append(ans1+ans2)
            return ans.pop()            
# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    print(Test.numDecodings("12"))
    print(Test.numDecodings("226"))
    print(Test.numDecodings("00"))
    print(Test.numDecodings("01"))
    print(Test.numDecodings("10"))
    print(Test.numDecodings("100"))
