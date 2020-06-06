#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (34.25%)
# Likes:    4594
# Dislikes: 435
# Total Accepted:    691.6K
# Total Submissions: 2M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# 
# You are given a target value to search. If found in the array return its
# index, otherwise return -1.
# 
# You may assume no duplicate exists in the array.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# Example 1:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# 
#

# @lc code=start
class Solution:
    def search(self, nums: [int], target: int) -> int:
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        else:
            start = 0
            end = len(nums)-1

            while start<end:
                middle = int((start+end)/2)
                if target == nums[start]:
                    return start
                elif target == nums[middle]:
                    return middle
                elif target == nums[end]:
                    return end
                else:
                    if nums[start]<nums[end]:
                        if target < nums[middle] and middle != end:
                            end = middle
                        elif nums[middle] < target and start != middle:
                            start = middle
                        else:
                            return -1
                    else:
                        if nums[start] < nums[middle]:
                            if target<nums[middle] and nums[start]<target:
                                end = middle
                            else:
                                start = middle
                        elif nums[middle]<nums[end]:
                            if nums[middle]<target and target < nums[end]:
                                start = middle
                            else:
                                end = middle
                        else:
                            return -1   
            return -1
# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    print(Test.search([4,5,6,7,8,1,2,3],3))
    print(Test.search([4,5],4))
    print(Test.search([4,5],5))
    print(Test.search([4,5,6,7,0,1,2],3))
    print(Test.search([4,5,6,7,8,1,2,3],8))

