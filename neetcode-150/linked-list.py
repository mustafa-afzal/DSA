# Reverse a Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      prev, curr = None, head
      while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
      return prev

# Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
                tail = tail.next
            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next
        tail.next = list1 if list1 else list2
        return dummy.next

# Linked List Cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# Reorder List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        s, f = head, head
        while f and f.next:
            if s.next and f.next.next:
                s = s.next
                f = f.next.next
            else:
                break
        curr = s.next
        s.next = None
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        curr = head
        while curr and prev:
            nxt = curr.next
            prevNext = prev.next
            curr.next = prev
            prev.next = nxt
            curr = nxt
            prev = prevNext

# Remove Nth Node from End of List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr, nxt = head, head
        steps = 0
        while nxt:
            steps += 1
            nxt = nxt.next
        dist = steps - n
        if dist == 0:
            return head.next
        while curr and dist - 1:
            curr = curr.next
            dist -= 1
        curr.next = curr.next.next 
        return head

# Copy List with Random Pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        map = {}
        while curr:
            map[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            map[curr].next = map[curr.next] if curr.next else None
            map[curr].random = map[curr.random] if curr.random else None
            curr = curr.next
        return map[head] if head else None


    