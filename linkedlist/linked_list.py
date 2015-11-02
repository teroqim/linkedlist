import weakref

class _LinkedListItem(object):
    def __init__(self, obj, prev, next, parent):
        self.prev = prev
        self.next = next
        self.obj = obj
        self.parent = weakref.ref(parent)

#Ideas for new methods: find_first, find_last, insert_after
class LinkedList(object):
    '''General purpose double-linked linked list.'''

    def __init__(self):
        self.front = None
        self.back = None
        self.length = 0

    def add_to_back(self, obj):
        '''Append item to back of list. O(1)'''
        item = _LinkedListItem(obj, self.back, None, self)
        if self.back:
            self.back.next = item

        self.back = item

        if not self.front:
            self.front = item
        
        self.length += 1

        return item

    def remove(self, item):
        '''Remove item from list. O(1)'''
        if not isinstance(item, _LinkedListItem):
            raise Exception('item must be of class _LinkedListItem')
        if item.parent() != self:
            raise Exception('item does not belong to this list and cannot be removed')

        if item.prev:
            item.prev.next = item.next
        else:
            #no prev means it is the front
            self.front = item.next
        if item.next:
            item.next.prev = item.prev
        else:
            #no next means it is the back
            self.back = item.prev
        item.parent = None
        if not (item.prev or item.next):
            self.front = self.back = None
            self.length = 0
        else:
            self.length -= 1

    def add_to_front(self, obj):
        '''Add item to front of list. O(1)'''
        item = _LinkedListItem(obj, None, self.front, self)
        if self.front:
            self.front.prev = item
        self.front = item 
        if not self.back:
            self.back = item
        self.length += 1 
        return item

    def get_front(self):
        '''Returns the item at the front of the list. None of list is empty. O(1)'''
        return self.front 

    def get_back(self):
        '''Returns item at the back of the list, None if list is empty. O(1)'''
        return self.back 
