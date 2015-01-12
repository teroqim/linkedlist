
class LinkedListItem(object):
    def __init__(self, obj, prev, next):
        self.prev = prev
        self.next = next
        self.obj = obj


class LinkedList(object):
    '''General purpose linked list.'''

    def __init__(self):
        self.front = None
        self.back = None

    def add_to_back(self, obj):
        '''Append item to back of list'''
        item = LinkedListItem(obj, self.back, None)
        if self.back:
            self.back.next = item

        self.back = item

        if not self.front:
            self.front = item

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
            self.front = self.back = None

    def add_to_front(self, obj):
        '''Add item to front of list'''
        item = LinkedListItem(obj, None, self.front)
        if self.front:
            self.front.prev = item
        self.front = item 
        if not self.back:
            self.back = item
        
        return item

    def get_front(self):
        '''Returns the item at the front of the list. None of list is empty.'''
        return self.front 

    def get_back(self):
        '''Returns item at the back of the list, None if list is empty.'''
        return self.back 
