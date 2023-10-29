import streamlit as st
from method import *  

st.title('Library Management System')

operation = st.selectbox('Choose an Operation', [
    'Add Book', 'Remove Book', 'Display Books',
    'Add Student', 'Remove Student', 'Display Students',
    'Issue Book', 'Return Book', 'Issued Books'
])

def display_output(data):
    if isinstance(data, str):
        st.success(data)
    elif isinstance(data, pd.DataFrame):
        if data.empty:
            st.error("Operation failed or no data to display")
        else:
            st.table(data)
    else:
        st.error("Unsupported data type")

def add_book():
    with st.form('Add Book'):
        name = st.text_input('Enter Book Name')
        author = st.text_input('Enter Author Name')
        submitted = st.form_submit_button('Submit')
        if submitted:
            result = addBook(name, author)
            display_output(result)

def remove_book():
    with st.form('Remove Book'):
        book_id = st.number_input('Enter Book ID', min_value=1, format='%d')
        submitted = st.form_submit_button('Submit')
        if submitted:
            result = removeBook(book_id)
            display_output(result)

def add_student():
    with st.form('Add Student'):
        name = st.text_input('Enter Student Name')
        phone = st.text_input('Enter Phone Number')
        address = st.text_input('Enter Address')
        submitted = st.form_submit_button('Submit')
        if submitted:
            result = addStudent(name, phone, address)
            display_output(result)

def remove_student():
    with st.form('Remove Student'):
        student_id = st.number_input('Enter Student ID', min_value=1, format='%d')
        submitted = st.form_submit_button('Submit')
        if submitted:
            result = removeStudent(student_id)
            display_output(result)

def issue_book():
    with st.form('Issue Book'):
        book_id = st.number_input('Enter Book ID', min_value=1, format='%d')
        student_id = st.number_input('Enter Student ID', min_value=1, format='%d')
        issue_date = st.date_input('Enter Issue Date')
        return_date = st.date_input('Enter Return Date')
        submitted = st.form_submit_button('Submit')
        if submitted:
            result = issue(book_id, student_id, issue_date, return_date)
            display_output(result)

def return_book():
    with st.form('Return Book'):
        book_id = st.number_input('Enter Book ID', min_value=1, format='%d')
        student_id = st.number_input('Enter Student ID', min_value=1, format='%d')
        submitted = st.form_submit_button('Submit')
        if submitted:
            result = returnBook(book_id, student_id)
            display_output(result)

if operation == 'Add Book':
    add_book()
elif operation == 'Remove Book':
    remove_book()
elif operation == 'Display Books':
    books_data = books()
    display_output(books_data)
elif operation == 'Add Student':
    add_student()
elif operation == 'Remove Student':
    remove_student()
elif operation == 'Display Students':
    students_data = students()
    display_output(students_data)
elif operation == 'Issue Book':
    issue_book()
elif operation == 'Return Book':
    return_book()
elif operation == 'Issued Books':
    issued_books_data = issuedBooks()
    display_output(issued_books_data)

if __name__ == '__main__':
    st.sidebar.info('Library Management System')
