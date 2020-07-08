#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#
# https://leetcode.com/problems/arranging-coins/description/
#
# algorithms
# Easy (39.73%)
# Likes:    569
# Dislikes: 679
# Total Accepted:    141K
# Total Submissions: 335.5K
# Testcase Example:  '5'
#
# You have a total of n coins that you want to form in a staircase shape, where
# every k-th row must have exactly k coins.
# ⁠
# Given n, find the total number of full staircase rows that can be formed.
# 
# n is a non-negative integer and fits within the range of a 32-bit signed
# integer.
# 
# Example 1:
# 
# n = 5
# 
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
# 
# Because the 3rd row is incomplete, we return 2.
# 
# 
# 
# Example 2:
# 
# n = 8
# 
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
# 
# Because the 4th row is incomplete, we return 3.
# 
# 
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        my_sum = 0
        ans = 0
        while my_sum < n:
            if n-my_sum >=ans +1:
                ans = ans +1
                my_sum = my_sum + ans
            else:
                break
        return ans
# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.arrangeCoins(5))

