
book_list = [
    {'name':'Mathematics', 'is_available': True},
    {'name':'English', 'is_available': True},
    {'name':'Science', 'is_available': True},
    {'name':'Malayalam', 'is_available': True}
]

def add_book(book):
    book_list.append(book)

def show_books():
    print('--------------------------------------------')
    print('Books in the Library')
    print('--------------------------------------------')
    for book in book_list:
        print(book['name'] + ' ---- ' + ('available' if book['is_available'] else 'not available'))

def donate_book():
    name = input('Enter the book name: ')
    add_book({'name':name, 'is_available':True})
    print('Donation successfull')
    print('\nUpdated Library data:')
    show_books()

def lent_book():
    show_books()
    is_lent_success = False
    name = input('Enter the book name to lent: ').strip()
    for book in book_list:
        if name.lower() == book['name'].lower() and book['is_available']:
            book['is_available'] = False
            is_lent_success = True
            break
    if not is_lent_success:
        print('Entered book not available')
    else:
        print('Lenting successful')
        print('\nUpdated Library data:')
        show_books()

def return_book():
    name = input('Enter the book name to return: ').strip()
    is_return_success = False
    for book in book_list:
        if name.lower() == book['name'].lower() and not book['is_available']:
            book['is_available'] = True
            is_return_success = True
            break
    if not is_return_success:
        print('Invalid book name/Book already returned')
    else:
        print('Return successfull')
        print('\nUpdated Library data:')
        show_books()

def validate_choice(choice):
    if choice == '#':
        exit()
    value = 0
    try:
        value = int(choice)
    except ValueError:
        return 0
    if value < 1 or value >4:
        return 0
    return 1

def navigate_choice(choice):
    if choice == '1':
        show_books()
    elif choice =='2':
        donate_book()
    elif choice == '3':
        lent_book()
    elif choice == '4':
        return_book()
    else:
        'Enter valid choice'

def show_options():
    print('--------------------------------------------')
    print('LIBRARY')
    print('--------------------------------------------')
    print('1. List all books')
    print('2. Donate a book')
    print('3. Lent a book')
    print('4. Return a book')
    print('#. Exit')
    print('--------------------------------------------')
    print('\n')


show_options()
con = 'y'

while con == 'y':
    choice = input('Enter a choice: ').strip()

    while validate_choice(choice) == 0:
        choice = input('Enter a valid choice: ').strip()

    navigate_choice(choice)
    con = input('Do you want to continue. y/n: ').strip().lower()

    
    


    


    


    