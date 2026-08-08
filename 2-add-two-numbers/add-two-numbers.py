# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Loop continues if l1 has nodes, l2 has nodes, or a carry remains
        while l1 or l2 or carry:
            # Extract values; use 0 if a list has already ended
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate total sum of the current digits and the carry
            total = val1 + val2 + carry
            carry = total // 10  # Finds the new carry (e.g., 12 // 10 = 1)
            digit = total % 10   # Finds the value for the node (e.g., 12 % 10 = 2)
            
            # Create a new node with the single digit and link it
            current.next = ListNode(digit)
            current = current.next
            
            # Move to the next nodes in the input lists if they exist
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        # Return the actual head of the list, skipping the initial dummy node
        return dummy.next
