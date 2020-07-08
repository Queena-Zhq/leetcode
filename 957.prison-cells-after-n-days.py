#
# @lc app=leetcode id=957 lang=python3
#
# [957] Prison Cells After N Days
#
# https://leetcode.com/problems/prison-cells-after-n-days/description/
#
# algorithms
# Medium (39.60%)
# Likes:    608
# Dislikes: 879
# Total Accepted:    73.6K
# Total Submissions: 180.5K
# Testcase Example:  '[0,1,0,1,1,0,0,1]\n7'
#
# There are 8 prison cells in a row, and each cell is either occupied or
# vacant.
# 
# Each day, whether the cell is occupied or vacant changes according to the
# following rules:
# 
# 
# If a cell has two adjacent neighbors that are both occupied or both vacant,
# then the cell becomes occupied.
# Otherwise, it becomes vacant.
# 
# 
# (Note that because the prison is a row, the first and the last cells in the
# row can't have two adjacent neighbors.)
# 
# We describe the current state of the prison in the following way: cells[i] ==
# 1 if the i-th cell is occupied, else cells[i] == 0.
# 
# Given the initial state of the prison, return the state of the prison after N
# days (and N such changes described above.)
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: cells = [0,1,0,1,1,0,0,1], N = 7
# Output: [0,0,1,1,0,0,0,0]
# Explanation: 
# The following table summarizes the state of the prison on each day:
# Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
# Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
# Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
# Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
# Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
# Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
# Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
# Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
# Output: [0,0,1,1,1,1,1,0]
# 
# 
# 
# 
# Note:
# 
# 
# cells.length == 8
# cells[i] is in {0, 1}
# 1 <= N <= 10^9
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def prisonAfterNDays(self, cells: [int], N: int) -> [int]:
        if N == 0:
            return cells
        else:
            list_n = []

            
            list_n.append(cells)
            i = 1
            while i<=N:
                new_str = self.next_step(cells)
                if new_str not in list_n:
                    list_n.append(new_str)
                    print(new_str)
                    i = i + 1
                    cells = new_str
                else:
                    break
            if i != N:
                return list_n[N%i]
            else: return list_n[N]
    def next_step(self,cells:[int]) -> [int]:
        pre = cells[0]
        for i in range(1,len(cells)-1):
            if pre == cells[i+1]:
                pre = cells[i]
                cells[i] = 1
            else:
                pre = cells[i]
                cells[i] = 0
        cells[0] = 0
        cells[len(cells)-1] = 0
        return  cells
# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.prisonAfterNDays([0,1,0,1,1,0,0,1],7))

