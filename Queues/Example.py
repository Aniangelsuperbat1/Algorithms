# -Sequential data structure that follows the FIFO methodology. First in,   First out.
# -First element added to the Queue will always be the first one removed
# -Add element to the back of the stack, called the tail
# -Remove elements from the front, called the head
# -Common Methods:
# 	-EnQueue: Enqueue(Object). Adds an object to tail end of Queue. 
# 	-Dequeue: Dequeue(). Removes elements from Queue from head of queue.
# 	-Peek: Peek(). Returns the object that is at the forefront of the Queue.
# 	-Contains: Contains(). Returns weather or not queue contains an object. Returns true or false. 

# Accessing: O(N). If you want element at the front, first must dequeue entire queue of elements
# Searching: O(N). Must search every element to find what you are looking for.
# Inserting: O(1). Always adds elements from the tail of Queue. Only very Enqueueing at a single point.
# Deleting: O(1). Always deletes elements from head of Queue. Only ever Dequeueing at a single point.
# Uses:
# 	-Job scheduling in computers. Which task is to be completed and when
# 	-Printer Queues. Whos documents are printed first.
