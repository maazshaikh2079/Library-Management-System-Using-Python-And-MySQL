# Note:-
# Data-base name : lmsdb
# Password : Shaikh@2079
# Host : localhost
# User : root          
# Admin password : Admin_1@2079
# Number books of present :-
# [In Library Table] - 10 books
# [In Borrowed Table] - 2 books
# Users / borrowers  present :-
# [In Borrowed Table]
# i)  Maaz - 7208613298 
# ii) Wahaj - 9321627175

# Program:-
from mysql.connector import connect
from mysql.connector.errors import InterfaceError
from mysql.connector.errors import ProgrammingError
from time import sleep

class Library:
    def __init__(self):
        self.__dcem = " Something went wrong during data base connection\n"
        try:
            try:
                self._dbCon = connect(
                    host="localhost",
                    password="Shaikh@2079",
                    user="root",
                    database="lmsdb"
                )
            except InterfaceError as ie:
                print("----------------------------------------------------------------------")
                print(f" {type(ie).__name__} : {self.__dcem}.")
                print("----------------------------------------------------------------------\n")
                exit()

            except ProgrammingError as pe:
                print("----------------------------------------------------------------------")
                print(f" {type(ie).__name__} : {self.__dcem}.")
                print("----------------------------------------------------------------------\n")
                exit()

            self._cur = self._dbCon.cursor()
            self._cmd = str()
            self._dbCon.commit()

        except Exception as e:
            print("----------------------------------------------------------------------")
            print(f" {type(e).__name__} : {self.__dcem}.")
            print("----------------------------------------------------------------------\n")
            exit()
        except:
            print("----------------------------------------------------------------------")
            print(f" Error : {self.__dcem}.")
            print("----------------------------------------------------------------------\n")
            exit()

    def lmsMenu(self):
        print("-----------------------------")
        print("  LIBRARY MANAGEMENT SYSTEM ")
        print("-----------------------------\n")

        print("__________MAIN-MENU__________\n")

        print(" Press [1] To Enter As Admin ")
        print(" Press [2] To Enter As User  ")
        print(" Press [3] To Exit System    ")
        print("_____________________________\n")

    def viewAllBks(self):
        self._cmd = "Select * from Library"
        self._cur.execute(self._cmd)
        result = self._cur.fetchall()

        if result != []:
            i = 1
            print("______Available-Book(s)______\n")
            for row in result:
                print(f" Book {i} :-")
                print(" ID     :", row[0])
                print(" Title  :", row[1])
                print(" Author :", row[2])
                print()
                i += 1
            print("-----------------------------\n")
            
        else:
            print("------------------------------------")
            print(" No book(s) present. Empty library. ")
            print("------------------------------------\n")

    def viewPtrBk(self):
        bktl = input(" Enter book title  : ")
        atr = input(" Enter author name : ")
        print()

        self._cmd = "select * from Library where Book_Title=%s and Author=%s"
        info = (bktl, atr)
        self._cur.execute(self._cmd, info)
        result = self._cur.fetchall()
        
        if result != []:
            row=result[0]
            print("________Book-Available________\n")
            print(" ID     :", row[0])
            print(" Title  :", row[1])
            print(" Author :", row[2])
            print()
            print("------------------------------\n")

        else:
            print("------------------------------------")
            print(" No such book present to be viewed. ")
            print("------------------------------------\n")

    def viewAllBrwBks(self):
        self._cmd = "Select * from Borrowed"
        self._cur.execute(self._cmd)
        result = self._cur.fetchall()
        i = 1

        if result != []:
            print("_______Borrowed-Book(s)_______\n")
            for row in result:
                print(f" Book {i} :-")
                print(" Borrower :", row[0])
                print(" Phone no.:", row[1])
                print(" Book ID  :", row[2])
                print(" Title    :", row[3])
                print(" Author   :", row[4])
                print()
                i += 1
            print("------------------------------\n")

        else:
            print("-------------------------------------------")
            print(" No book(s) borrowed yet to be viewed yet. ")
            print("-------------------------------------------\n")

    def viewPtrBrwBk(self):
        bktl = input(" Enter book title  : ")
        atr =  input(" Enter author name : ")
        print()

        self._cmd = "select * from Borrowed where Book_Title=%s and Author=%s"
        info = (bktl, atr)
        self._cur.execute(self._cmd, info)
        result = self._cur.fetchall()
        
        if result != []:
            row=result[0]
            print("________Book-Borrowed________\n")
            print(" Borrower :", row[0])
            print(" Phone no.:", row[1])
            print(" Book ID  :", row[2])
            print(" Title    :", row[3])
            print(" Author   :", row[4])
            print()
            print("------------------------------\n")

        else:
            print("-----------------------------------------")
            print(" No such book borrowed yet to be viewed. ")
            print("-----------------------------------------\n")

    def addBks(self):
        while True:
            ch = input(" Enter 'C' to continue adding or 'Q' to quit: ")
            print()

            if ch == 'C' or ch == 'c':
                bkid = int(input(" Enter book ID     : "))
                bktl = input(" Enter book title  : ")
                atr = input(" Enter author name : ")
                bktl = bktl.title()
                atr = atr.title()
                print()
                self._cmd = "select * from Library where Book_ID=%s and Book_Title=%s and Author=%s"
                info = (bkid, bktl, atr)
                self._cur.execute(self._cmd, info)
                result = self._cur.fetchall()

                if result == []:
                    self._cmd = "Insert into Library(Book_ID,Book_Title,Author) values(%s,%s,%s)"
                    info = (bkid, bktl, atr)
                    self._cur.execute(self._cmd, info)
                    self._dbCon.commit()
                    print("-----------------------------")
                    print(" Book added.                 ")
                    print("-----------------------------\n")

                else:
                    print("-----------------------------")
                    print(" Book already present.       ")
                    print("-----------------------------\n")

            elif ch == 'Q' or ch == 'q':
                break

            else:
                print("-----------------------------")
                print(" Invalid choice! try again.  ")
                print("-----------------------------\n")
                self.addBks()

    def rmvBks(self):
        while True:
            ch = input(" Enter 'C' to continue removing or 'Q' to quit: ")
            print()

            if ch == 'C' or ch == 'c':
                bkid = int(input(" Enter book ID     : "))
                bktl = input(" Enter book title  : ")
                atr =  input(" Enter author name : ")
                bktl = bktl.title()
                atr = atr.title()
                print()

                self._cmd = "select * from Library where Book_ID=%s and Book_Title=%s and Author=%s"
                info = (bkid, bktl, atr)
                self._cur.execute(self._cmd, info)
                result = self._cur.fetchall()

                if result != []:
                    self._cmd = "Delete from Library where Book_ID=%s and Book_Title=%s and Author=%s"
                    info = (bkid, bktl, atr)
                    self._cur.execute(self._cmd, info)
                    self._dbCon.commit()
                    print("-----------------------------")
                    print(" Book removed.               ")
                    print("-----------------------------\n")
                else:
                    print("--------------------------------------")
                    print(" No such book present to be removed.  ")
                    print("--------------------------------------\n")
            elif ch == 'Q' or ch == 'q':
                break
            else:
                print("-----------------------------")
                print(" Invalid choice! try again.  ")
                print("-----------------------------\n")
                self.rmvBks()

    def brwBks(self, unm, phn):
        while True:
            ch = input(" Enter 'C' to continue borrowing or 'Q' to quit: ")
            print()
            if ch == 'C' or ch == 'c':
                bkid = int(input(" Enter book ID     : "))
                bktl = input(" Enter book title  : ")
                atr = input(" Enter author name : ")
                print()

                self._cmd = "select * from Library where Book_ID=%s and Book_Title=%s and Author=%s"
                info = (bkid, bktl, atr)
                self._cur.execute(self._cmd, info)
                result = self._cur.fetchall()

                if result != []:
                    self._cmd = "Delete from Library where Book_ID=%s and Book_Title=%s and Author=%s"
                    info = (bkid, bktl, atr)
                    self._cur.execute(self._cmd, info)
                    self._dbCon.commit()
                    self._cmd = "Insert into Borrowed(Borrower,Phone_No,Book_ID,Book_Title,Author) values(%s,%s,%s,%s,%s)"
                    info = (unm, phn, bkid, bktl, atr)
                    self._cur.execute(self._cmd, info)
                    self._dbCon.commit()
                    print("-----------------------------")
                    print(" Book borrowed.              ")
                    print("-----------------------------\n")
                else:
                    print("--------------------------------------")
                    print(" No such book present to be borrowed. ")
                    print("--------------------------------------\n")
            elif ch == 'Q' or ch == 'q':
                break
            else:
                print("-----------------------------")
                print(" Invalid choice! try again.  ")
                print("-----------------------------\n")
                self.brwBks()

    def rtnBks(self, unm, phn):
        self._cmd = "select * from Borrowed where Borrower=%s and Phone_No=%s"
        info = (unm, phn)
        self._cur.execute(self._cmd, info)
        result = self._cur.fetchall()
        if result != []:
            while True:
                ch = input(" Enter 'C' to continue returning or 'Q' to quit: ")
                print()
                if ch == 'C' or ch == 'c':
                    bkid = int(input(" Enter book ID     : "))
                    bktl = input(" Enter book title  : ")
                    atr = input(" Enter author name : ")
                    print()

                    self._cmd = "select * from Borrowed where Borrower=%s and Phone_No=%s and Book_ID=%s and Book_Title=%s and Author=%s"
                    info = (unm, phn, bkid, bktl, atr)
                    self._cur.execute(self._cmd, info)
                    result = self._cur.fetchall()

                    if result != []:
                        self._cmd = "Delete from Borrowed where Borrower=%s and Phone_No=%s and Book_ID=%s and Book_Title=%s and Author=%s"
                        info = (unm, phn, bkid, bktl, atr)
                        self._cur.execute(self._cmd, info)
                        self._dbCon.commit()
                        self._cmd = "Insert into Library(Book_ID,Book_Title,Author) values(%s,%s,%s)"
                        info = (bkid, bktl, atr)
                        self._cur.execute(self._cmd, info)
                        self._dbCon.commit()
                        print("-----------------------------")
                        print(" Book returned.              ")
                        print("-----------------------------\n")
                    else:
                        print("----------------------------------------------------------------------------")
                        print(f" No such book borrowed by '{unm} - {phn}' to be returned.                  ")
                        print("----------------------------------------------------------------------------\n")
                elif ch == 'Q' or ch == 'q':
                    break
                else:
                    print("-----------------------------")
                    print(" Invalid choice! try again.  ")
                    print("-----------------------------\n")
                    self.rtnBks()
        else:
            print("--------------------------------------------------------------")
            print(f" '{unm} - {phn}' has never borrowed any book.                ")
            print("--------------------------------------------------------------\n")

    def quit(self):
        print(" quiting...\n")
        sleep(1)

    def exitSys(self):
        print("-----------------------------")
        print(" Thank you! have a nice day. ")
        print("-----------------------------\n")
        sleep(1)
        print(" exiting...\n")
        sleep(2)
        exit()


