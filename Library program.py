# Displays available books and borrowed books in two different lists.
def display_books(available_books, borrowed_books):

    print("Available Books:")
    if len(available_books) == 0:
        print(' Currently no books in list ')
    else:
        for i in range (len(available_books)):
            print (f" {(i+1)}. {available_books[i]}")
    print ("Borrowed Books: ")
    if (len(borrowed_books)) == 0:
        print (' Currently no books in list')
    else:
        for i in range(len(borrowed_books)):
            print(f" {(i+1)}. {borrowed_books[i]}")

# Handles the process of checking out a book.
def borrow_book(available_books, borrowed_books):

    display_books(available_books, borrowed_books)
    book_choice = int(input('Which book would you like to borrow (1-5): '))
    if 1 <= book_choice <= len(available_books):
            selected_book = available_books[book_choice - 1]
            available_books.remove(selected_book)
            borrowed_books.append(selected_book)
            print(f"You have borrowed: {selected_book}")
    else:
        print("Please select a valid book number.")

# Handles the process of returning books from the user
def return_books(available_books, borrowed_books):

    print("Borrowed Books: ")
    if (len(borrowed_books)) == 0:
        print (' Currently no books in list')
    while borrowed_books:
            book = borrowed_books.pop()  # Remove and get the last borrowed book
            available_books.append(book)
            print("All books have been returned.")

# Handles the main function of the program.
def main():

    MENU_OPTIONS = """ 
        1. Display all books available and borrowed.
        2. Borrow a book. 
        3. Return a book. 
        4. Exit the program
        """
    available_books = ["The Bible", "The Great Gatsby", "Of mice and Men", "Fly into the Wind", "The DaVinci Code"]
    borrowed_books = []

    print('Welcome to the library program. Please select from the following options.')

    while True:
        print(MENU_OPTIONS)
        user_choice = int(input('Which menu option would you like to choose (1-4): '))

        if user_choice == 4:
            print('Thanks for using the library. Goodbye!')
            break
        elif user_choice == 1:
            display_books(available_books, borrowed_books)
        elif user_choice == 2:
            borrow_book(available_books, borrowed_books)
        elif user_choice == 3:
            return_books(available_books, borrowed_books)
        else:
            print("Invalid option, please try again.")



if __name__ == "__main__":
    main()