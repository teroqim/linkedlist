
class LinkedListItem(object):
    def __init__(self, obj, prev, next):
        self.prev = prev
        self.next = next
        self.obj = obj



class LinkedList(object):
    '''General purpose linked list.'''

    def __init__(self):
        self.head = None
        self.tail = None

    def addToBack(self, obj):
        '''Append item to back of list'''
        item = LinkedListItem(obj, self.tail, None)
        self.tail = item

        if not self.head:
            self.head = item

        return item

    def remove(self, item):
        '''Remove item from list. '''
        if not isinstance(item, LinkedListItem):
            raise Exception('item must be of class LinkedListItem')
        if item.prev:
            item.prev.next = item.next
        if item.next:
            item.next.prev = item.prev
        if not (item.prev or item.next):
            self.head = self.tail = None

    def addToFront(self, obj):
        '''Add item to front of list'''
        item = LinkedListItem(obj, None, self.head)
        self.head = item 
        if not self.tail:
            self.tail = item
        
        return item

    def get_front(self):
        '''Returns the item at the front of the list. None of list is empty.'''
        return self.head 

    def get_back(self):
        '''Returns item at the back of the list, None if list is empty.'''
        return self.tail 
