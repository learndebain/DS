class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.myStack = Node(None)
        self.myQueue = Node(None)
    def pushC(self, ch):
        newNode = Node(ch)
        newNode.next = self.myStack
        self.myStack = newNode
    def traverse(self):
        while True:
            if (self.myQueue == None):
                break
            print (self.myQueue.data)
            self.myQueue = self.myQueue.next
    def popC(self):
        data = self.myStack.data
        self.myStack = self.myStack.next
        return(data)
    def enqueue(self, ch):
        newNode = Node(ch)
        if(self.myQueue.data == None):
            self.myQueue = newNode
            return
        copy = self.myQueue
        while True:
            if (copy.next == None):
                break
            copy = copy.next
        copy.next = newNode
        


obj = Stack()

obj.pushC(10)
obj.pushC(20)
obj.pushC(30)
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
obj.traverse()
print(obj.popC())
print(obj.popC())
print(obj.popC())
print(obj.popC())
obj.traverse()
