from method import *

print('---Library Management System---')
print('Hello, There!!.')
s = ' 1.Add Books\n 2.Remove Books\n 3.Display Books\n 4.Add Students\n 5.Remove Students\n 6.Display Students\n 7.Issue Book\n 8.Return Book\n 9.Issued Books\n 0.Exit'
print(s)
loop = 1
while(True):
    n = int(input('Enter Number for required Operation:\n'))
    match n:
        case 1:
            name = input('Enter Book name:\n')
            author = input('Enter Auther Name:\n')
            addBook(name, author)
        case 2:
            bId = int(input('Enter Book Id:\n'))
            removeBook(bId)
        case 3:
            books()
        case 4:
            name = input('Enter student name:\n')
            phn = int(input('Enter Mobile Number:\n'))
            address = input('Enter Address:\n')
            addStudent(name, phn, address)
        case 5:
            sId = int(input('Enter Student Id:\n'))
            removeStudent(sId)
        case 6:
            students()
        case 7:
            bId = int(input('Enter Book Id:\n'))
            sId = int(input('Enter Student Id:\n'))
            print('Date Formate: YYYY-MM-DD')
            issue_date = input('Enter issue date:\n')
            return_date = input('Enter return date:\n')
            issue(bId, sId, issue_date, return_date)
        case 8:
            bId = int(input('Enter Book Id:\n'))
            sId = int(input('Enter Student Id:\n'))
            return_book(bId, sId)
        case 9:
            issued_books()
        case 0:
            break
        case _:
            print('Enter a Valid number!!.')
            print('\U0001f60a')