class Admin(Library):
    def __init__(self):
        super().__init__()

    def admMenu(self):
        print("__________________ADMIN-MENU__________________\n")

        print(" Press [1] To View All Book(s)                ")
        print(" Press [2] To View A Particular Book          ")
        print(" Press [3] To View Borrowed Book(s)           ")
        print(" Press [4] To View A Particular Borrowed Book ")
        print(" Press [5] To Add Book(s)                     ")
        print(" Press [6] To Remove Book(s)                  ")
        print(" Press [7] To Quit As Admin                   ")
        print("______________________________________________\n")

    def entrAsAdm(self):
        try:
            pwd = input(" Enter password: ")
            print()
            if pwd == "Admin_1@2079":
                print(" Welcome Admin!\n")
                self.admMenu()

                ch = int()

                while (ch != 7):
                    ch = int(input(" Enter your choice : "))
                    print()

                    match ch:
                        case 1:
                            self.viewAllBks()

                        case 2:
                            self.viewPtrBk()

                        case 3:
                            self.viewAllBrwBks()

                        case 4:
                            self.viewPtrBrwBk()

                        case 5:
                            self.addBks()

                        case 6:
                            self.rmvBks()

                        case 7:
                            self.quit()

                        case _:
                            print(" Invalid choice!\n")

            else:
                raise ValueError(" Wrong password! entry denied.\n")
        except ValueError as ve:
            print(f" {type(ve).__name__} : {ve.args[0]}")


