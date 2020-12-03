# Stacks:
# Last in, first out. LIFO
# Append(): puts an item on top of stack
# pop(): takes an item off of stack
# peek(): lets you see an item on top of stack without removing it
# clear(): clears all items from stack
# Examples/use cases:
# Undo Command: track which commands have been executed. Pop last command off command stack to undo it.


class Stack:
    def __init__(self):
        self._data = []

    def push(self, data):
        self._data.append(data)

    def pop(self):
        return self._data.pop()

    def peek(self):
        return self._data[len(self._data) - 1]


stack = Stack()
stack.push(5)
print(stack.peek())
test = stack.pop()
print(test)
