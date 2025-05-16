class Book:
    total_books = 0
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        print(cls.total_books)

Book.increment_book_count()

book1 = Book()

