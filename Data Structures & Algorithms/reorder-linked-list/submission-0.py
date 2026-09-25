# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: return
        
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
            
        first, second = head, prev
        while second:
            first.next, second.next, first, second = second, first.next, first.next, second.next
