#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (36.42%)
# Likes:    4082
# Dislikes: 261
# Total Accepted:    584.4K
# Total Submissions: 1.5M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
# 
# Example:
# 
# 
# Input:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# Output: 1->1->2->3->4->4->5->6
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
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        head = current = ListNode(0)
        my_lists = []
        for m in lists:
            if m != []:
                my_lists.append(m)
        n = len(my_lists)
        while n > 0:
            my_min = 1000
            k = 0
            empty = -1
            for i in range(n):
                if my_lists[i].val<my_min:
                    my_min = my_lists[i].val
                    k = i
            if len(my_lists)>0:
                current.next = ListNode(my_min)
                current = current.next
                new_node = my_lists[k].next
                my_lists.remove(my_lists[k])
                if new_node:
                    my_lists.append(new_node)
            n = len(my_lists)
        return head.next
# @lc code=end
if __name__ == "__main__":
    test = Solution()
    L1 = ListNode(1)
    L2 = ListNode(4)
    L3 = ListNode(5)
    L1.next = L2
    L2.next = L3
    L4 = ListNode(1)
    L5 = ListNode(3)
    L6 = ListNode(4)
    L4.next = L5
    L5.next = L6
    L7 = ListNode(2)
    L8 = ListNode(6)
    L7.next = L8
    ans = test.mergeKLists([])

    while ans:
        print(ans.val)
        ans = ans.next
