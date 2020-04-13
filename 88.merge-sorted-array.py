#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (37.06%)
# Likes:    1830
# Dislikes: 3738
# Total Accepted:    518.2K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
# 
# Note:
# 
# 
# The number of elements initialized in nums1 and nums2 are m and n
# respectively.
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2.
# 
# 
# Example:
# 
# 
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# Output: [1,2,2,3,5,6]
# 
#

# @lc code=start
class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0 :
            pass
        elif m == 0:
            for i in range(n):
                nums1[i] =nums2[i]
        else:
            num = len(nums1)-1
            m = m-1
            n = n-1
            while num>-1:
                if m<0:
                    nums1[num] = nums2[n]
                    n = n - 1
                elif n<0:
                    nums1[num] = nums1[m]
                    m = m - 1
                else:
                    if nums1[m]>nums2[n]:
                        nums1[num] = nums1[m]
                        m = m - 1
                    else:
                        nums1[num] = nums2[n]
                        n = n - 1
                num = num -1
        print(nums1)
# @lc code=end
if __name__ == "__main__":
    Test=Solution()
    print(Test.merge([1,2,3,0,0,0],3,[2,5,6],3))
