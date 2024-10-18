class MyIterable:
    def __init__(self, start, end):
        self.start = start  # Starting value
        self.end = end      # Ending value

    def __iter__(self):
        # Return an instance of an iterator (can be self or another object)
        self.current = self.start
        return self

    def __next__(self):
        # Return the next value in the iteration or raise StopIteration
        if self.current < self.end:
            num = self.current
            self.current += 1  # Move to the next value
            return num
        else:
            raise StopIteration  # End of iteration


my_iter = MyIterable(1, 5)

for num in my_iter:
    print(num)
