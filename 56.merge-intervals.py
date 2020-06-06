#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (36.86%)
# Likes:    3511
# Dislikes: 257
# Total Accepted:    529.7K
# Total Submissions: 1.4M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
# 
# Example 1:
# 
# 
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
# 
# 
# Example 2:
# 
# 
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#

# @lc code=start
class Solution:
    def merge(self, intervals: [[int]]) -> [[int]]:
        if len(intervals)<=1:
            return intervals
        else:
            intervals.sort()
            ans = []
            begin = intervals[0][0]
            end = intervals[0][1]
            for i in intervals:
                if i[0]>end:
                    ans.append([begin,end])
                    begin = i[0]
                    end = i[1]
                elif i[1]<=end and i[0]>=begin:
                    continue
                elif i[0]<= end and i[1]>end:
                    end = i[1]
                else:
                    continue
            ans.append([begin,end])
            return ans

# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    print(Test.merge([[1,3],[2,6],[8,10],[15,18]]))
    print(Test.merge([[1,4],[4,5]]))
