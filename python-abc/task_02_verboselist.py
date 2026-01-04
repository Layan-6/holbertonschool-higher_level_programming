#!/usr/bin/env python3
"""Task 2: Extending the Python List with Notifications"""

class VerboseList(list):
    """A list subclass that prints notifications for modifications"""

    def append(self, item):
        """Add an item to the end of the list with notification"""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list with items from iterable with notification"""
        length_before = len(self)
        super().extend(iterable)
        added_items = len(self) - length_before
        print(f"Extended the list with [{added_items}] items.")

    def remove(self, item):
        """Remove first occurrence of item with notification"""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return item at index with notification"""
        item = self[index] if len(self) > 0 else None
        result = super().pop(index)
        print(f"Popped [{result}] from the list.")
        return result
