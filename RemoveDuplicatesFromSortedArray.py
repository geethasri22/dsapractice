# Definition for singly-linked list.
# Each node has a value (val) and a pointer to the next node (next).
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        # start with the head of the linked list
        actuel = head

        # traverse the list until we reach the end
        while actuel != None and actuel.next != None:
            # If the current node and the next node have the same value
            if actuel.val == actuel.next.val:
                # Skip the duplicate by linking to the node after next
                actuel.next = actuel.next.next
            else:
                # Otherwise, move forward to the next node
                actuel = actuel.next

        # Return the modified head (list without duplicates)
        return head
