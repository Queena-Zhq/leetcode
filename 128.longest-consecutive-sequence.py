#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (44.40%)
# Likes:    3251
# Dislikes: 174
# Total Accepted:    298.3K
# Total Submissions: 666.5K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
# 
# Your algorithm should run in O(n) complexity.
# 
# Example:
# 
# 
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
# 
# 
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: [int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        else:
            nums = set(nums)
            nums = list(nums)
            nums.sort()
            n = len(nums)
            ans = 0
            start , end = 0,1
            while end <n:
                if nums[end] - nums[end-1] == 1:
                    end = end +1
                else:
                    ans = max(ans,end - start)
                    start = end
                    end = end+1
            return max(ans,end-start)
# @lc code=end
if __name__ == "__main__":
    test = Solution()
    print(test.longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(test.longestConsecutive([0,0]))
    print(test.longestConsecutive([0,-1]))
    print(test.longestConsecutive([1,2,0,1]))
