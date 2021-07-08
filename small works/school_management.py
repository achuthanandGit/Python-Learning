student_list = [
    {'std_id': '1', 'name': 'Akhil', 'std' : '8', 'subjects' : {'Maths' : 45, 'Science' : 44, 'IT' : 50}},
    {'std_id': '2', 'name': 'Achu', 'std' : '9', 'subjects' : {'Maths' : 45, 'Science' : 44, 'IT' : 50}}
]

faculty_list = [
    {'fac_id':'1', 'name' : 'David', 'subject' : 'Maths'},
    {'fac_id':'2', 'name' : 'Priya', 'subject' : 'Science'},
    {'fac_id':'3', 'name' : 'Sreeja', 'subject' : 'IT'}
]

def show_students():
    print("\nStudents:")
    if student_list:
        for student in student_list:
            print(student)
    else:
        print('No Students. Please add a new student.')
        
def show_faculties():
    print("\nFaculties:")
    if faculty_list:
        for faculty in faculty_list:
            print(faculty)
    else:
        print('No faculties. Please add a new faculty.')

def get_student_details():
    is_valid_data = False

    id_list = []
    [id_list.append(student['std_id']) for student in student_list]

    std_id = input("Enter student ID: ").strip()
    name = input("Enter student name: ").strip()
    std = input("Enter student standard: ").strip()
    
    while not is_valid_data:
        if not std_id:
            std_id = input("Enter valid student ID: ").strip()
        elif std_id in id_list:
            std_id = input("Student ID already used. Enter new Student ID: ").strip()
        elif not name:
            name = input("Enter valid student name: ").strip()
        elif not std:
            std = input("Enter valid student standard: ").strip()
        else:
            is_valid_data = True

    return std_id, name, std

def get_faculty_details():
    is_valid_data = False

    id_list = []
    [id_list.append(faculty['fac_id']) for faculty in faculty_list]

    fac_id = input("Enter faculty ID: ").strip()
    name = input("Enter faculty name: ").strip()
    subject = input("Enter faculty subject: ").strip()

    while not is_valid_data:
        if not fac_id:
            fac_id = input("Enter valid faculty ID: ").strip()
        elif fac_id in id_list:
            fac_id = input("Faculty ID already used. Enter new faculty ID: ").strip()
        elif not name:
            name = input("Enter valid faculty name: ").strip()
        elif not subject:
            subject = input("Enter valid faculty subject: ").strip()
        else:
            is_valid_data = True

    return fac_id, name, subject,

def add_student():
    std_id, name, std =  get_student_details()
    student_list.append({'std_id': std_id, 'name':name, 'std': std, 'subjects' : {'Maths' : None, 'Science' : None, 'IT' : None}})
    print("Student added successfully.\n")

def add_faculty():
    fac_id, name, subject =  get_faculty_details()
    faculty_list.append({'std_id': fac_id, 'name':name, 'subject': subject})
    print("Faculty added successfully.\n")

def remove_student():
    data_to_remove = {}
    std_id = input("Enter student ID: ").strip()
    while not std_id:
        std_id = input("Enter valid student ID: ").strip()
    for student in student_list:
        if student['std_id'] == std_id:
            data_to_remove = student
            break

    if not data_to_remove:
        print('Student not found. Please try again with valid student ID.')
    else:
        student_list.remove(data_to_remove)
        print('Student removed succesfully. New student list: ')
        show_students()

def remove_faculty():
    data_to_remove = {}
    fac_id = input("Enter fcaulty ID: ").strip()
    while not fac_id:
        fac_id = input("Enter valid student ID: ").strip()

    for faculty in faculty_list:
        if faculty['fac_id'] == fac_id:
            data_to_remove = faculty
            break

    if not data_to_remove:
        print('Faculty not found. Please try again with valid faculty ID.')
    else:
        faculty_list.remove(data_to_remove)
        print('Faculty removed successfully. New Faculty list: ')
        show_faculties()

def update_student_mark():
    is_valid = False

    subject_list = ['Maths', 'Science', 'IT']
    id_list  = []
    [id_list.append(student['std_id']) for student in student_list]
    print(id_list)

    std_id = input("Enter student ID: ").strip()
    subject = input("Enter the subject ('Maths', 'Science', 'IT'): ").strip()
    mark = input("Enter mark: ").strip()

    while not is_valid:
        if (not std_id) or std_id not in id_list:
            std_id = input("Enter valid student ID: ").strip()
        elif (not subject) or subject not in subject_list:
            subject = input("Enter valid subject ('Maths', 'Science', 'IT'): ").strip()
        else:
            try:
                mark = int(mark)
                is_valid = True
            except ValueError:
                mark = input("Enter valid mark: ").strip()
            
    
    for student in student_list:
        if student['std_id'] == std_id:
            student['subjects'][subject] = mark

    print("Student mark update successfully.")

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
        show_students()
    elif choice =='2':
        show_faculties()
    elif choice == '3':
        add_student()
    elif choice == '4':
        remove_student()
    elif choice == '5':
        add_faculty()
    elif choice == '6':
        update_student_mark()
    else:
        'Enter valid choice'


def show_options():
    print('-----------------------------------------')
    print('School')
    print('-----------------------------------------')
    print('1. Show all students')
    print('2. Show all faculties')
    print('3. Add student')
    print('4. Remove Student')
    print('5. Add faculty')
    print('5. Remove faculty')
    print('6. Update student marks (Maths, Science, IT)')
    print('#. Exit')
    print('-----------------------------------------')

show_options()
con = 'y'

while con == 'y':
    choice = input('Enter a choice: ').strip()

    while validate_choice(choice) == 0:
        choice = input('Enter a valid choice: ').strip()
    
    navigate_choice(choice)
    con = input('\nDo you want to continue. y/n: ').strip().lower()