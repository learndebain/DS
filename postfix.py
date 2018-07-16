class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        self.head = Node(None)
    
    def push(self, data):
        node = Node(data)
        if (self.head.data == None):
            self.head = node
            return
        node.next = self.head
        self.head = node
    
    def isEmpty(self):
        if (self.head == None):
            return True
        return False

    def pop(self):
        if (self.head == None):
            print ('Empty stack.')
            return 
        data = self.head.data
        self.head = self.head.next
        return data

    def show(self):
        curr = self.head
        while (curr):
            print (curr.data)
            curr = curr.next
        print ('Done priniting.')


# cars = Stack()
# cars.push(1)
# cars.push(2)
# cars.push(3)
# cars.show()
# data = True
# while data:
#     data = cars.pop()
#     print (data) 

cars = Stack()
cars.push('start')
exp = input('Enter expression: ')
ans = 0
for i in range(len(exp)):
    data = exp[i]
    if data in ['*', '/', '+', '-']:
        op2 = str(cars.pop())
        # print ('op1 ', op2)
        op1 = str(cars.pop())
        # print('op2 ', op1)
        result = op1 + data + op2
        # print (result)
        ans = eval(result)
        # print(ans)
        cars.push(ans)
    else:
    #     print ('pushing', data)
        cars.push(data)
    #     print('stack is ')
    #     cars.show()
    
cars.show()
