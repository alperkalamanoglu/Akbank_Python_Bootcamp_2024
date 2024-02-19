class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")
    
    def __del__(self):
        self.file.close()
    
    def list_books(self):
        self.file.seek(0)
        books = self.file.readlines()
        if not books:
            print("No books available.")
        else:
            for book in books:
                book_info = book.strip().split(',')
                print(f"Title: {book_info[0]}, Author: {book_info[1]}")
    
    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_year = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")
    
    def remove_book(self):
        title = input("Enter the title of the book to remove: ")
        self.file.seek(0)
        books = self.file.readlines()
        updated_books = []
        removed = False
        for book in books:
            if title.lower() not in book.lower():
                updated_books.append(book)
            else:
                removed = True
        if not removed:
            print(f"Book with title '{title}' not found.")
        else:
            self.file.seek(0)
            self.file.truncate()
            self.file.writelines(updated_books)
            print(f"Book '{title}' removed successfully.")

def main():
    lib = Library()
    while True:
        print("\n*** MENU***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            lib.list_books()
        elif choice == "2":
            lib.add_book()
        elif choice == "3":
            lib.remove_book()
        else:
            print("Invalid choice. Please enter a number from 1 to 3.")

if __name__ == "__main__":
    main()
