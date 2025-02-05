class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0
    
    def __next__(self):
        item = next(self.iterator)
        self.count += 1
        return item
    
    def get_count(self):
        return self.count

# Testing the CountedIterator
my_list = [1, 2, 3, 4, 5]
counted_iter = CountedIterator(my_list)

# Manual iteration
print(next(counted_iter))  # 1
print(next(counted_iter))  # 2
print(counted_iter.get_count())  # 2

# Loop iteration
for item in counted_iter:
    print(item)
print(counted_iter.get_count())  # 5
