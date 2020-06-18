from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, list_val: List[int] =[], inp_h: ListNode = ListNode()):
        if not list_val:
            self.head = inp_h
        else:
            self.head = ListNode(list_val[0])
            iterator = self.head
            for i in range (1,len(list_val)):
                iterator.next = ListNode(list_val[i])
                iterator = iterator.next
    
    def __str__(self) -> str:
        s = ''
        h = self.head
        while h.next :
            s += '{} -> '.format(h.val)
            h = h.next
        s += str(h.val)
        return s

if __name__ == '__main__' :
    print(LinkedList([1,2,2,3]))