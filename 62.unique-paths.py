#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths/description/
#
# algorithms
# Medium (49.53%)
# Likes:    2630
# Dislikes: 186
# Total Accepted:    416.2K
# Total Submissions: 803K
# Testcase Example:  '3\n2'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# How many possible unique paths are there?
# 
# 
# Above is a 7 x 3 grid. How many possible unique paths are there?
# 
# 
# Example 1:
# 
# 
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the
# bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# 
# 
# Example 2:
# 
# 
# Input: m = 7, n = 3
# Output: 28
# 
# 
# 
# Constraints:
# 
# 
# 1 <= m, n <= 100
# It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.
# 
# 
#

# @lc code=start
# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         if m == 1 or n == 1:
#             return 1
#         else:
#             start = [1,1]
#             end = [m,n]
#             ans = 0
#             loop = []
#             loop.append(start)
#             while loop:
#                 current = loop.pop()
#                 if current == end:
#                     ans += 1
#                 elif current[0] == m:
#                     loop.append([current[0],current[1]+1])
#                 elif current[1] == n:
#                     loop.append([current[0]+1,current[1]])
#                 else:
#                     loop.append([current[0]+1,current[1]])
#                     loop.append([current[0],current[1]+1])
#             return ans
# class Solution:
#     def uniquePaths(self, m : int, n: int) -> int:
#         if m == 1 or n == 1:
#             return 1
#         else:
#             return self.uniquePaths(m-1,n)+self.uniquePaths(m,n-1)
class Solution:
    def uniquePaths(self,m : int, n:int) -> int:
        if m == 1 or n == 1:
            return 1
        else:
            ans = [[1 for x in range(n)] for y in range(m)]
            for i in range(1,m):
                for j in range(1,n):
                    ans[i][j] = ans[i][j-1]+ ans[i-1][j]
            return ans[m-1][n-1]
# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    print(Test.uniquePaths(3,2))
    print(Test.uniquePaths(7,3))
