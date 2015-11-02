import pytest
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

    def test_add_to_empty_back_gives_new_front(self):
        '''Adding an item to the back of an empty list also creates a front
        that is equal to the back item'''
        ll = LinkedList()
        item = 1235
        ll.add_to_back(item)
        assert ll.get_back().obj == item
        assert ll.get_front().obj == item
        assert ll.get_front() == ll.get_back()

    def test_add_to_empty_front_gives_new_back(self):
        '''Adding an item to the front of an empty list also creates a back
        that is equal to the front item'''
        ll = LinkedList()
        item = 1235
        ll.add_to_front(item)
        assert ll.get_front().obj == item
        assert ll.get_back().obj == item
        assert ll.get_front() == ll.get_back()

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

    def test_add_back_appends_item(self):
        '''Adding to the back of the list multiple times does not remove items.
        Instead the list is appended with the new item'''
        linked_list = LinkedList()
        linked_list.add_to_back(12)
        linked_list.add_to_back(14)
        assert linked_list.get_back().obj == 14
        assert linked_list.get_back().prev.obj == 12

    def test_add_front_prepends_item(self):
        '''Adding to the front of the list multiple times does not remove items.
        Instead the list is prepended with the new item'''
        linked_list = LinkedList()
        linked_list.add_to_front(12)
        linked_list.add_to_front(14)
        assert linked_list.get_front().obj == 14
        assert linked_list.get_front().next.obj == 12

    def test_add_front_multiple_equal_items(self):
        '''Adding the same item to the front of the list multiple times creates
        different linked list objects with the same item'''
        linked_list = LinkedList()
        linked_list.add_to_front(12)
        linked_list.add_to_front(12)
        assert linked_list.get_front().obj == linked_list.get_front().next.obj 
        assert linked_list.get_front() != linked_list.get_front().next 

    def test_add_back_multiple_equal_items(self):
        '''Adding the same item to the back of the list multiple times creates
        different linked list objects with the same item'''
        linked_list = LinkedList()
        linked_list.add_to_back(12)
        linked_list.add_to_back(12)
        assert linked_list.get_back().obj == linked_list.get_back().prev.obj 
        assert linked_list.get_back() != linked_list.get_back().prev 

    def test_remove(self):
        '''Removing an item brings adjacent items together'''
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
        linked_list.remove(middle)
        assert front.next == back
        assert back.prev == front

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

    def test_empty_list_has_0_lenght(self):
        linked_list = LinkedList()
        assert linked_list.length == 0

    def test_non_empty_list_has_length(self):
        linked_list = LinkedList()
        item1 = 123
        item2 = 34234
        item3 = 1212
        linked_list.add_to_front(item1)
        assert linked_list.length == 1
        linked_list.add_to_back(item2)
        assert linked_list.length == 2
        linked_list.add_to_front(item3)
        assert linked_list.length == 3

    def test_removing_items_reduces_length(self):
        linked_list = LinkedList()
        assert linked_list.length == 0
        linked_list.add_to_front(123)
        linked_list.add_to_front(12312)
        assert linked_list.length == 2
        item = linked_list.get_front()
        linked_list.remove(item)
        assert linked_list.length == 1
        item = linked_list.get_front()
        linked_list.remove(item)
        assert linked_list.length == 0

    def test_can_only_remove_items_from_own_list(self):
        with pytest.raises(Exception):
            linked_list = LinkedList()
            linked_list2 = LinkedList()
            item = 123123123
            linked_list.add_to_front(item)
            list_item = linked_list.get_front()
            linked_list2.remove(list_item)

    def test_removed_item_has_no_parent(self):
        '''Removing an item also removes any references from the item to the 
        list'''
        ll = LinkedList()
        item = list()
        litem = ll.add_to_back(item)
        assert litem.parent()
        ll.remove(litem)
        assert litem.parent == None

    def test_cannot_remove_item_twice(self):
        '''It is not possible to remove an item that has already been removed
        and not been processed in any way after being removed'''
        ll = LinkedList()
        obj = dict()
        item = ll.add_to_front(obj)
        ll.remove(item)
        with pytest.raises(Exception):
            ll.remove(item)

    def test_remove_updates_head_if_necessary(self):
        '''Removing head, updates head''' 
        ll = LinkedList()
        obj = 1234
        obj2 = list()
        item1 = ll.add_to_front(obj)
        item2 = ll.add_to_front(obj2)
        assert ll.get_front() == item2
        ll.remove(item2)
        assert ll.get_front() == item1

    def test_remove_updates_back_if_necessary(self):
        '''Removing back updates back'''
        ll = LinkedList()
        obj = 1234
        obj2 = list()
        item1 = ll.add_to_back(obj)
        item2 = ll.add_to_back(obj2)
        assert ll.get_back() == item2
        ll.remove(item2)
        assert ll.get_back() == item1

    def test_remove_all_items_deletes_front_and_back(self):
        ll = LinkedList()
        obj = 1234
        obj2 = list()
        item1 = ll.add_to_back(obj)
        item2 = ll.add_to_back(obj2)
        ll.remove(item2)
        ll.remove(item1)
        assert ll.get_front() == None
        assert ll.get_back() == None

