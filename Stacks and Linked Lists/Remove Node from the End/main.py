# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right = head
        dummy = ListNode(0, head)
        left = dummy
        while n > 0:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
def printList(head: Optional[ListNode]) -> None:
    node = head
    while node:
        print(node.val)
        node = node.next
    return
s = Solution()
a = ListNode(1)
b = ListNode(2)
# c = ListNode(3)
# d = ListNode(4)
# e = ListNode(5)
# f = ListNode(6)
# g = ListNode(7)
a.next = b
# b.next = c
# c.next = d
# d.next = e
# e.next = f
# f.next = g
printList(s.removeNthFromEnd(a, 2))