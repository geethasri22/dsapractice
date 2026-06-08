class Solution:
    def compute(self, head):
        # Reverse the linked list
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        head = prev

        # Traverse reversed list and remove smaller nodes
        max_val = head.data
        curr = head
        while curr and curr.next:
            if curr.next.data < max_val:
                curr.next = curr.next.next
            else:
                curr = curr.next
                max_val = curr.data

        # Reverse again to restore original order
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
