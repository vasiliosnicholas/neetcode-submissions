# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        iterator = head
        head = None
        while iterator:
            next_node = iterator.next
            iterator.next = head
            head = iterator
            iterator = next_node
        return head