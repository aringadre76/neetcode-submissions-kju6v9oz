# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        prev = None
        while curr:
            print(curr.val)

            temp = curr.next # saved for next iter

            curr.next = prev
            
            # for next iter
            prev = curr
            curr = temp

        return prev
            