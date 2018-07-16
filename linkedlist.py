def oldcode():
	# class Node:
	# 	def __init__(self, data):
	# 		self.data = data
	# 		self.next = None
	# 		self.old = None


	# class LinkedList:
	# 	def add(self, head, data):
	# 		node = Node(data)
	# 		if (head == None):
	# 			return node
	# 		curr = head
	# 		while curr.next:
	# 			curr = curr.next
	# 		curr.next = node
	# 		node.old = curr
	# 		return head
	# 	def insertAt(self, head, index, data):
	# 		node = Node(data)
	# 		if (index == 0):
	# 			node.next = head
	# 			return node
	# 		curr = head
	# 		while index:
	# 			index = index - 1
	# 			if (curr.next):
	# 				if (index == 0):
	# 					node.next = curr
	# 					node.old = curr.old
	# 					curr.old.next = node
	# 					curr.old = node
	# 				curr = curr.next
	# 			else:
	# 				print ('Index out of range lol')
	# 				break
	# 		return head

	# 	def reverseList(self, head):
	# 		curr = head
	# 		temp = None
	# 		prev = None
	# 		while (curr):
	# 			temp = curr.next
	# 			curr.next = prev
	# 			prev = curr
	# 			curr = temp
	# 		return prev

	# 	def printList(self, head):
	# 		if (head == None):
	# 			print ('Empty list.')
	# 			return
	# 		curr = head
	# 		while (curr):
	# 			print (curr.data, end = ' ')
	# 			curr = curr.next
	# 		print ()
	# n = int(input('Enter no. of elements: '))
	# newList = LinkedList()
	# head = None
	# for _ in range(n):
	# 	head = newList.add(head, int(input()))

	# newList.printList(head)

	# n = int(input('Enter value to be inserted: '))
	# ind = int(input('Enter index: '))
	# head = newList.insertAt(head, ind, n)
	# newList.printList(head)
	# head = newList.reverseList(head)
	# newList.printList(head)
	pass

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList(object):

	def __init__(self):
	    """
	    Initialize your data structure here.
	    """
	    self.head = None
	    self.size = 0

	def get(self, index):
	    """
	    Get the value of the index-th node in the linked list. If the index is invalid, return -1.
	    :type index: int
	    :rtype: int
	    """
	    if index not in range(self.size):
	        return -1
	    curr = self.head
	    if not self.head:
	        return -1
	    while index:
	        if curr.next:
	            curr = curr.next
	        else:
	            return -1
	        index -= 1
	    return curr.data
        
	def addAtHead(self, val):
	    """
	    Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
	    :type val: int
	    :rtype: void
	    """
	    newnode = Node(val)
	    newnode.next = self.head
	    self.head = newnode
	    self.size += 1
	    return
        
	def addAtTail(self, val):
	    """
	    Append a node of value val to the last element of the linked list.
	    :type val: int
	    :rtype: void
	    """
	    newnode = Node(val)
	    curr = self.head
	    if not curr:
	        self.head = newnode
	        return
	    while curr.next:
	        curr = curr.next
	    self.size += 1
	    curr.next = newnode

	def addAtIndex(self, index, val):
	    """
	    Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
	    :type index: int
	    :type val: int
	    :rtype: void
	    """
	    if not index:
	        self.addAtHead(val)
	        return
	    curr = self.head
	    if not curr:
	        return
	    while index-1:
	        if curr.next:
	            curr = curr.next
	        else:
	            return
	        index -= 1
	    newnode = Node(val)
	    newnode.next = curr.next
	    curr.next = newnode
	    self.size += 1
	    return
        
	def deleteAtIndex(self, index):
	    """
	    Delete the index-th node in the linked list, if the index is valid.
	    :type index: int
	    :rtype: void
	    """
	    curr = self.head
	    if not curr:
	        return
	    if not index:
	        self.size -= 1
	        self.head = self.head.next
	        return
	    while index-1:
	        if curr.next:
	            curr = curr.next
	        else:
	            return
	        index -= 1
	    if not curr.next:
	        return
	    curr.next = curr.next.next
	    self.size -= 1
	    return

	def reverseList(self):
		# lis = []
		# curr = self.head
		# while curr:
		# 	lis.append(curr.data)
		# 	curr = curr.next
		# self.head = Node(lis.pop())
		# while lis:
		# 	newnode = Node(lis.pop())
		# 	curr = self.head
		# 	while curr.next:
		# 		curr = curr.next
		# 	curr.next = newnode
		# pass
		if not self.head:
			return None
		curr = self.head
		while curr.next:
			temp = curr.next
			curr.next = temp.next
			temp.next = self.head
			self.head = temp

	def show(self):
		curr = self.head
		while curr:
			print(curr.data)
			curr = curr.next

	def detectCycle(self):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		slow = fast = self.head
		if not self.head:
			 return None
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			if fast == slow:
				slo = self.head
				while True:
					if slow == slo:
						return slow
					slo = slo.next
					slow = slow.next
		return None

	def removeElements(self, val):
		if not self.head:
			return None
		while self.head and self.head.data == val:
			self.head = self.head.next
		curr = self.head
		if not curr:
			return None
		while curr and curr.next:
			if curr.next.data == val:
				curr.next = curr.next.next
			else:
				curr =  curr.next
		

print('works.')
lis = [2, 2, 3, 1, 2, 2, 1]
# for each in range(1, 6):
# 	lis.append(each)
# 	lis.append(6)
ll = MyLinkedList()
for each in lis:
	ll.addAtTail(each)
ll.show()
print('now removing.')
ll.removeElements(2)
ip = input('enter input')
print(ip)
ip2 = input('enter input again')
print(ip2)
ll.show()

