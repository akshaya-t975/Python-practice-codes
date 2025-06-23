class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published
        self.checked_out = False

    def display_info(self):
        status = "Checked Out" if self.checked_out else "Available"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year Published: {self.year_published}")
        print(f"Status: {status}")
        print()

    def checkout(self):
        self.checked_out = True
        print(f"You have checked out '{self.title}'.\n")

    def return_book(self):
        self.checked_out = False
        print(f"You have returned '{self.title}'.\n")


title1 = input("Enter title of first book: ")
author1 = input("Enter author of first book: ")
year1 = int(input("Enter year published of first book: "))
book1 = Book(title1, author1, year1)

title2 = input("\nEnter title of second book: ")
author2 = input("Enter author of second book: ")
year2 = int(input("Enter year published of second book: "))
book2 = Book(title2, author2, year2)


print("\nBook 1 info:")
book1.display_info()
print("Book 2 info:")
book2.display_info()


book1.checkout()
book1.display_info()


book1.return_book()
book1.display_info()



