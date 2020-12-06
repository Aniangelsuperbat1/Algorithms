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