# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        
        elements = 0
        while curr:
            elements += 1
            curr = curr.next
        
        removalIndex = elements - n

        curr = head
        if removalIndex == 0:
            return head.next
        currIdx = 0
        while currIdx <= removalIndex:
            if (currIdx + 1) == removalIndex:
                curr.next = curr.next.next
                break
            currIdx += 1
            curr = curr.next
        return head


        
        

        