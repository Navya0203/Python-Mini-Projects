#onlinelibrarymanager
#create libraryclass
#methods define to display all book
#adbook if someone donates a adbook
#lend karni hai kisiko book tab
#return karega koi

#navyalibrary=library("list of books","namelibrary")

#dictionary maintain ki kis insaan ne konsi book le rakhi hai
#if a book not available then tell who has taken the book
#dictionary book,name

#create a main function and run infinite while loop
import time

class Library:



    def __init__(self,list_B,namelib):
        self.list=list_B
        self.name=namelib
        self.lent={}

    def display(self):
         for books in self.list:
             print(books)

    def lend(self,name,book):
        if book not in self.lent.keys():


            self.lent.update({book:name})
            print(self.lent)
            print('Lender book database has been updated')


        else:
            print(f"This book has been lent to {self.lent[book]}")

    def returnb(self,book):
        self.lent.pop(book)
        print("book was returned successfully")
        #print(cls.lent)

    def adbook(self,bookn):
        self.list.append(bookn)
        print("Book has been added to the book list")
if __name__ == '__main__':


    Mylib=Library(["A","B","C","D","E"],"Mylib")
    while True:
        print("Welcome to my library")
        print("Please enter 1 if you want to see the books available")
        print("Please enter 2 if you want to donate a book")
        print("Please enter 3 if you want to borrow a book")
        print("Please enter 4 if you want to return a book")
        a=int(input("please choose one of the following 1,2,3,4 \n"))
        if a==1:
            Mylib.display()
            time.sleep(2)
        elif a==2:
            bookname=input('Please enter the name of the book')
            Mylib.adbook(bookname)
            print(Mylib.list)

            time.sleep(2)
        elif a==3:
            if len(Library.lent)!=0:
                print(f"These are the books that have been lent already and are not available {Library.lent}")
            else:
                print('All books are available to be lent')
            name=input("Please enter your name")
            book=input("Please enter the name of the book you wish to lend")
            if book in Mylib.list:
                Mylib.lend(name,book)
                time.sleep(2)
            else:
                print('Choose a book from the list of available books')
        elif a==4:
            bookr=input('Enter the name of the book you wish to return')
            Mylib.returnb(bookr)

        else:
            print("Enter a valid input")
        q=input('Do you wish to continue y/n')
        while q!="y" and q!="n":
            print('Please give a valid input')
            q=input('Do you wish to continue y/n')

        if q=="n":
            break
