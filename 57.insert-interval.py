#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Hard (32.99%)
# Likes:    1478
# Dislikes: 173
# Total Accepted:    239.5K
# Total Submissions: 724.1K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# Given a set of non-overlapping intervals, insert a new interval into the
# intervals (merge if necessary).
# 
# You may assume that the intervals were initially sorted according to their
# start times.
# 
# Example 1:
# 
# 
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with
# [3,5],[6,7],[8,10].
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#

# @lc code=start
class Solution:
    def insert(self, intervals: [[int]], newInterval: [int]) -> [[int]]:
        if len(intervals) == 0:
            return [newInterval]
        else:
            intervals.append(newInterval)
            intervals.sort()
            ans = []
            begin = intervals[0][0]
            end = intervals[0][1]

            for i in intervals:
                if i[0]>end:
                    ans.append([begin,end])
                    begin = i[0]
                    end = i[1]
                else:
                    begin = min(begin,i[0])
                    end = max(end,i[1])
            ans.append([begin,end])
            return ans
# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    print(Test.insert([[1,3],[6,9]],[2,5]))
    print(Test.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))
