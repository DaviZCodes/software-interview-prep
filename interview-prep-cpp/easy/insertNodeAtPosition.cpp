/*
Author: Davi Zheng
Question: Given a SinglyLinkedList, we are given an int which we want to add to our data
 and a position in the linked list we want to add.
 We do not have to define all other functions such as create linked list and node.

 Example:
 Given linked list: 1 -> 2 -> 3
 We want to add data 6 on position 2. So it ends up as:
 1 -> 2 -> 6 -> 3

 We return the altered linked list. Keep in mind the comments are based on the given example above.
 */

#include <iostream>

linkedListNode* insertNodeAtPosition(linkedListNode* headPtr, int data, int position){
    linkedListNode* new_node = new linkedListNode(data); //create Node pointer
    linkedListNode* curr = headPtr; //create a curr/temp for where we are pointing at the linked list

    //base case
    if (headPtr == nullptr){
        return headPtr;
    }

    //create a variable which determine how many times we must write head = headPtr->next
    int i = 0;
    while (i < position - 1){ //we use position -1 because ->next is basically +1
        curr = curr->next;
        ++i;
    } //after the while loop curr can insert the position at the correct place, 2 in this case

    new_node->next = curr->next; //we are adding the elements after curr in the linked list (3) to node 6,
                                // so new_node will then be 6 -> 3 based on given example
    curr->next = new_node; // we are now adding 6 -> 3 to previous elements of linked list (1 -> 2),
                          // so headPtr will then be  1 -> 2 -> 6 -> 3
    return headPtr; //the linked list is then altered and then will be returned
}


