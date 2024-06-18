# Definition for singly-linked list.
from typing import Optional
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # l = 0
        # node = head
        # while node != None:
        #     l += 1
        #     node = node.next
        # node = head
        # mid = math.floor(l / 2)
        # while node != None and mid != 0:
        #     node = node.next
        #     mid -= 1
        # return node
        if head is None:
            return None
        if head.next is None:
            return head
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
s = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
print(s.middleNode(a).val)