#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (47.07%)
# Likes:    4497
# Dislikes: 496
# Total Accepted:    511.9K
# Total Submissions: 1.1M
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with
# x-axis forms a container, such that the container contains the most water.
# 
# Note: You may not slant the container and n is at least 2.
# 
# 
# 
# 
# 
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In
# this case, the max area of water (blue section) the container can contain is
# 49. 
# 
# 
# 
# Example:
# 
# 
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
#

# @lc code=start
# class Solution:
#     def maxArea(self, height: [int]) -> int:
#         ans = 0
#         for i in range(len(height)-1):
#             for j in range(i+1,len(height)):
#                 my_min = min(height[i],height[j])
#                 ans = max(ans,my_min*(j-i))
#         return ans

class Solution:
    def maxArea(self, height: [int]) -> int:
        if len(height) == 2:
            return min(height[0],height[1])
        else:
            
            start = 0
            end = len(height)-1
            ans = (end-start)*min(height[start],height[end])
            while end>start:
                if height[start]<height[end]:
                    start+=1
                else:
                    end-=1
                ans = max(ans,(end-start)*min(height[start],height[end]))

        return ans
        
# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    print(Test.maxArea([1,8,6,2,5,4,8,3,7]))

