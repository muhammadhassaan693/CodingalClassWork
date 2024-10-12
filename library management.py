class library:
    def __init__(self, list_of_book, nm):
        #initializing the variable or fethure in this class
        self.booklist=list_of_book
        self.name=nm
        self.lenthOfDictionary={}

    def displayBooks(self):
        print(f"we have the following books in our library = {self.name}")

        for book in self.booklist:
            print(book)


    def lendBook(self, user, book):
        if book not in self.booklist:
            print("sorry we do not have that book")
        elif book in self.lenthOfDictionary:
            print("the book is already being used by ",self.lenthOfDictionary[book])
        else:
            self.lenthOfDictionary[book]= user       

    def addBook(self,book):
        self.booklist.append(book)
        print(f"{book} as been added to the book list")



books = library(

['Python', 'Rich Dad Poor Dad', 'Harry Potter', 'C++ Basics', 'Algorithms by CLRS'],

"Let's Upskill")

userName=input("please enter your name: ")

while True:
    print(f"hello {userName} welcome to the library please chosse an opction")
    print("1.display book")
    print("2.lend book")
    print("3.at a book")
    print("4.quit")

    userchoice=int(input("enter your choice to continue = "))

    if userchoice == 1:
        books.displayBooks()
    elif userchoice == 2:
        bookname = input("enter the book name you want borrow = ")
        books.lendBook(userName,bookname)
    elif userchoice == 3:
        bookname = input("enter the the book name you want to add = ")
        books.addBook()
    elif userchoice == 4:
        print("thank you for using the library goodbey")
        break
