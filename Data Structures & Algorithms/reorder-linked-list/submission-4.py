# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next  # START reversing from node after slow
        slow.next = None  # CUT the list here!

        prev = None
        curr = mid
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        left = head
        right = prev
        while left and right:
            temp1 = left.next
            temp2 = right.next

            left.next = right
            right.next = temp1

            left = temp1
            right = temp2

        self.printList(head)

    def printList(self, node):
        res = []
        while node:
            res.append(node.val)
            node = node.next
        print(res)


            

        






    def printList(self, node):
        res = []
        while node:
            res.append(node.val)
            node = node.next
        print(res)
