#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
# https://leetcode.com/problems/min-stack/description/
#
# algorithms
# Easy (39.11%)
# Likes:    3028
# Dislikes: 296
# Total Accepted:    510.1K
# Total Submissions: 1.2M
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]'
#
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
# 
# 
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# 
# Output
# [null,null,null,null,-3,null,0,-2]
# 
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
# 
# 
# 
# Constraints:
# 
# 
# Methods pop, top and getMin operations will always be called on non-empty
# stacks.
# 
# 
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def push(self, x: int) -> None:
        self.nums.append(x)

    def pop(self) -> None:
        if len(self.nums) == 0:
            return None
        else:
            return self.nums.pop()

    def top(self) -> int:
        if len(self.nums) ==0:
            return None
        else:
            n = len(self.nums)
            return self.nums[n-1]

    def getMin(self) -> int:
        if len(self.nums) == 0:
            return None
        else:
            min = self.nums[0]
            for i in self.nums:
                if i<min:
                    min = i
            return min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
if __name__ == "__main__":
    Test = MinStack()
    Test.push(1)
    Test.push(2)
    Test.push(3)
    Test.push(-2)
    print(Test.getMin())
    print(Test.pop())

