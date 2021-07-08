product_list = [
    {'product_id':'1', 'name':'Egg', 'units_available': 100, 'rate': 4},
    {'product_id':'2', 'name':'Banana', 'units_available': 30, 'rate': 10},
    {'product_id':'3', 'name':'Apple', 'units_available': 150, 'rate': 20},
    {'product_id':'4', 'name':'Orange', 'units_available': 100, 'rate': 23}
]

def show_products():
    for product in product_list:
        print(product)

def remove_product():
    data_to_remove = {}
    product_id = input("Enter the product ID: ").strip()
    id_list = []
    [id_list.append(product['product_id']) for product in product_list]

    while (not product_id) or product_id not in id_list:
        product_id = input("Enter valid product ID: ").strip()

    for product in product_list:
        if product['product_id'] == product_id:
            data_to_remove = product
            break

    product_list.remove(data_to_remove)
    print('Product details succesfully removed. New product list:')
    show_products()

def add_product():
    is_valid = False
    id_list = []
    [id_list.append(product['product_id']) for product in product_list]

    product_id = input("Enter the product ID: ").strip()
    name = input("Enter the product name: ").strip()
    units_available = input("Enter units available: ").strip()
    rate = input("Enter the rate per unit: ").strip()

    while not is_valid:
        if not product_id:
            product_id = input("Enter valid product ID: ").strip()
        elif product_id in id_list:
            product_id = input("Product ID already used. Enter new product ID: ").strip()
        elif not name:
            name = input("Enter valid product name: ").strip()
        elif not units_available:
            units_available = input("Enter valid units available: ").strip()
        elif not rate:
            rate = input("Enter valid rate per unit: ").strip()
        else:
            try:
                units_available = int(units_available)
            except ValueError:
                units_available = input("Enter valid units available: ").strip()

            try:
                rate = int(rate)
            except ValueError:
                rate = input("Enter valid rate per unit: ").strip()

            is_valid = True
    
    product_list.append({'product_id':product_id, 'name':name, 'units_available': units_available, 'rate': rate})
    print("\nProduct added successfully.\n")
    show_products()

def buy_product():
    is_valid = False

    product_id = input("Enter the product ID: ").strip()
    units = input("Enter the units: ").strip()

    id_list = []
    [id_list.append(product['product_id']) for product in product_list]

    while not is_valid:
        if (not product_id) or product_id not in id_list:
            product_id = input("Enter valid product ID: ").strip()
        else:
            try:
                units = int(units)
                is_valid = True
            except ValueError:
                units = input("Enter valid units: ").strip()

    rate_to_pay = 0
    for product in product_list:
        if product['product_id'] == product_id:
            rate_to_pay = rate_to_pay + (product['rate'] * units)
            product['units_available'] = product['units_available'] - units
    
    print("Product bought successfully. Amount to pay: "+str(rate_to_pay))
    
def validate_choice(choice):
    if choice == '#':
        exit()
    value = 0
    try:
        value = int(choice)
    except ValueError:
        return 0
    if value < 1 or value > 4:
        return 0
    return 1

def navigate_choice(choice):
    if choice == '1':
        show_products()
    elif choice =='2':
        add_product()
    elif choice == '3':
        remove_product()
    elif choice == '4':
        buy_product()
    else:
        'Enter valid choice'

def show_options():
    print('--------------------------------------------')
    print('Super Market')
    print('--------------------------------------------')
    print('1. List all products')
    print('2. Add product')
    print('3. Remove product')
    print('4. Buy Product')
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
    con = input('\nDo you want to continue. y/n: ').strip().lower()