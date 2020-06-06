#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (54.62%)
# Likes:    3472
# Dislikes: 106
# Total Accepted:    512.2K
# Total Submissions: 935.2K
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given a set of candidate numbers (candidates) (without duplicates) and a
# target number (target), find all unique combinations in candidates where the
# candidate numbers sums to target.
# 
# The same repeated number may be chosen from candidates unlimited number of
# times.
# 
# Note:
# 
# 
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: [int], target: int) -> [[int]]:
        if len(candidates) == 0:
            return []
        else:
            candidates = sorted(candidates)
            results = self.my_calculate(candidates,[],target,[])
            return results

    def my_calculate(self, candidates:[int], my_nums: [int], target:int, my_results: [[int]]):
            if sum(my_nums) == target:
                my_results.append(my_nums)
                return my_results
            else:
                for i in candidates:
                    my_nums.append(i)
                    if sum(my_nums)<=target:
                        my_results = self.my_calculate(candidates,my_nums,target,my_results)
                        my_nums.pop()
                    else:
                        my_nums.pop()
                        break
                return my_results
                    
            
# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    print(Test.combinationSum([2,3,5],8))
    print(Test.combinationSum([2,3,6,7],7))

