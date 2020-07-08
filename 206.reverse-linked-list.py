#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (61.09%)
# Likes:    4405
# Dislikes: 89
# Total Accepted:    979.3K
# Total Submissions: 1.6M
# Testcase Example:  '[1,2,3,4,5]'
#
# Reverse a singly linked list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# 
# 
# Follow up:
# 
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# recursive
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head != None:
            if head.next == None:
                return head
            else:
                my_link = self.reverseList(head.next)
                head.next.next = head
                head.next = None
                return my_link
        else:
            return head

# none recursive
class Solution1:
    def reverseList(self,head:ListNode) ->ListNode:
        if head == None:
            return head
        else:
            if head.next == None:
                return head
            else:
                my_head = head
                my_current = head.next
                my_head.next = None
                my_next = my_current.next
                while my_next:
                    my_current.next = my_head
                    my_head = my_current
                    my_current = my_next
                    my_next = my_next.next

                my_current.next = my_head
                return my_current
# @lc code=end
if __name__ == "__main__":
    test = Solution1()
    T1 = ListNode(1)
    T2 = ListNode(2)
    T3 = ListNode(3)
    T4 = ListNode(4)
    T1.next = T2
    T2.next = T3
    T3.next = T4

    ans = test.reverseList(T1)
    while ans!=None:
        print(ans.val)
        ans = ans.next

