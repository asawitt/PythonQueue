class QueueNode:
	def __init__(self,value):
		self.next = None
		self.value = value

class Queue:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size.length = 0
	def push(self,value): #Enqueue
		if self.head is None:
			self.head = self.tail = QueueNode(value)
			self.size = 1
		else:
			self.tail.next = QueueNode(value)
			self.tail = self.tail.next
			self.size += 1
	def pop(self): #Dequeue
		if self.head is None:
			return None
		val = self.head.value
		self.head = self.head.next
		self.size -= 1
		return val
	def peek(self):
		if self.head is None:
			return None
		return self.head.value
	def display(self):
		cur = self.head
		print("[",end="")
		while cur is not None: 
			if cur.next is None:
				print(cur.value,end="")
			else:
				print(cur.value,end="<--")
			cur = cur.next
		print("]")

	def isEmpty(self):
		if self.head is None:
			return True
		return False

	def getSize(self):
		return self.size

	def find(self,value):
		cur = self.head
		while cur is not None:
			if cur.value == value:
				return True
			cur = cur.next
		return False
