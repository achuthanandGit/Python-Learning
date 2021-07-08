import mysql.connector



cursor = cnx.cursor()
print('connection successful')

cursor.execute("USE {}".format('mysql_python'))
print('database use sucessfull')

cursor.execute("CREATE TABLE `STUDENTS` (`Rno` int(3) NOT NULL, `name` varchar(15) NOT NULL, `city` varchar(15) NOT NULL, PRIMARY KEY (`Rno`))")
print("Table created successfull")

cursor.close()
cnx.close()
print("Connection closed successfully")

