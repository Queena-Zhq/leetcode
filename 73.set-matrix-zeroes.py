#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
# https://leetcode.com/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (42.52%)
# Likes:    1868
# Dislikes: 287
# Total Accepted:    301.9K
# Total Submissions: 708.5K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a m x n matrix, if an element is 0, set its entire row and column to 0.
# Do it in-place.
# 
# Example 1:
# 
# 
# Input: 
# [
# [1,1,1],
# [1,0,1],
# [1,1,1]
# ]
# Output: 
# [
# [1,0,1],
# [0,0,0],
# [1,0,1]
# ]
# 
# 
# Example 2:
# 
# 
# Input: 
# [
# [0,1,2,0],
# [3,4,5,2],
# [1,3,1,5]
# ]
# Output: 
# [
# [0,0,0,0],
# [0,4,5,0],
# [0,3,1,0]
# ]
# 
# 
# Follow up:
# 
# 
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best
# solution.
# Could you devise a constant space solution?
# 
# 
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        col = []
        for line in matrix:
            if 0 in line:
                for j in range(len(line)):
                    if line[j] == 0:
                        col.append(j)
                matrix[matrix.index(line)] = [0 for i in range(len(line))]
        col = list(set(col))
        for i in col:
            for j in range(len(matrix)):
                matrix[j][i] = 0
        # print(matrix)
# @lc code=end
if __name__ == "__main__":
    test = Solution()
    test.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
    test.setZeroes([[1,1,1],[1,0,1],[1,1,1]])
