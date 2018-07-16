class BstNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    head = None
    
    def insert(self, data):
        if not self.head:
            self.head = QueueNode(data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = QueueNode(data)
        return

    def pop(self):
        if not self.head:
            return None
        temp = self.head
        self.head = self.head.next
        return temp


class Bst:
    head = None
    inorderlist = []
    def __init__(self, data = None):
        if data:
            self.head = BstNode(data)

    def insert(self, data, curr = None, arr = None):
        self.insertstart(data, curr)
        self.balancetree(arr)

    def insertstart(self, data, curr = None):
        node = BstNode(data)
        if (self.head == None):
            self.head = node
            return
        if (curr == None):
            return node
        if (node.data < curr.data):
            curr.left = self.insertstart(data, curr.left)
            pass
        if (node.data > curr.data):
            curr.right = self.insertstart(data, curr.right)
            pass
        return curr

    def findmin(self, curr = None):
        if not curr:
            curr = self.head
        while curr.left:
            curr = curr.left
        return(curr)

    def findmax(self, curr = None):
        if not curr:
            curr = self.head
        while curr.right:
            curr = curr.right
        return(curr)

    def findheight(self, curr):
        height = -1
        if not curr:
            return height
        return 1 + max(self.findheight(curr.left), self.findheight(curr.right))

    def bfs(self):
        if not self.head:
            print('Empty tree.')
            return
        newqueue = Queue()
        newqueue.insert(self.head)
        curr = newqueue.head
        while curr:
            temp = newqueue.pop()
            print(temp.data.data)
            if temp.data.left:
                newqueue.insert(temp.data.left)
            if temp.data.right:
                newqueue.insert(temp.data.right)
            curr = newqueue.head

    def preorder(self, curr):
        if not curr:
            return
        print(curr.data, end = ' ')
        self.preorder(curr.left)
        self.preorder(curr.right)

    def postorder(self, curr):
        if not curr:
            return
        self.postorder(curr.left)
        self.postorder(curr.right)
        print(curr.data, end = ' ')
    
    def inorder(self, curr):
        if not curr:
            return
        self.inorder(curr.left)
        print(curr.data, end = ' ')
        self.inorderlist += [curr.data] #created only for checkifbst function
        self.inorder(curr.right)
    
    def checkifbst(self):
        if not len(self.inorderlist):
            print('executed')
            self.inorder(self.head)
        if self.inorderlist == sorted(self.inorderlist):
            print('\nGiven tree is BST.')
        else:
            print('\nGiven tree is not a BST.')

    def balancetree(self, arr):
        if not arr:
            return
        mid = int(len(arr)/2)
        curr = BstNode(arr[mid])
        curr.left = self.balancetree(arr[:mid])
        curr.right = self.balancetree(arr[mid+1:])
        if len(arr) == len(self.inorderlist):
            self.head = curr
        return curr

    def delete(self, data, curr):
        if not self.head:
            print('Tree is Empty.')
            return
        if not curr:
            print('Not found')
            return
        if (data < curr.data):
            curr.left = self.delete(data, curr.left)
            return curr
        elif (data > curr.data):
            curr.right = self.delete(data, curr.right)
            return curr
        else:
            if not curr.right and not curr.left:
                curr = None
                if self.head.data == data and not self.head.left and not self.head.right:
                    self.head = curr
            elif not curr.right:
                temp = curr
                curr = curr.left
                if temp == self.head:
                    self.head = curr
                del temp
            elif not curr.left:
                temp = curr
                curr = curr.right
                if temp == self.head:
                    self.head = curr
                del temp
            else:
                temp = self.findmin(curr.right)
                curr.data = temp.data
                curr.right = self.delete(temp.data, curr.right)
            return curr
        
    def showTree(self, curr):
        if not curr:
            return
        print (curr.data, end = ' ')
        if curr.right:
            print ('', end= ' ')
            self.showTree(curr.right)
        if curr.left:
            print ('', end = ' ')
            self.showTree(curr.left)


def testcases():
    print('tree 1 starts:')
    tre1 = Bst(123)
    tre1.insert(1232, tre1.head)
    tre1.insert(111, tre1.head)
    tre1.insert(1231, tre1.head)
    tre1.showTree(tre1.head)
    print('tree 1 works', end = '\n\n\n\n')

    print('tree 2 starts: ')
    tre2 = Bst()
    tre2.insert(123, tre2.head)
    tre2.insert(122, tre2.head)
    tre2.insert(121, tre2.head)
    tre2.insert(1233, tre2.head)
    tre2.insert(1232,tre2.head)
    tre2.checkifbst()
    tre2.showTree(tre2.head)
    pass
    print('tree 2 works:')


    tre3 = Bst(15)
    ip_array = [20, 10, 8, 12, 17, 25]
    for element in ip_array:
        tre3.insert(element, tre3.head)
    tre3.showTree(tre3.head)
    print('The max value is:', tre3.findmax().data)
    print('The min value is:', tre3.findmin().data)
    print(tre3.findheight(tre3.head))

    tre4 = Bst(8)
    tre4.insert(3, tre4.head)
    tre4.insert(1, tre4.head)
    tre4.insert(6, tre4.head)
    tre4.insert(4, tre4.head)
    tre4.insert(7, tre4.head)
    tre4.insert(10, tre4.head)
    tre4.insert(14, tre4.head)
    tre4.insert(13, tre4.head)
    print(tre4.findheight(tre4.head))
    tre4.showTree(tre4.head)
    tre4.bfs()

    tre5 = Bst()
    tre5.bfs()

    tre6 = Bst('F')
    tre6.insert('D', tre6.head)
    tre6.insert('J', tre6.head)
    tre6.insert('B', tre6.head)
    tre6.insert('E', tre6.head)
    tre6.insert('G', tre6.head)
    tre6.insert('K', tre6.head)
    tre6.insert('A', tre6.head)
    tre6.insert('C', tre6.head)
    tre6.insert('I', tre6.head)
    tre6.bfs()
    print('preorder is: ', end = '')
    tre6.preorder(tre6.head)
    print('\npostorder is: ', end = '')
    tre6.postorder(tre6.head)
    print('\ninorder is: ', end = '')
    tre6.inorder(tre6.head)

    tre7 = Bst(12)
    tre7.insert(5, tre7.head)
    tre7.insert(3, tre7.head)
    tre7.insert(7, tre7.head)
    tre7.insert(15, tre7.head)
    tre7.insert(17, tre7.head)
    tre7.insert(19, tre7.head)
    tre7.insert(13, tre7.head)
    tre7.insert(1, tre7.head)
    tre7.insert(9, tre7.head)
    tre7.inorder(tre7.head)

    tre8 = Bst(10)
    iplist = [5, 15, 4, 2, 1, 3, 8, 7, 6, 9, 13, 12, 17, 11, 18, 19, 14, 16, 20, 0]
    for each in iplist:
        tre8.insert(each, tre8.head)
    tre8.inorder(tre8.head)
    ip = 1
    while True:
        try:
            ip = int(input('\nEnter number to be deleted: '))
        except ValueError:
            break
        tre8.delete(ip, tre8.head)
        print('\n')
        tre8.inorder(tre8.head)
    print('showing tree: ')
    tre8.showTree(tre8.head)
    print('\n')
    tre8.balancetree(tre8.inorderlist)
    tre8.showTree(tre8.head)

    tre9 = Bst(10)
    tre9.delete(10, tre9.head)
    tre9.showTree(tre9.head)

    tre10 = Bst(100)
    tre10.insert(50, tre10.head)
    tre10.inorder(tre10.head)
    tre10.delete(100, tre10.head)
    tre10.inorder(tre10.head)
    tre10.showTree(tre10.head)
    pass


testcases()
print('\nworks.')