class User(Library):
    def __init__(self):
        super().__init__()

    def usrMenu(self):
        print("______________USER-MENU______________\n")

        print(" Press [1] To View All Book(s)       ")
        print(" Press [2] To View A Particular Book ")
        print(" Press [3] To Borrow Book(s)         ")
        print(" Press [4] To Return Book(s)         ")
        print(" Press [5] To Quit As User           ")
        print("_____________________________________\n")

    def entrAsUsr(self):
        unm = input(" Enter user name : ")
        phn = int(input(" Enter phone no. : "))
        print()
        print(" Welcome",unm)
        print()

        self.usrMenu()

        ch = int()

        while (ch != 5):
            ch = int(input(" Enter your choice : "))
            print()
            match ch:
                case 1:
                    self.viewAllBks()

                case 2:
                    self.viewPtrBk()

                case 3:
                    self.brwBks(unm, phn)

                case 4:
                    self.rtnBks(unm, phn)

                case 5:
                    self.quit()

                case _:
                    print("-----------------------------")
                    print(" Invalid choice!              ")
                    print("-----------------------------\n")


# Driver code:-
if __name__ == "__main__":
    li = Library()
    ad = Admin()
    us = User()

    ch = int()

    while (ch != 3):
        li.lmsMenu()

        ch = int(input(" Enter your choice : "))
        print()

        match ch:
            case 1:
                ad.entrAsAdm()

            case 2:
                us.entrAsUsr()

            case 3:
                li.exitSys()

            case _:
                print("-----------------------------")
                print(" Invalid choice!             ")
                print("-----------------------------\n")
                print()
