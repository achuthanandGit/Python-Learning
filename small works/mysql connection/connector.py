import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta


def get_connection(config):
    try:
        cnx = mysql.connector.connect(**config)
        return cnx
    except:
        print("MySQL Error Connection")
        return None

def create_database(cursor, DB_NAME):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

def use_database(cursor, DB_NAME):
    try:
        cursor.execute("USE {}".format(DB_NAME))
        print("Database use successful")
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(DB_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(cursor, DB_NAME)
            print("Database {} created successfully.".format(DB_NAME))
            cnx.database = DB_NAME
        else:
            print(err)
            exit(1)

def create_tables(cursor, TABLES):
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

    



config = {
  'user': 'root',
  'password': '2100910',
  'host': '127.0.0.1',
}

cnx = get_connection(config)
cursor = cnx.cursor()
use_database(cursor, 'mysql_python')

TABLES = {}
TABLES['employees'] = (
    "CREATE TABLE `employees` ("
    "  `emp_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
    "  `hire_date` date NOT NULL,"
    "  PRIMARY KEY (`emp_no`)"
    ") ENGINE=InnoDB")

create_tables(cursor, TABLES)


add_employee_query = "INSERT INTO employees (birth_date, first_name, last_name, gender, hire_date) VALUES (%s, %s, %s, %s, %s)"
data_employee = (date(1977, 6, 14), 'Geert', 'Vanderkelen', 'M', datetime.now().date() )

try:
    cursor.execute(add_employee_query, data_employee)
    cnx.commit()
    print("Employee added successfully")
except:
    print("Query execution error, try again.")


get_employee_query = ("SELECT first_name, last_name, hire_date FROM employees "
         "WHERE birth_date BETWEEN %s AND %s")
hire_start = date(1977, 1, 1)
hire_end = date(1977, 12, 31)

try:
    cursor.execute(get_employee_query, (hire_start, hire_end))
    for (first_name, last_name, hire_date) in cursor:
        print("{}, {} born on {:%d %b %Y}".format(last_name, first_name, hire_date))
except:
    print("Query execution error, try again.")


cursor.close()
cnx.close()