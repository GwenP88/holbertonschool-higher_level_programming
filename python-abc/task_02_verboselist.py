#!/usr/bin/env python3
"""VerboseList prints notifications
when items are added to or removed from a list."""


class VerboseList(list):
    """VerboseList extends list and
    prints notifications on append/extend/remove/pop."""

    def append(self, item):
        """Append one item to the list and print a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        """Extend the list and print how many items were added."""
        nb_of_items = len(item)
        super().extend(item)
        print("Extended the list with [{}] items.".format(nb_of_items))

    def remove(self, item):
        """Remove the first matching item and print a notification."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=None):
        """Pop and return an item (default last) and print a notification."""
        if index is None:
            index = -1
        print("Popped [{}] from the list.".format(self[index]))
        popped_item = super().pop(index)
        return popped_item
