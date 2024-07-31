class Library:
    __books = []
    __no_of_books = None
    def __init__(self, *books):
        self.__books.extend(books)
        self.__no_of_books = len(books)
    def display_books(self):
        for book in self.__books:
            print(book)
    def add_book(self, book):
        self.__books.append(book)
        __no_of_books = len(self.__books)
    def get_no_of_books(self):
        return self.__no_of_books
    def delete_a_book(self,book):
        self.__books.remove(book)

library = Library(None)
while True:
    x = int(input("Enter\n1 to ADD BOOK\n2 to Display All Books In Library\n3 to Delete a Book From Library\n4 to Print No Of Books in Library\n5 to exit\n>"))
    match x:
        case 1:
            book = input("Enter Name Of Book To Add : ")
            library.add_book(book)
            continue
        case 2:
            library.display_books()
            continue
        case 3:
            book = input("Enter Name Of Book To Delete : ")
            library.delete_a_book(book)
            continue
        case 4:
            print(f"No of Total Books in Library are = {library.get_no_of_books()}")
        case 5:
            print("See You Next Time\nGOOD Byeee!")
            break
        case _:
            print("Invalid Input!\nEnter 1/2/3/4 OR 5")
            continue
