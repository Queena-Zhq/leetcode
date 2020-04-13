#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (49.31%)
# Likes:    3588
# Dislikes: 534
# Total Accepted:    897.1K
# Total Submissions: 1.7M
# Tes  tcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = ListNode(0)
        ans_List = ListNode(0)
        num = 0
        if l1 == None and l2 != None:
            return l2
        elif l1 != None and l2 == None:
            return l1
        elif l1 == None and l2 == None:
            return None
        else:
            while l1 != None and l2 != None:
                if l1.val<l2.val:
                    ans_List.next = ListNode(l1.val)
                    l1 = l1.next
                else: 
                    ans_List.next = ListNode(l2.val)
                    l2 = l2.next
                if num == 0:
                    l.next = ans_List.next
                    num = 1
                ans_List = ans_List.next
            if l1 != None and l2 == None:
                ans_List.next = l1
            elif l1 == None and l2 != None:
                ans_List.next = l2
            else:
                print("Situation")
            return l.next

# @lc code=end

if __name__ == "__main__":
    Test = Solution()
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(4)
    l1.next = l2
    l2.next = l3

    l4 = ListNode(1)
    l5 = ListNode(3)
    l6 = ListNode(4)
    l4.next = l5
    l5.next = l6
    l = ListNode(0)
    l.next = Test.mergeTwoLists(l1,l4)
    l = l.next
    while l != None:
        print(l.val)
        print("->")
        l = l.next

