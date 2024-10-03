class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        print(f"'{self.title}' by {self.author}")

# Example usage:
my_book = Book("1984", "George Orwell")
my_book.describe()  # Output: '1984' by George Orwell
