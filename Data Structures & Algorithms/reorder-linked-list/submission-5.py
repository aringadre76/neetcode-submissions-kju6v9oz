class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        
        # Reverse second half
        prev = None
        curr = mid
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Merge two halves
        left = head
        right = prev
        while left and right:
            left_next = left.next
            right_next = right.next
            
            left.next = right
            right.next = left_next
            
            left = left_next
            right = right_next
        
        self.printList(head)

    def printList(self, node):
        res = []
        while node:
            res.append(node.val)
            node = node.next
        print(res)
