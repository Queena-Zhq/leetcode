#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (34.93%)
# Likes:    2983
# Dislikes: 221
# Total Accepted:    586.1K
# Total Submissions: 1.7M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, remove the n-th node from the end of list and return its
# head.
# 
# Example:
# 
# 
# Given linked list: 1->2->3->4->5, and n = 2.
# 
# After removing the second node from the end, the linked list becomes
# 1->2->3->5.
# 
# 
# Note:
# 
# Given n will always be valid.
# 
# Follow up:
# 
# Could you do this in one pass?
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count = n
        pre_node = head
        next_node = head
        head_sign = 0
        while next_node:
            if count>0:
                count -= 1
                if count == 0:
                    head_sign = 1
                next_node = next_node.next
            else:
                head_sign = 0
                if next_node.next:
                    pre_node = pre_node.next
                next_node = next_node.next
        if count == 0 and head_sign == 1:
            return head.next
        else:
            current_node = pre_node.next
            pre_node.next = current_node.next
            return head
# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    L1 = ListNode(1)
    L2 = ListNode(2)
    L3 = ListNode(3)
    L4 = ListNode(4)
    L5 = ListNode(5)
    L1.next = L2
    L2.next = L3
    L3.next = L4
    L4.next = L5
    
    ans = Test.removeNthFromEnd(L1,5)
    while ans:
        print(ans.val)
        ans = ans.next

