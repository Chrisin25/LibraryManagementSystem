from LibraryManagement.library_module import Library,LibraryUser
print("library")
new_library=Library()
stop=False
while not stop:
    choice = int(input("Enter your choice:1.add book 2.remove book 3.search book 4.generate book."))
    if choice==1:
        print(new_library.add_book())
    elif choice==2:
        book_id = int(input("enter book id:"))
        print(new_library.remove_book(book_id))
    elif choice==3:
        book_title=input("enter book title:")
        new_library.search_book(book_title)
    elif choice==4:
        new_library.generate_book()
    else:
        print("invalid choice")
    response=input("do you want to continue: y or n")
    if response=="n":
        stop=True
#Create a user.

print("User")
new_user=LibraryUser()
stop=False
while not stop:
    choice = int(input("Enter your choice:1.borrow book 2.return book 3.track borrowed book"))
    if choice==1:
        book_id = int(input("enter book id:"))
        print(new_user.borrow_book(new_library,book_id))
    elif choice==2:
        print(new_user.return_book(new_library))
    elif choice==3:
        new_user.track_borrowed_books()
    else:
        print("invalid choice")
    response=input("do you want to continue: y or n")
    if response=="n":
        stop=True