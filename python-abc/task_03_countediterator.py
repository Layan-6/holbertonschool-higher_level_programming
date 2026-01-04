#!/usr/bin/env python3
"""Task 3: CountedIterator - Keeping Track of Iteration"""

class CountedIterator:
    """An iterator that keeps count of items iterated"""
    
    def __init__(self, iterable):
        """Initialize with an iterable and set counter to 0"""
        self.iterator = iter(iterable)
        self.counter = 0
    
    def __next__(self):
        """Get next item, increment counter, and return item"""
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise
    
    def get_count(self):
        """Return the number of items iterated"""
        return self.counter
    
    def __iter__(self):
        """Return self to allow iterator to be used in for-loops"""
        return self
