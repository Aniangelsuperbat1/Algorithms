# Linked List:
# -Sequential data structure in which every element is a separate object called a Node , which has two parts. Each node has two separate pieces of information.
# 	-The data
# 	-The reference(or pointer node) which points to the next node on the list
# -Every linked list starts with a head node
# -Every Linked list ends with a tail node that reference pointer is equal to Null
# Data can flow in and out of any point in a linked List
# -Adding a node to head of linked List
# 	-Make new Node’s pointer point to the current head of the linked List
# -Removing a node from head of linked list
# 	-Set the head node’s pointer to a Null value 
# -Inserting a node in the middle of a Linked List: Two step process
# 	1. Make the pointer of the new Node point to the node after the location we want to insert at
# 	2. Set the Node before the location we want to insert at to point towards the new Node
# -Remove a node from the middle of a linked list:
# -Make the pointer of the node previous to the one we are removing, to now point the node after the one we are removing
# -Inserting at the end/tail of the linked list:
# 	-Only modify last/tail node
# -Make the current tail point towards the new node you want to add and make the reference/pointer node point to Null
# -Deleting at end/tail node of a linked list:
# 	-Set the previous tail to point towards a null value instead of the current tail

# Accessing: O(n). Must go through each node before finding element you want 
# Searching: O(n).  Must go through each node before finding element you want
# Inserting: If inserting at head or tail of linked list = O(1). If inserting in middle of linked List = O(n)
# Deleting: If deleting at head of linked list = O(1). If deleting at middle of linked list = O(n)
# Uses: Music list. Photo list
# One big drawback: Only ever go forward with pointers, cant not go backwards.


class singly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None 

new_list = singly_linked_list()
node1 = Node(1)
node2 = Node(2)

new_list.head = node1
new_list.next = node2
new_list.tail = node2