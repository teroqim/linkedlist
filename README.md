linkedlist
==========
Linked list data structure implemented in Python.

This project uses semantic versioning v2.0.0 (http://semver.org/).

Installation
------------

```python
pip install linkedlist
```

Example
-------
```python
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
```

Running tests
-------------
Install `pytest <http://pytest.org/latest/getting-started.html>`,
then simply run the following command from the root folder:

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
Peter Andersson <teroqim@gmail.com> `@teroqim <https://github.com/teroqim>`
