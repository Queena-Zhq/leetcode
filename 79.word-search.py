#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (34.32%)
# Likes:    3366
# Dislikes: 165
# Total Accepted:    443.2K
# Total Submissions: 1.3M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given a 2D board and a word, find if the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# Example:
# 
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
# 
# 
# 
# Constraints:
# 
# 
# board and word consists only of lowercase and uppercase English letters.
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3
# 
# 
#

# @lc code=start
class Solution:
    def exist(self, board: [[str]], word: str) -> bool:
        if len(board) == 0:
            return False
        else:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if self.my_exist(board,i,j,word):
                        return True
            return False
    def my_exist(self,board : [[str]], i:int,j:int,word:str) -> bool:
        if len(word) == 0:
            return True
        elif i<0 or j<0 or i== len(board) or j == len(board[0]):
            return False
        else:
            if word[0] == board[i][j]:
                char = board[i][j]
                board[i][j] = "#"
                if self.my_exist(board,i+1,j,word[1:]) or self.my_exist(board,i-1,j,word[1:]) or self.my_exist(board,i,j+1,word[1:]) or self.my_exist(board,i,j-1,word[1:]):
                    return True
                else:
                    board[i][j] = char
                    return False
            else:
                return False
# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    print(Test.exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']],"ABCCED"))
    print(Test.exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']],"SEE"))
    print(Test.exist([['A','B','C','E'],['S','F','C','S'],['A','D','E','E']],"ABCB"))

