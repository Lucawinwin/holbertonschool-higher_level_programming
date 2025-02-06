#!/usr/bin/env python3
"""
This module defines a CountedIterator class that wraps an iterator
and counts the number of items iterated over.
"""


class CountedIterator:
    """
    An iterator that counts the number of items iterated over.
    """
    def __init__(self, iterator):
        """
        Initialize the CountedIterator with an existing iterator.
        """
        self.iterator = iter(iterator)
        self.counter = 0

    def __iter__(self):
        """
        Return the iterator itself.
        """
        return self

    def __next__(self):
        """
        Return the next item from the iterator and increment the count.
        """
        item = next(self.iterator)
        if not item:
            raise StopIteration
        self.counter += 1
        return item

    def get_count(self):
        """
        Return the number of items iterated over.
        """
        return self.counter
