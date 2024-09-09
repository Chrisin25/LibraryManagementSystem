from LibraryManagement.library_module import Library,LibraryUser

new_library=Library()
#Add books to the library.
print(new_library.add_book())
#Create a user.
new_user=LibraryUser()
#Allow the user to borrow a book and return it
book_id=input("book id:")
print(new_user.borrow_book(new_library,book_id))
print(new_user.return_book(new_library))

