from linkedlist import LinkedList

ll = LinkedList()

# Add items to either the front or the back
ll.add_to_front(12)
ll.add_to_front(14)
ll.add_to_back(16)
ll.add_to_back(15)

# Retrieve front and back
front = ll.get_front()
back = ll.get_back()

# Output: '14'
print front.obj

# Output: '15'
print back.obj

# Output: '12'
print front.next.obj

# Output: '16'
print back.prev.obj

# Remove item
ll.remove(front.next)

# Output: '16'
print front.next.obj

