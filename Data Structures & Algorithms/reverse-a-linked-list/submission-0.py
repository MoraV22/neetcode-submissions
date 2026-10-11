# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev, curr= None, ListNode(head.val)

        while head.next:
            prev,curr = curr, ListNode(head.next.val) 
            curr.next=prev
            head=head.next
        return curr
        
            



