# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        # stack = []
        # node = head
        # while node != None:
        #     stack.append(node)
        #     node = node.next
        # l = len(stack)
        # head = stack.pop()
        # node = head
        # for i in range(l - 1):
        #     current = stack.pop()
        #     node.next = current
        #     node = current
        # node.next = None
        # return head
        previous = None
        current = head
        nextNode = None
        while current:
            nextNode = current.next
            current.next = previous
            previous = current
            current = nextNode
        return previous
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
print(s.reverseList(a).val)