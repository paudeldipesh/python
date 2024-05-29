class Library:
    """
    This class represents a library that holds books.
    """

    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def print_books(self):
        """
        Prints all the books currently in the library.
        """
        if self.no_of_books == 0:
            print("There are no books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)

    def add_book(self, book):
        """
        Adds a book to the library collection.
        """
        self.books.append(book)
        self.no_of_books += 1

    def get_number_of_books(self):
        """
        Returns the number of books currently in the library.
        """
        return self.no_of_books


# Create a library object
library = Library()
library.print_books()

# Add some books to the library
library.add_book("The Power of Your Subconscious Mind")
library.add_book("Think and Grow Rich")
library.add_book("The Intelligent Investor")
library.add_book("Rich Dad Poor Dad")
library.add_book("The Science of Getting Rich")

# Print all the books in the library
library.print_books()

# Get the number of books in the library
number_of_books = library.get_number_of_books()
print("Number of books:", number_of_books)
