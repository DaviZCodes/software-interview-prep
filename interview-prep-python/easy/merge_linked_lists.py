'''
File: Merge Linked Lists
Author: DaviZCodes

Question (easy):
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list.
The list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''

def mergeLinkedList(list1, list2):
    #base cases
    if not list1 and not list2:
        return none
    if not list1:
        return list2
    if not list2:
        return list1

    #creating a current node, a dummy node which will be returned, and a first listnode

    #points to an empty node
    curr = dummy = ListNode(0)

    #while both exists
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        #increment current
        curr = curr.next

    #adding the remaining of list1 or list2
    if list1:
        curr.next = list1
    elif list2:
        curr.next = list2

    return dummy.next

'''
Keep in mind that this code cannot be implemented abstractly.
You need to use the ListNode and .val implementation for singly-linked list.
The thing is to set base cases, then while both lists exist, if value of list1 is smaller, 
the next current is the smaller list, then the smaller list points to next. 
The opposite occurs if value of list1 is bigger. Also, we return dummy.next value because only dummy
points to an empty node.
'''