import pytest
from linkedlist import LinkedList

class TestLinkedList:

    def test_init(self):
        '''There are no front or back in a newly initialized list'''
        ll = LinkedList()
        assert ll.front == None
        assert ll.back == None

    def test_add_to_empty_list(self):
        '''
        Adding an element to an empty list means back and front is 
        that element.
        '''
        ll = LinkedList()
        key = 12
        value = "asd"
        ll.add_to_back(key, value)
        assert ll.back.key == key
        assert ll.front.key == key
        assert ll.back.value == value
        assert ll.front.value == value
        
        ll = LinkedList()
        key = 18
        value = "llk"
        ll.add_to_front(key, value)
        assert ll.back.key == key
        assert ll.front.key == key
        assert ll.back.value == value
        assert ll.front.value == value

    def test_add_to_empty_back_gives_new_front(self):
        '''Adding an item to the back of an empty list also creates a front
        that is equal to the back item'''
        ll = LinkedList()
        key = 12
        value = "asd"
        ll.add_to_back(key, value)
        assert ll.back.key == key
        assert ll.front.key == key
        assert ll.back.value == value
        assert ll.front.value == value
        assert ll.front == ll.back

    def test_add_to_empty_front_gives_new_back(self):
        '''Adding an item to the front of an empty list also creates a back
        that is equal to the front item'''
        ll = LinkedList()
        key = 12
        value = "asd"
        ll.add_to_front(key, value)
        assert ll.back.key == key
        assert ll.front.key == key
        assert ll.back.value == value
        assert ll.front.value == value
        assert ll.front == ll.back

    def test_last_item_point_to_none(self):
        '''Item at the back has None as next pointer'''
        ll = LinkedList()
        ll.add_to_back(0, 23)
        assert ll.back.next == None
        ll.add_to_back(123, 234)
        assert ll.back.next == None

    def test_prev_from_front_is_none(self):
        '''Item at the front has None as prev pointer'''
        ll = LinkedList()
        ll.add_to_front(0, 98)
        assert ll.front.prev == None
        ll.add_to_front(123, 98)
        assert ll.front.prev == None

    def test_add_back_appends_item(self):
        '''Adding to the back of the list multiple times does not remove items.
        Instead the list is appended with the new item'''
        ll = LinkedList()
        ll.add_to_back(12, 345)
        ll.add_to_back(14, 34)
        assert ll.back.key == 14
        assert ll.back.prev.key == 12

    def test_add_front_prepends_item(self):
        '''Adding to the front of the list multiple times does not remove items.
        Instead the list is prepended with the new item'''
        ll = LinkedList()
        ll.add_to_front(12, 54)
        ll.add_to_front(14, 98)
        assert ll.front.key == 14
        assert ll.front.next.key == 12

    def test_add_front_multiple_equal_items(self):
        '''Adding the same item to the front of the list multiple times creates
        different linked list objects with the same item'''
        ll = LinkedList()
        ll.add_to_front(12)
        ll.add_to_front(12)
        assert ll.front.key == ll.front.next.key 
        assert ll.front != ll.front.next 

    def test_add_back_multiple_equal_items(self):
        '''Adding the same item to the back of the list multiple times creates
        different linked list objects with the same item'''
        ll = LinkedList()
        ll.add_to_back(12)
        ll.add_to_back(12)
        assert ll.back.key == ll.back.prev.key 
        assert ll.back != ll.back.prev 

    def test_remove(self):
        '''Removing an item brings adjacent items together'''
        ll = LinkedList()
        key1 = 141
        key2 = 123
        key3 = 552
        ll.add_to_back(key1)
        ll.add_to_back(key2)
        ll.add_to_back(key3)
        front = ll.front
        back = ll.back
        middle = front.next
        ll.remove(middle)
        assert front.next == back
        assert back.prev == front

    def test_add_to_back_next(self):
        '''Adding to back makes previous back item the item before the new
        back'''
        ll = LinkedList()
        key1 = 123
        key2 = 1233
        ll.add_to_back(key1)
        ll.add_to_back(key2)
        assert ll.back.prev.key == key1
        assert ll.back.prev.next.key == key2

    def test_add_to_front_prev(self):
        '''Add to front places previous front after the new front'''
        ll = LinkedList()
        key1 = 123
        key2 = 1233
        ll.add_to_front(key1)
        ll.add_to_front(key2)
        assert ll.front.next.key == key1
        assert ll.front.next.prev.key == key2

    def test_empty_list_has_0_lenght(self):
        ll = LinkedList()
        assert ll.length == 0

    def test_non_empty_list_has_length(self):
        ll = LinkedList()
        ll.add_to_front(123)
        assert ll.length == 1
        ll.add_to_back(345)
        assert ll.length == 2
        ll.add_to_front(987)
        assert ll.length == 3

    def test_removing_items_reduces_length(self):
        ll = LinkedList()
        assert ll.length == 0
        ll.add_to_front(123)
        ll.add_to_front(12312)
        assert ll.length == 2
        item = ll.front
        ll.remove(item)
        assert ll.length == 1
        item = ll.front
        ll.remove(item)
        assert ll.length == 0

    def test_can_only_remove_items_from_own_list(self):
        with pytest.raises(Exception):
            ll = LinkedList()
            linked_list2 = LinkedList()
            ll.add_to_front(123)
            list_item = ll.front
            linked_list2.remove(list_item)

    def test_removed_item_has_no_parent(self):
        '''Removing an item also removes any references from the item to the 
        list'''
        ll = LinkedList()
        litem = ll.add_to_back(list())
        assert litem.parent()
        ll.remove(litem)
        assert litem.parent == None

    def test_cannot_remove_item_twice(self):
        '''It is not possible to remove an item that has already been removed
        and not been processed in any way after being removed'''
        ll = LinkedList()
        item = ll.add_to_front(dict())
        ll.remove(item)
        with pytest.raises(Exception):
            ll.remove(item)

    def test_remove_updates_head_if_necessary(self):
        '''Removing head, updates head''' 
        ll = LinkedList()
        item1 = ll.add_to_front(1234)
        item2 = ll.add_to_front(list())
        assert ll.front == item2
        ll.remove(item2)
        assert ll.front == item1

    def test_remove_updates_back_if_necessary(self):
        '''Removing back updates back'''
        ll = LinkedList()
        item1 = ll.add_to_back(123)
        item2 = ll.add_to_back("lkj")
        assert ll.back == item2
        ll.remove(item2)
        assert ll.back == item1

    def test_remove_all_items_deletes_front_and_back(self):
        ll = LinkedList()
        item1 = ll.add_to_back("lkjh")
        item2 = ll.add_to_back([1,2,3])
        ll.remove(item2)
        ll.remove(item1)
        assert ll.front == None
        assert ll.back == None

    def test_find_first_finds_first(self):
        ll = LinkedList()
        key = 123
        value1 = 441
        value2 = "sdsfgg"
        ll.add_to_front(key, value1)
        ll.add_to_front(key, value2)
        item = ll.find_first(key)
        assert item.value == value2

    def test_find_first_finds_nothing(self):
        ll = LinkedList()
        key = 123
        item = ll.find_first(key)
        assert item == None

    def test_find_last_finds_last(self):
        ll = LinkedList()
        key = 123
        value1 = 441
        value2 = "sdsfgg"
        ll.add_to_front(key, value1)
        ll.add_to_front(key, value2)
        item = ll.find_last(key)
        assert item.value == value1
        
    def test_find_last_finds_nothing(self):
        ll = LinkedList()
        key = 123
        item = ll.find_last(key)
        assert item == None

    #=============== insert_after ===========

    def test_insert_after_updates_back(self):
        ll = LinkedList()
        item1 = ll.add_to_front(5151, 91951)
        assert ll.back == item1
        item2 = ll.insert_after(item1, 123, 234)
        assert ll.back == item2

    def test_insert_after(self):
        ll = LinkedList()
        item1 = ll.add_to_front(5151, 91951)
        assert item1.next == None
        item2 = ll.insert_after(item1, 123, 234)
        assert item1.next == item2
        item3 = ll.insert_after(item1, 987234, "kjnsdfjn")
        assert item1.next == item3
        assert item3.next == item2
        assert item3.prev == item1
        assert item2.prev == item3

    def test_cannot_insert_after_None(self):
        ll = LinkedList()
        with pytest.raises(Exception):
            ll.insert_after(None, 123, 1414)

    def test_cannot_insert_after_item_from_other_list(self):
        ll = LinkedList()
        ll2 = LinkedList()
        item_from_ll = ll.add_to_front(123, 123)
        with pytest.raises(Exception):
            ll2.insert_after(item_from_ll, 123, 1414)

    def test_insert_after_updates_length(self):
        ll = LinkedList()
        item1 = ll.add_to_front(5151, 91951)
        assert ll.length == 1
        ll.insert_after(item1, 123, 234)
        assert ll.length == 2
        ll.insert_after(item1, 987234, "kjnsdfjn")
        assert ll.length == 3
            
    def test_insert_after_return_new_item(self):
        ll = LinkedList()
        item1 = ll.add_to_front(5151, 91951)
        key = 123
        value = [1,2,3]
        item2 = ll.insert_after(item1, key, value)
        assert item2.key == key
        assert item2.value == value

    # ============== insert_before ==========

    def test_insert_before_updates_front(self):
        ll = LinkedList()
        item1 = ll.add_to_back(5151, 91951)
        assert ll.front == item1
        item2 = ll.insert_before(item1, 123, 234)
        assert ll.front == item2

    def test_insert_before(self):
        ll = LinkedList()
        item1 = ll.add_to_back(5151, 91951)
        assert item1.prev == None
        item2 = ll.insert_before(item1, 123, 234)
        assert item1.prev == item2
        assert item2.next == item1
        item3 = ll.insert_before(item1, 987234, "kjnsdfjn")
        assert item1.prev == item3
        assert item3.prev == item2
        assert item2.next == item3
        assert item3.next == item1

    def test_cannot_insert_before_None(self):
        ll = LinkedList()
        with pytest.raises(Exception):
            ll.insert_before(None, 123, 1414)

    def test_cannot_insert_before_item_from_other_list(self):
        ll = LinkedList()
        ll2 = LinkedList()
        item_from_ll = ll.add_to_front(123, 123)
        with pytest.raises(Exception):
            ll2.insert_before(item_from_ll, 123, 1414)

    def test_insert_before_updates_length(self):
        ll = LinkedList()
        item1 = ll.add_to_front(5151, 91951)
        assert ll.length == 1
        ll.insert_before(item1, 123, 234)
        assert ll.length == 2
        ll.insert_before(item1, 987234, "kjnsdfjn")
        assert ll.length == 3
            
    def test_insert_before_return_new_item(self):
        ll = LinkedList()
        item1 = ll.add_to_front(5151, 91951)
        key = 123
        value = [1,2,3]
        item2 = ll.insert_before(item1, key, value)
        assert item2.key == key
        assert item2.value == value

    #============== map =====================

    def test_map_None_equal_to_identity(self):
        ll = LinkedList()
        item1 = ll.add_to_front(123, 8907067)
        ll2 = ll.map(None)
        item2 = ll2.front
        assert item1.key == item2.key
        assert item1.value == item2.value
        assert ll.length == ll2.length

    def test_map_creates_new_list(self):
        ll = LinkedList()
        ll2 = ll.map(None)
        assert ll != ll2

    def test_map_applies_func_to_all_keys_and_values(self):
        ll = LinkedList()
        item1 = ll.add_to_front(123, 345)
        item2 = ll.add_to_front("", 2345)
        item3 = ll.add_to_front([1,2,3], 234)
        ll2 = ll.map(lambda x, y: (x, False))
        ll_current = ll.front
        ll2_current = ll2.front
        assert ll.length == ll2.length and ll.length == 3 
        while ll_current:
            assert ll_current.key == ll2_current.key
            assert ll2_current.value == False
            ll_current = ll_current.next
            ll2_current = ll2_current.next

    def test_map_preserves_front_and_back(self):
        ll = LinkedList()
        ll.add_to_front(123, 123123)
        ll.add_to_front(234234, 92834923)
        ll2 = ll.map(None)
        assert ll.front.key == ll2.front.key
        assert ll.front.value == ll2.front.value
        assert ll.back.key == ll2.back.key
        assert ll.back.value == ll2.back.value

    def test_map_creates_new_items(self):
        ll = LinkedList()
        item1 = ll.add_to_front(12, 3534536)
        ll2 = ll.map(None)
        item2 = ll2.front
        assert item1 != item2
        assert item1.key == item2.key
        assert item2.value == item2.value

    #=============== in_map ===================

    def test_in_map_None_equal_to_identity(self):
        ll = LinkedList()
        item1 = ll.add_to_front(123, 8907067)
        ll.in_map(None)
        assert item1 == ll.front

    def test_in_map_applies_func_to_all_keys_and_values(self):
        ll = LinkedList()
        item1 = ll.add_to_front(123, 345)
        item2 = ll.add_to_front("", 2345)
        item3 = ll.add_to_front([1,2,3], 234)
        ll.in_map(lambda x, y: (True, False))
        assert ll.length == 3 
        ll_current = ll.front
        while ll_current:
            assert ll_current.key == True
            assert ll_current.value == False
            ll_current = ll_current.next

    #=============== filter ==================

    def test_map_filter_equal_to_identity(self):
        ll = LinkedList()
        item1 = ll.add_to_front(123, 8907067)
        ll2 = ll.filter(None)
        item2 = ll2.front
        assert item1.key == item2.key
        assert item1.value == item2.value
        assert ll.length == ll2.length

    def test_filter_creates_new_list(self):
        ll = LinkedList()
        ll2 = ll.filter(None)
        assert ll != ll2

    def test_filter_applies_func_to_all_items(self):
        ll = LinkedList()
        item1 = ll.add_to_front(123, 345)
        item2 = ll.add_to_front("", 2345)
        item3 = ll.add_to_front([1,2,3], 234)
        ll2 = ll.filter(lambda x, y: True)
        ll_current = ll.front
        ll2_current = ll2.front
        assert ll.length == ll2.length and ll.length == 3 
        while ll_current:
            assert ll_current.key == ll2_current.key
            assert ll2_current.value == ll2_current.value
            ll_current = ll_current.next
            ll2_current = ll2_current.next

    def test_filter_preserves_front_and_back_if_needed(self):
        ll = LinkedList()
        ll.add_to_front(123, 123123)
        ll.add_to_front(234234, 92834923)
        ll2 = ll.filter(None)
        assert ll.front.key == ll2.front.key
        assert ll.front.value == ll2.front.value
        assert ll.back.key == ll2.back.key
        assert ll.back.value == ll2.back.value

    def test_filter_creates_new_items(self):
        ll = LinkedList()
        item1 = ll.add_to_front(12, 3534536)
        ll2 = ll.filter(None)
        item2 = ll2.front
        assert item1 != item2
        assert item1.key == item2.key
        assert item2.value == item2.value

    def test_filter_remove_all(self):
        ll = LinkedList()
        item1 = ll.add_to_front(123, 345)
        item2 = ll.add_to_front(51515, 15151551)
        item3 = ll.add_to_front(987, 234267)
        assert ll.length == 3
        assert ll.front == item3
        assert ll.back == item1
        ll2 = ll.filter(lambda x,y: False)
        assert ll2.length == 0

    def test_filter_remove_selective(self):
        ll = LinkedList()
        item1 = ll.add_to_back(1, 345)
        item2 = ll.add_to_back(5, 15151551)
        item3 = ll.add_to_back(7, 234267)
        item4 = ll.add_to_back(1, 907525)
        item5 = ll.add_to_back(7, 789235)
        ll2 = ll.filter(lambda x,y: x==1)
        assert ll2.length == 2
        assert ll2.front.key == item1.key
        assert ll2.front.value == item1.value
        assert ll2.back.key == item4.key
        assert ll2.back.value == item4.value

    #================== in_filter ============

    def test_in_filter_None_equal_to_identity(self):
        ll = LinkedList()
        item1 = ll.add_to_front(123, 8907067)
        ll.in_filter(None)
        assert item1.key == ll.front.key
        assert item1.value == ll.front.value
        assert ll.length == 1

    def test_in_filter_applies_func_to_all_items(self):
        ll = LinkedList()
        items = [ll.add_to_back(123, 345),
                    ll.add_to_back("", 2345),
                    ll.add_to_back([1,2,3], 234)]
        ll.in_filter(lambda x, y: True)
        ll_current = ll.front
        assert ll.length == 3 
        i = 0
        while ll_current:
            assert ll_current == items[i]
            ll_current = ll_current.next
            i += 1

    def test_in_filter_preserves_front_and_back_if_needed(self):
        ll = LinkedList()
        item1 = ll.add_to_front(123, 123123)
        item2 = ll.add_to_front(234234, 92834923)
        ll.in_filter(None)
        assert ll.front == item2
        assert ll.back == item1 

    def test_in_filter_remove_all(self):
        ll = LinkedList()
        item1 = ll.add_to_front(123, 345)
        item2 = ll.add_to_front(51515, 15151551)
        item3 = ll.add_to_front(987, 234267)
        assert ll.length == 3
        ll.in_filter(lambda x,y: False)
        assert ll.length == 0

    def test_in_filter_remove_selective(self):
        ll = LinkedList()
        item1 = ll.add_to_back(1, 345)
        item2 = ll.add_to_back(5, 15151551)
        item3 = ll.add_to_back(7, 234267)
        item4 = ll.add_to_back(1, 907525)
        item5 = ll.add_to_back(7, 789235)
        ll.in_filter(lambda x,y: x==1)
        assert ll.length == 2
        assert ll.front == item1
        assert ll.back == item4

    #============== swap_places =============

    def test_swap_None_no_switch(self):
        ll = LinkedList()
        with pytest.raises(Exception):
            ll.swap(None, None)
        assert ll.length == 0
        item1 = ll.add_to_back(123, 12141)
        with pytest.raises(Exception):
            ll.swap(item1, None)
        assert ll.length == 1
        assert ll.front == item1
        with pytest.raises(Exception):
            ll.swap(None, item1)
        assert ll.length == 1
        assert ll.front == item1

    def test_swap_same_no_effect(self):
        ll = LinkedList()
        item1 = ll.add_to_back(123, 91284)
        item2 = ll.add_to_back(51515, 192)
        assert ll.front == item1
        assert ll.back == item2
        assert ll.length == 2
        ll.swap(item1, item1)
        assert ll.front == item1
        assert ll.back == item2
        assert ll.length == 2

    def test_swap_only_items_from_list(self):
        ll = LinkedList()
        ll2 = LinkedList()
        item1 = ll.add_to_front(5151, 91951)
        item2 = ll2.add_to_front(58888888, 851)
        with pytest.raises(Exception):
            ll.swap(item1, item2)

    def test_swap_front(self):
        ll = LinkedList()
        item1 = ll.add_to_front(1414, 1414)
        item2 = ll.add_to_back(431, 4321)
        ll.swap(item1, item2)
        ll.front == item2

    def test_swap_back(self):
        ll = LinkedList()
        item1 = ll.add_to_front(1414, 1414)
        item2 = ll.add_to_back(431, 4321)
        ll.swap(item1, item2)
        ll.back == item1

    def test_swap_preserves_length(self):
        ll = LinkedList()
        item1 = ll.add_to_front(5151, 91951)
        assert ll.length == 1
        item2 = ll.add_to_front(235151, 91951)
        assert ll.length == 2
        ll.swap(item1, item2)
        assert ll.length == 2
            
    def test_swap_non_edge_items(self):
        ll = LinkedList()
        item1 = ll.add_to_back(5151, 91951)
        item2 = ll.add_to_back(235151, 91951)
        item3 = ll.add_to_back(512351, 91951)
        item4 = ll.add_to_back(510951, 91951)
        item5 = ll.add_to_back(51747451, 91951)
        ll.swap(item2, item4)
        assert item1.next.key == item4.key
        assert item4.next == item3
        assert item3.next == item2
        assert item2.next == item5
        assert item5.prev == item2
        assert item2.prev == item3
        assert item3.prev == item4
        assert item4.prev == item1

