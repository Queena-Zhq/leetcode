#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (33.36%)
# Likes:    2131
# Dislikes: 547
# Total Accepted:    350.1K
# Total Submissions: 1M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# Input:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        if len(matrix) == 0:
            return []
        else:
            d = 0
            ans = []
            row = len(matrix)
            col = len(matrix[0])
            u = 0
            l = 0
            d = row-1
            r = col-1
            while u<d and l<r:
                for j in range(l,r):
                    ans.append(matrix[u][j])
                for i in range(u,d):
                    ans.append(matrix[i][r])
                for j in range(l,r):
                    ans.append(matrix[d][col-j-1])
                for i in range(u,d):
                    ans.append(matrix[row-i-1][l])
                u += 1
                l += 1
                r -= 1
                d -= 1
            if len(ans) == row*col:
                return ans
            else:
                if l == r:
                    while u != d:
                        ans.append(matrix[u][l])
                        u += 1
                    ans.append(matrix[u][l])
                elif u == d:
                    while l != r:
                        ans.append(matrix[u][l])
                        l += 1
                    ans.append(matrix[u][l])
                return ans
# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    matrix1 = [[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]
    matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    matrix3 = [[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]
    matrix4 = [[1, 2, 3],[4,5, 6],[7,8,9],[10,11,12]]
    matrix5 = []
    matrix6 = [[1,2,3]]
    matrix7 = [[1],[2],[3]]
    matrix8 = [[2,5],[8,4],[0,-1]]
    ans1 = Test.spiralOrder(matrix1)
    print(ans1)
    ans2 = Test.spiralOrder(matrix2)
    print(ans2)
    ans3 = Test.spiralOrder(matrix3)
    print(ans3)
    ans4 = Test.spiralOrder(matrix4)
    print(ans4)
    ans5 = Test.spiralOrder(matrix5)
    print(ans5)
    ans6 = Test.spiralOrder(matrix6)
    print(ans6)
    ans7 = Test.spiralOrder(matrix7)
    print(ans7)
    ans8 = Test.spiralOrder(matrix8)
    print(ans8)

