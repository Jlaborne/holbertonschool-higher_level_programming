class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extended the list with {len(iterable)} items.")

    def remove(self, item):
        if item in self:
            print(f"Removed {item} from the list.")
        super().remove(item)

    def pop(self, index=None):
        if index is None:
            index = len(self) - 1
        if index < 0 or index >= len(self):
            raise IndexError("pop index out of range")
        item = self[index]
        print(f"Popped {item} from the list.")
        return super().pop(index)

