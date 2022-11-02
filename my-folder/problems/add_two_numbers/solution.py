# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Set head node so we can return the entire modified list later
        head = l1
        
        
        # Traverse l1 and l2, until both == None (i.e. we are at the end of lists)
        while l1 != None and l2 != None:
            
            
            # Create node for shorter list
            if l1.next == None and l2.next != None:
                new = ListNode()
                l1.next = new
            elif l2.next == None and l1.next != None:
                new = ListNode()
                l2.next = new
            
            
            # Modify list
            l1.val += l2.val
            
            
            # If l1 is now greater than 9, keep the value in the ones spot
            if l1.val > 9:
                remainder = l1.val // 10
                l1.val = l1.val % 10
                
                
                # Then carry the 1 and add it to the next node
                if l1.next != None:
                    l1.next.val += remainder
                else:
                    l1.next = ListNode(1)
            
            
            # Set nodes to their next nodes
            l1 = l1.next
            l2 = l2.next
            
        return head