import pandas as pd
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
        conn.close()
        return f'Student Successfully added with ID {res[0] - 1}'
    return "Connection to the database failed"

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
        conn.close()
        return f'Book Successfully added with ID {res[0] - 1}'
    return "Connection to the database failed"

def removeStudent(stud_id):
    conn = connectDB()
    if conn:
        cursor = conn.cursor()
        query = 'DELETE FROM STUDENT WHERE stud_id = %s;'
        args = (stud_id,)
        cursor.execute(query, args)
        conn.commit()
        conn.close()
        return 'Student removed successfully!!'
    return "Connection to the database failed"

def removeBook(book_id):
    conn = connectDB()
    if conn:
        cursor = conn.cursor()
        query = 'DELETE FROM BOOK WHERE book_id = %s;'
        args = (book_id,)
        cursor.execute(query, args)
        conn.commit()
        conn.close()
        return 'Book removed successfully!!'
    return "Connection to the database failed"

def students():
    conn = connectDB()
    if conn:
        cursor = conn.cursor()
        query = 'SELECT * FROM student'
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return pd.DataFrame(rows, columns=['ID', 'Name', 'Mobile No', 'Address'])
    return "Connection to the database failed"

def books():
    conn = connectDB()
    if conn:
        cursor = conn.cursor()
        query = 'SELECT * FROM book'
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return pd.DataFrame(rows, columns=['ID', 'Name', 'Author', 'Availability'])
    return "Connection to the database failed"

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
        conn.close()
        return f'Book issued Successfully added with ID {res[0] - 1}'
    return "Connection to the database failed"

def returnBook(book_id, stud_id):
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
        return 'Book Returned Successfully!!'
    return "Connection to the database failed"

def issuedBooks():
    conn = connectDB()
    if conn:
        cursor = conn.cursor()
        query = 'SELECT book_id, book.name, stud_id, student.name FROM book, student WHERE ROW(book_id, stud_id) IN (SELECT book_id, stud_id FROM issue_book WHERE status="In Issue");'
        cursor.execute(query)
        rows = cursor.fetchall()
        conn.close()
        return pd.DataFrame(rows, columns=['Book Id', 'Book Name', 'Student Id', 'Student Name'])
    return "Connection to the database failed"
