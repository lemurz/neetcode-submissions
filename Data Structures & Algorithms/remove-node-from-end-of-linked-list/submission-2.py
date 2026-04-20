# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        dummy = ListNode(0, head)
        prev = dummy

        for i in range(n-1):
            fast = fast.next

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next
        
        prev.next = slow.next

        return dummy.next

        