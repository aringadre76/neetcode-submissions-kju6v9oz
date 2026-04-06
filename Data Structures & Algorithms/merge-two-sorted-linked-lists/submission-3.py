# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()

        curr1 = list1
        curr2 = list2

        # if curr1.val < curr2.val:
        #     dummy.next = curr1
        # else:
        #     dummy.next = curr2
        
        # curr1 = curr1.next
        # curr2 = curr2.next
        new = dummy
        
        while curr1 or curr2:
            if curr1 is None:
                new.next = curr2
                break
            elif curr2 is None:
                new.next = curr1
                break
            elif curr1.val < curr2.val:
                new.next = curr1
                curr1 = curr1.next
            else:
                new.next = curr2
                curr2 = curr2.next

            new = new.next

            
        print(dummy)
        return dummy.next
