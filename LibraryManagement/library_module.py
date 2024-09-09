class Book:
    id=300
    def __init__(self):
        self.title=input("book title:")
        self.author=input("author:")
        Book.id+=1
        self.book_id=Book.id
        self.borrowed_status=False
    def display_book_details(self):
        print("id:",self.book_id)
        print("title:",self.title)
        print("author:",self.author)


class Library:
    def __init__(self):
        self.book_collection=[]
    def add_book(self):
        new_book=Book()
        self.book_collection.append(new_book)
        return "book added successfully"
    def remove_book(self,book_id):
        for book in self.book_collection:
            if book.book_id==book_id:
                if book.borrowed_status:
                    print("book is borrowed.can't remove the book.")
                else:
                    self.book_collection.remove(book)
                return "book removed"
        return "book not found"
    def search_book(self,book_title):
        book_found=False
        for book in self.book_collection:
            if book_title.lower() in book.title.lower():
                print(book.display_book_details())
                book_found=True
        if not book_found:
            print("book not found")
    def generate_book(self):
        for book in self.book_collection:
            yield book

class User:
    id=1000
    def __init__(self):
        self.name=input("user name:")
        User.id+=1
        self.user_id=User.id
    def display_user_details(self):
        print("User Id",self.user_id)
        print("User Name",self.name)

class LibraryUser(User):
    def __init__(self):
        super().__init__()
        self.borrowed_books=[]
    def borrow_book(self,library,book_id):
        for book in library.book_collection:
            if book.book_id==book_id:
                if not book.borrowed_status:
                    book.borrowed_status=True
                    self.borrowed_books.append(book)
                    return "book is successfully borrowed"
                else:
                    return "book is already borrowed"
            else:
                return "book not found"
    def return_book(self,library):
        book_id=int(input("book id:"))
        for book in library.book_collection:
            if book.book_id==book_id and book.borrowed_status==True and book in self.borrowed_books:
                    book.borrowed_status=False
                    self.borrowed_books.remove(book)
                    return "book is successfully returned"
            else:
                    return "unable to return book"
    def track_borrowed_books(self):
        if not self.borrowed_books:
            print("No books have been borrowed")
        else:
            print("books borrowed:")
            for book in self.borrowed_books:
                print(book.display_book_details())


