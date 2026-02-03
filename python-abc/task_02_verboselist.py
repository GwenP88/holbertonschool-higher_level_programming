#!/usr/bin/env python3
"""VerboseList prints notifications
when items are added to or removed from a list."""


class VerboseList(list):
    """VerboseList extends list and
    prints notifications on append/extend/remove/pop."""

    def append(self, iterable):
        """Append one item to the list and print a notification."""
        super().append(iterable)
        print("Added [{}] to the list.".format(iterable))

    def extend(self, iterable):
        """Extend the list and print how many items were added."""
        nb_of_items = len(iterable)
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(nb_of_items))

    def remove(self, iterable):
        """Remove the first matching item and print a notification."""
        print("Removed [{}] from the list.".format(iterable))
        super().remove(iterable)

    def pop(self, index=None):
        """Pop and return an item (default last) and print a notification."""
        if index is None:
            index = -1
        print("Popped [{}] from the list.".format(self[index]))
        popped_item = super().pop(index)
        return popped_item
