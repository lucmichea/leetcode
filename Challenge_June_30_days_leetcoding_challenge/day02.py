"""
                Delete Node in a Linked List

Problem:

    Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

    Given linked list -- head = [4,5,1,9], which looks like following: 
     _____     _____     _____     _____
    |     |   |     |   |     |   |     |
    |  4  |-->|  5  |-->|  1  |-->|  9  |
    |_____|   |_____|   |_____|   |_____|

Example 1:

    Input: head = [4,5,1,9], node = 5
    Output: [4,1,9]
    Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

Example 2:

    Input: head = [4,5,1,9], node = 1
    Output: [4,5,9]
    Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function. 

Note:

    The linked list will have at least two elements.
    All of the nodes' values will be unique.
    The given node will not be the tail and it will always be a valid node of the linked list.
    Do not return anything from your function.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node : ListNode):
        while node.next:
            node.val = node.next.val
            if node.next.next :
                node = node.next
            else:
                node.next = None

    def deleteNodeHead(self, head: ListNode, node: int):
        """
        :type head: ListNode
        :type node: int, value of the node to delete
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if head.val == node:
            head = head.next
            return

        pointer = head
        while pointer.next:
            if pointer.next.val == node:
                pointer.next = pointer.next.next
                return
            pointer = pointer.next

                