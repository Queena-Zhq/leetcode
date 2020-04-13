#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (43.52%)
# Likes:    1247
# Dislikes: 100
# Total Accepted:    426.8K
# Total Submissions: 957.8K
# Testcase Example:  '[1,1,2]'
#
# Given a sorted linked list, delete all duplicates such that each element
# appear only once.
# 
# Example 1:
# 
# 
# Input: 1->1->2
# Output: 1->2
# 
# 
# Example 2:
# 
# 
# Input: 1->1->2->3->3
# Output: 1->2->3
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        elif head.next == None:
            return head
        else:
            nxt = head.next
            now = head
            while nxt != None:
                if now.val != nxt.val:
                    now.next = nxt
                    now = now.next
                else:
                    if nxt.next == None:
                        now.next = None
                nxt = nxt.next
            return head
# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    l1 = ListNode(1)
    l2 = ListNode(1)
    l3 = ListNode(2)
    l1.next = l2
    l2.next = l3

    l = Test.deleteDuplicates(l1)
    while l != None:
        print(l.val)
        l = l.next
