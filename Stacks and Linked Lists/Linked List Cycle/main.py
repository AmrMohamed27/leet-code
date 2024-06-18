# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # temp = {}
        # node = head
        # while node:
        #     if temp.__contains__(node):
        #         return True
        #     temp[node] = node.val
        #     node = node.next
        # return False
        if not head:
            return False
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast and fast is slow:
                return True
        return False
s = Solution()
a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(-4)
a.next = b
b.next = c
c.next = d
d.next = b
z = ListNode(1)
zz = ListNode(2)
z.next = zz
print(s.hasCycle(z))
