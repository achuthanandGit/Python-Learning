import os

def create_file(name, extension):
    try:
        f = open(name+extension, 'x')
        f.close()
        print(name+extension+' file created successfully.')
    except FileExistsError:
        print('File already exists')

def delete_file(name, extension):
    try:
        os.remove(name+extension)
        print('File deleted successfully.')
    except FileNotFoundError:
        print('File not exists')
        

def open_file(name, extension, mode):
    try:
        print("Opening file in +"+ mode +" mode.")
        f = open(name+extension, mode)
    except FileNotFoundError:
        print('File not exists. Creating new file.')
        create_file(name, extension)
        f = open(name+extension, mode)
    print('File Name: ' + f.name + ', Mode: ' + f.mode)
    f.close()

def read_display(name, extension, mode):
    try:
        f = open(name+extension, mode)
        data = f.read()
        if data:
            print('Data: \n'+ data)
        else:
            print('Empty file.')
        f.close()
    except FileNotFoundError:
        print("File not exists.")
    except IOError:
        print("Error reading file. Try again.")

def read_write_display(name, extension, mode):
    try:
        print("Opening file in read and write mode.")
        f = open(name+extension, mode)
        data = f.read()
        if data:
            print('Data: \n'+ data)
        else:
            print('Empty file.')
        write_data = input("Enter the data to write into: ")
        while write_data == "":
            write_data = input("Enter valid data to write into.")
        f.write(write_data)    
        f.close()
        read_display(name, extension, 'r')
    except FileNotFoundError:
        print("File not exists.")
    except IOError:
        print("Error reading file. Try again.")
    

def validate_choice(choice):
    if choice == '#':
        exit()
    value = 0
    try:
        value = int(choice)
    except ValueError:
        return 0
    if value < 1 or value > 6:
        return 0
    return 1

def navigate_choice(choice):
    if choice == '1':
        create_file(file_name, extension)
    elif choice =='2':
        delete_file(file_name, extension)
    elif choice == '3':
        open_file(file_name, extension, 'r')
    elif choice == '4':
        open_file(file_name, extension, 'w')
    elif choice == '5':
        read_display(file_name, extension, 'r')
    elif choice == '6':
        read_write_display(file_name, extension, 'r+')
    else:
        'Enter valid choice'

def show_options():
    print('--------------------------------------------')
    print('File Operations')
    print('--------------------------------------------')
    print('1. Create file')
    print('2. Delete file')
    print('3. Open file with read mode')
    print('4. Open file with write mode')
    print('5. Open file, read data and display')
    print('6. Open file, read & display, write & display')
    print('#. Exit')
    print('--------------------------------------------')
    print('\n')
    

show_options()
con = 'y'

while con == 'y':
    
    valid_entries = False
    valid_file_types = ['.txt', '.bin']
    file_name = input("Enter the file name: ").strip()
    extension = input("Enter the file type (.txt or .bin): ").strip()
    
    while not valid_entries:
        if not file_name:
            file_name = input("Enter valid file name: ").strip()
        elif extension not in valid_file_types:
            extension = input("Enter valid file type (.txt or .bin): ").strip()
        else:
            valid_entries = True
            
    choice = input('Enter the choice: ').strip()

    while validate_choice(choice) == 0:
        choice = input('Enter a valid choice: ').strip()

    navigate_choice(choice)

    con = input('\nDo you want to continue. y/n: ').strip().lower()