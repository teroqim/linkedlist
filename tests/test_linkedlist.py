from linkedlist import LinkedList 

class TestLinkedList:

    def test_init(self):
        '''There are no front or back in a newly initialized list'''
        linked_list = LinkedList()
        assert linked_list.get_front() == None
        assert linked_list.get_back() == None

    def test_add_to_empty_list(self):
        '''
        Adding an element to an empty list means back and front is 
        that element.
        '''
        linked_list = LinkedList()
        item = 12
        linked_list.add_to_back(item)
        assert linked_list.get_back().obj == item
        assert linked_list.get_front().obj == item
        
        linked_list = LinkedList()
        item = 18
        linked_list.add_to_front(item)
        assert linked_list.get_back().obj == item
        assert linked_list.get_front().obj == item

    def test_last_item_point_to_none(self):
        '''Item at the back has None as next pointer'''
        linked_list = LinkedList()
        linked_list.add_to_back(0)
        assert linked_list.get_back().next == None
        linked_list.add_to_back(123)
        assert linked_list.get_back().next == None

    def test_prev_from_front_is_none(self):
        '''Item at the front has None as prev pointer'''
        linked_list = LinkedList()
        linked_list.add_to_front(0)
        assert linked_list.get_front().prev == None
        linked_list.add_to_front(123)
        assert linked_list.get_front().prev == None

    def test_remove(self):
        '''Removing item brings adjacent items together'''
        linked_list = LinkedList()
        item1 = 141
        item2 = 123
        item3 = 552
        linked_list.add_to_back(item1)
        linked_list.add_to_back(item2)
        linked_list.add_to_back(item3)
        front = linked_list.get_front()
        back = linked_list.get_back()
        middle = front.next
        assert front.next.obj == back.prev.obj
        linked_list.remove(middle)
        assert front.next.obj == back.obj
        assert back.prev.obj == front.obj

    def test_add_to_back_next(self):
        '''Adding to back makes previous back item the item before the new
        back'''
        linked_list = LinkedList()
        item1 = 123
        item2 = 1233
        linked_list.add_to_back(item1)
        linked_list.add_to_back(item2)
        assert linked_list.get_back().prev.obj == item1
        assert linked_list.get_back().prev.next.obj == item2

    def test_add_to_front_prev(self):
        '''Add to front places previous front after the new front'''
        linked_list = LinkedList()
        item1 = 123
        item2 = 1233
        linked_list.add_to_front(item1)
        linked_list.add_to_front(item2)
        assert linked_list.get_front().next.obj == item1
        assert linked_list.get_front().next.prev.obj == item2
