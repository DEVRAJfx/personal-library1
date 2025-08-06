

# this is a cli app we are gonna make a library . where we can add , remove, ,
'''
Welcome to Your Library!

1. Add Book
2. Remove Book
3. Search Book
4. Show All Books
5. Exit

Enter your choice: 1
Enter title: The Alchemist
Enter author: Paulo Coelho
Enter year: 1988
Book added!

Enter your choice: 4
Your Library:
1. The Alchemist - Paulo Coelho (1988)


'''
# the frontpage of the library app

print("\n       Welcome to your personal library!       \n")
print("1. Add new book")
print("2. Remove existing book")
print("3. Search book")
print("4. Show all books")
print("5. Exit")

library = []
n = True

while n:
    choice = input("\nEnter your choice: ")

    if choice.isdigit():
        choice = int(choice)

        if choice == 1:
            name = input("Enter the name of the book: ")
            author = input("Enter the author of the book: ")
            year = int(input("Enter the year the book was published: "))
            bookinfo = (name, author, year)
            library.append(bookinfo)
            print("\nBook added.")

        elif choice == 2:
            removename = input("Enter the name you want to remove: ")
            found = False
            for rbook in library:
                if rbook[0].lower() == removename.lower():
                    library.remove(rbook)
                    print("Book removed.")
                    found = True
                    break
            if not found:
                print("Book not found.")

        elif choice == 3:
            findname = input("Enter the name of the book to search: ")
            found = False
            for book in library:
                if book[0].lower() == findname.lower():
                    print(f"Found: {book[0]} - {book[1]} ({book[2]})")
                    found = True
                    break
            if not found:
                print("Book not found.")

        elif choice == 4:
            if library:
                for i, book in enumerate(library, start=1):
                    print(f"{i}. {book[0]} - {book[1]} ({book[2]})")
            else:
                print("Library is empty.")

        elif choice == 5:
            print("Thanks for visiting the library!")
            break

        else:
            print("Enter a valid choice (1-5).")
    else:
        print("Invalid input. Please enter a number.")



          
          
          

        
          



           
        


        
        

        