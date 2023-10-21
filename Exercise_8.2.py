'''Write a program that asks the user to enter
the area code (for example FI) and prints
out the airports located in that country
ordered by airport type. For example,
Finland has 65 small airports, 15 helicopter airports and so on.'''

import mysql.connector
my_db= mysql.connector.connect(
    host = 'localhost',
    port = '3306',
    database = 'flight_game',
    user = 'root',
    password = 'r00t',
    autocommit = True
)

area_code = input("Enter your desired area code: ")
sql = ("select name, type, iso_country from airport order by type;")
mycursor = my_db.cursor()
mycursor.execute(sql)
results = mycursor.fetchall()
if results:
    for name, type, iso_country in results:
        if area_code == iso_country:
            print(f'{name}:{type}')

else:
    print("Please enter a valid input. ")


mycursor.close()
my_db.close()
