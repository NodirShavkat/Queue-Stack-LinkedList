from queues import LinkedList, Stack, Queue

# LinkedList
ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)

ll.show()

ll.delete(30)
ll.show()


#1 Stack 
my_stack = Stack()

print(my_stack.is_empty())

my_stack.push(10)
my_stack.push(20)
my_stack.push(30)

print(my_stack.is_empty())

print(my_stack.peek())

my_stack.pop()
print(my_stack.peek())

print(my_stack.size())

#2 Stack
browser_storage = Stack()

browser_storage.push('get/users/')
browser_storage.push('get/1/detail/')
browser_storage.push('get/orders/')
browser_storage.push('get/products')

print(browser_storage.peek())

browser_storage.pop()
browser_storage.pop()

print(browser_storage.peek())


#1 Queue
q = Queue()

q.enqueue('A')
q.enqueue('B')
q.enqueue('C')

q.dequeu()

print(q.front())

#2 Queue
print_service = Queue()

print_service.enqueue('django_by_4_exampless.pdf')
print_service.enqueue('user_info.docx')
print_service.enqueue('example.txt')

print_service.dequeu()

print(print_service.front())
