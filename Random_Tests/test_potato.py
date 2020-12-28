# Difference between a Thread and a Process?

# What is the difference between a Tuple and a List?

# What is a linked list?

# What is garbage collection?

# Which of the following are mutable ? int, string, list, dictionaries, float

# What is a hashtable? 

# What is a memory leak?

# What is the normal process of development from your experience?

# Can you tell me about your project?

# Which ubuntu commands do you know?

# Can you tell me the complexity of the following code :

# l0 is of length k
# l1 is of length n
# l2 is of length m
#

# O(k*(n+m/2))


        





# Create a FIFO class which we can initialize with a list.
# It has two methods add and get. 


# Create a FILO class which we can initialize with a list.
# It has two methods add and get. 

class FILO:
    def __init__(self, l=[]):
        self.l = l
    def add(self, value):
        self.l.append(value)
    def get(self):
        return self.l.pop()



# Create a singly linked list class. Tip : create a node class first and then a 
# linked list class that will use the node class.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = None

A = ListNode(0)
A.next = ListNode(1)

class SinglyLinkedList:
    def __init__(self, l = []):
        self.l = l
        self.head = ListNode()
        self.addNode()
        
    def addNode(self):
        head = ListNode()
        node = head
        while len(self.l) != 0:
            val = self.l.pop(0)
            node.next = ListNode(val)
            node = node.next
        self.head = head.next

SLL = SinglyLinkedList([1,2,3])

print(SLL.head.val)

# reverse a singly linked list



# reverse a string 

s = 'abcdefgh'
q = list(s)
q.reverse()
q1 = ''.join(q)
print(q1)

s = s[::-1]
print(s)

# check if a string contains repetive characters

s = 'abcdefagaaaasaad'

def repetiveChars(s):
    res = []
    for i in range(0, len(s)-1):
        if s[i] not in res:
            res.append(s[i])
    return ''.join(res)

print(repetiveChars(s))

# how can you find where two lists join each other?
