#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (40.85%)
# Likes:    1505
# Dislikes: 255
# Total Accepted:    407.3K
# Total Submissions: 951.6K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
# 
# The input strings are both non-empty and contains only characters 1 or 0.
# 
# Example 1:
# 
# 
# Input: a = "11", b = "1"
# Output: "100"
# 
# Example 2:
# 
# 
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
# 
# Constraints:
# 
# 
# Each string consists only of '0' or '1' characters.
# 1 <= a.length, b.length <= 10^4
# Each string is either "0" or doesn't contain any leading zero.
# 
# 
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "0":
            return b
        elif b == "0":
            return a
        else:
            if len(a)>len(b):
                b = b.zfill(len(a))
            else:
                a = a.zfill(len(b))
            ans = []
            a = a[::-1]
            b = b[::-1]
            rent = 0
            for i in range(len(a)):
                ans.append(str(int((int(a[i])+int(b[i])+rent)%2)))
                rent = int(int(int(a[i])+int(b[i])+rent)/2)
                
            if rent == 1:
                ans.append("1")
            ans.reverse()
            num = "".join(ans)
            return num
            



# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    print(Test.addBinary("1111","1111"))
