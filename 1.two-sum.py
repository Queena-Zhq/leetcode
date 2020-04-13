#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i

# if __name__ == "__main__":
    
#     Test1 = Solution()
#     print(Test1.twoSum([1,2,3],3))


# @lc code=end

    
