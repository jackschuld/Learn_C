# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr:
            while curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next
            curr = curr.next
        return head
        

        
        
        
        
        #cur=head
        #while cur:
        #    while cur.next and cur.next.val==cur.val:
        #        cur.next=cur.next.next
        #    cur=cur.next
        #return head