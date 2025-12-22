class LibraryAccount:
    def __init__(self, name):
        self.name = name
        self.books = []

    def borrow_book(self, book_name):
        self.books.append(book_name)
        print(f"Book '{book_name}' is borrowed.")

    def return_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"Book '{book_name}' is returned.")
        else:
            print("Error: this book is not borrowed!")

    def list_books(self):
        if self.books:
            print("Borrowed books:")
            for book in self.books:
                print("-", book)
        else:
            print("No borrowed books.")

account = LibraryAccount("Georgi")
account.borrow_book("Harry Potter")
account.borrow_book("The Lord of the Rings")
account.list_books()
account.return_book("Harry Potter")
account.return_book("Peter Pan") 
account.list_books()