# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        The solution is to create a slow and fast pointer.
        The fast pointer is 2x faster than the slow pointer.
        Thus, when the fast pointer reaches the end, the 
        slow pointer is at the middle node.
        '''

        slow_pointer = head
        fast_pointer = head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        
        return slow_pointer

        '''
        # previous solution:
        if not head:
            return head
        
        curr = head
        len_list = 0

        while curr:
            len_list += 1
            curr = curr.next
        
        middle_node = ceil((len_list + 1)/2)

        curr2 = head
        index = 0
        while curr2:
            index += 1
            if index == middle_node:
                return curr2
            
            curr2 = curr2.next'''

        
