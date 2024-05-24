class CountedIterator():
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0
    def get_count(self):
        return self.count
    def __next__(self):
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration("No more items in the iterator")
iterable_list = [1, 2, 3, 4, 5]
counted_iter = CountedIterator(iterable_list)

try:
    while True:
        item = next(counted_iter)
        print(f"Got {item}, total {counted_iter.get_count()} items iterated.")
except StopIteration:
    print("No more items.")
