from db import *
from tabulate import tabulate

def addStudent(name, phno, address):
    conn = connectDB()
    if conn:
        cursor = conn.cursor()
        query = 'INSERT INTO STUDENT(name, phno, address) VALUES(%s, %s, %s);'
        args = (name, phno, address)
        cursor.execute(query, args)
        conn.commit()
        query = 'SELECT AUTO_INCREMENT FROM information_schema.Tables WHERE TABLE_SCHEMA = "lms" AND TABLE_NAME = "student";'
        cursor.execute(query)
        res = cursor.fetchone()
        print('Student Successfully added with ID', res[0] - 1)
        conn.close()

def addBook(name, author):
    conn = connectDB()
    if conn:
        cursor = conn.cursor()
        query = 'INSERT INTO BOOK(name, author, availability) VALUES(%s, %s, %s);'
        args = (name, author, 'Yes')
        cursor.execute(query, args)
        conn.commit()
        query = 'SELECT AUTO_INCREMENT FROM information_schema.Tables WHERE TABLE_SCHEMA = "lms" AND TABLE_NAME = "book";'
        cursor.execute(query)
        res = cursor.fetchone()
        print('Book Successfully added with ID', res[0] - 1)
        conn.close()

def removeStudent(stud_id):
    conn = connectDB()
    if conn:
        cursor = conn.cursor()
        query = 'DELETE FROM STUDENT WHERE stud_id = %s;'
        args = (stud_id,)
        cursor.execute(query, args)
        conn.commit()
        print('Student removed successfully!!.')
        conn.close()

def removeBook(book_id):
    conn = connectDB()
    if conn:
        cursor = conn.cursor()
        query = 'DELETE FROM BOOK WHERE book_id = %s;'
        args = (book_id,)
        cursor.execute(query, args)
        conn.commit()
        print('Book removed successfully!!.')
        conn.close()

def students():
    conn = connectDB()
    if conn:
        cursor = conn.cursor()
        query = 'SELECT * FROM student'
        cursor.execute(query)
        row = cursor.fetchall()
        print(tabulate(row, headers=['ID', 'Name', 'Mobile No', 'Address']))
        conn.close()

def books():
    conn = connectDB()
    if conn:
        cursor = conn.cursor()
        query = 'SELECT * FROM book'
        cursor.execute(query)
        row = cursor.fetchall()
        print(tabulate(row, headers=['ID', 'Name', 'Author', 'Availability']))
        conn.close()

def issue(book_id, stud_id, issue_date, return_date):
    conn = connectDB()
    if conn:
        cursor = conn.cursor()
        query = 'INSERT INTO issue_book (book_id, stud_id, issue_date, return_date, status) VALUES(%s, %s, %s, %s, %s);'
        args = (book_id, stud_id, issue_date, return_date, 'In Issue')
        cursor.execute(query, args)
        conn.commit()
        query = 'UPDATE book set availability = "No" WHERE book_id = %s'
        args = (book_id,)
        cursor.execute(query, args)
        conn.commit()
        query = 'SELECT AUTO_INCREMENT FROM information_schema.Tables WHERE TABLE_SCHEMA = "lms" AND TABLE_NAME = "issue_book";'
        cursor.execute(query)
        res = cursor.fetchone()
        print('Book issued Successfully added with ID', res[0] - 1)
        conn.close()

def return_book(book_id, stud_id):
    conn = connectDB()
    if conn:
        cursor = conn.cursor()
        query = 'UPDATE book set availability = "Yes" WHERE book_id = %s'
        args = (book_id,)
        cursor.execute(query, args)
        conn.commit()
        query = 'UPDATE issue_book set status = "Returned" WHERE book_id = %s and stud_id = %s'
        args = (book_id, stud_id)
        cursor.execute(query, args)
        conn.commit()
        conn.close()
        print('Book Returned Successfully!!.')

def issued_books():
    conn = connectDB()
    if conn:
        cursor = conn.cursor()
        query = 'select book_id, book.name, stud_id, student.name from book, student where ROW(book_id, stud_id) in (select book_id, stud_id from issue_book where status="In Issue");'
        cursor.execute(query)
        row = cursor.fetchall()
        print(tabulate(row, headers=['Book Id', 'Book Name', 'Student Id', 'Student Name']))
        conn.close()
