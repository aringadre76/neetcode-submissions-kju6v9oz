# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1, curr2 = list1, list2
        
        merged = dummy = ListNode()
        while curr1 and curr2:

            if curr1.val <= curr2.val:
                print(curr1.val, curr2.val)
                merged.next = curr1
                curr1 = curr1.next

            else:
                print(curr1.val, curr2.val)
                merged.next = curr2
                curr2 = curr2.next

            merged = merged.next

        if curr1:
            merged.next = curr1
        else:
            merged.next = curr2

        return dummy.next