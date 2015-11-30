linkedlist
==========
Linked list data structure implemented in Python.

This project is using [semantic versioning](http://semver.org/).

Installation
------------

```python
pip install linkedlist
```

Examples
-------
```python
from linkedlist import LinkedList

ll = LinkedList()

# Add items to either the front or the back
ll.add_to_front(12, "hi")
ll.add_to_front(14, "hello")
ll.add_to_back(16, [1, 2, 3])
ll.add_to_back(15)

# Retrieve front and back
# Output: '14'
print ll.front.key
# Output: "hello"
print ll.front.value

# Output: '15'
print ll.back.value
# Output: None

# Output: '12'
print ll.front.next.key
# Output: "hi"
print ll.front.next.value

# Output: '16'
print ll.back.prev.key
# Output: [1, 2, 3]
print ll.back.prev.value

```
```python
ll = LinkedList()
ll.add_to_front(14, "hello")
ll.add_to_back(16, [1, 2, 3])

# Remove item
ll.remove(ll.back)
# Output: "hello"
print ll.back.value
```
```python
ll = LinkedList()
ll.add_to_front(14, "hello")
ll.add_to_back(16, [1, 2, 3])
ll.add_to_back(16, "16 again")

# Find first
first = ll.find_first(16)
# Output: [1, 2, 3]
print first.value

#Find last
last = ll.find_last(16)
# Output: "16 again"
print last.value

# Insert after
ll.insert_after(ll.front, 17, "17 now")
# Output: "17 now"
print ll.front.next.value

# Insert before
ll.insert_before(ll.back, 18, "18!")
# Output: "18!"
print ll.back.prev.value
```
```python
ll = LinkedList()
ll.add_to_front(14, "hello")
ll.add_to_back(16, [1, 2, 3])
ll.add_to_back(16, "16 again")

# Filter
ll2 = ll1.filter(lambda x, y: x==14)
# Output: 1
print ll2.length
# Output: "hello"
print ll2.front.value

# 'In list' filter
ll.in_filter(lambda: x, y: x==16)
# Output: 2
print ll.length
```
```python
ll = LinkedList()
ll.add_to_front(14, "hello")
ll.add_to_back(16, [1, 2, 3])
ll.add_to_back(16, "16 again")

# Map
ll2 = ll.map(lambda x, y: (x/2, y))
# Output: 7
print ll.front.key
# Output: 8
print ll.front.next.key

# 'In list' map
ll.in_map(lambda x, y: (True, False))
# Output: True
print ll.front.key
# Output: False
print ll.front.value
# Output: True
print ll.back.key
# Output: False
print ll.back.value
```
```python
ll = LinkedList()
ll.add_to_back(14, "hello")
item1 = ll.add_to_back(16, [1, 2, 3])
ll.add_to_back(17, "16 again")
item2 = ll.add_to_back(18, "18!")
ll.add_to_back(19, "nine+ten")

# Swap
ll.swap(item1, item2)
# Output: 18
print ll.front.next.key
# Output: 16
print ll.back.prev.key

```

Running tests
-------------
Install [pytest](http://pytest.org/latest/getting-started.html),
then run the following command from the root folder:

```
py.test
```
Contributing
------------
0. (optional) Open an issue with a suggestion for a feature or a bug.
1. Find an open issue to work on, then fork the repo.
2. Solve issue and write tests to illustrate the bug or feature.
3. Send pull request indicating which issue is solved.

Maintainer
----------
Peter Andersson \<teroqim@gmail.com\> [@teroqim](https://github.com/teroqim)
