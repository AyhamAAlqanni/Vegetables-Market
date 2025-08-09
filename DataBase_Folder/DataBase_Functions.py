

# This Python script defines several functions (Create, Read, Update, Delete) for interacting with a MySQL tables. 
# It uses the cursor and database objects imported from a module called DataBase.py.

# cursor: Used to execute SQL statements.
# database: The MySQL connection object, used to commit changes.
from DataBase_Folder.DataBase_Setup import cursor, database
from mysql.connector import Error


# Purpose: Adds a new row to the vegetables table.
def add_vegetable(vegetable_number, vegetable_name, supplier_name, price, added_date):

    try:

        sql = "INSERT INTO vegetables(vegetable_number, vegetable_name, supplier_name, price, added_date) VALUES (%s, %s, %s, %s, %s)"

        cursor.execute(sql, (vegetable_number, vegetable_name, supplier_name, price, added_date))

        database.commit()
        
    except Error as err:

        print(f"Error Adding Vegetable: {err}")


# Purpose: Fetches all vegetables entries, ordered by oldest first.
# row[1] refers to the text column (since row[0] is vegetable_number).
# NOTE: It doesn't print all details, only the text.
def get_vegetables():

    try:

        sql = ("SELECT * FROM vegetables ORDER BY vegetable_number ASC")

        cursor.execute(sql)

        result = cursor.fetchall()

        return list(result)

    except Error as err:

        print(f"Error Getting Vegetables: {err}")


# Purpose: Retrieves a single vegetable by vegetable number.
# fetchone() returns a single row (as a tuple).
def get_single_vegetable(vegetable_number):

    try:

        sql = ("SELECT * FROM vegetables WHERE vegetable_number = %s")

        cursor.execute(sql, (vegetable_number,))

        result = cursor.fetchone()

        if result != None:

            return result

    except Error as err:

        print(f"Error Getting Vegetable Number: {err}") 


# Purpose: Updates vegetable's entire row by its vegetable number.
def update_vegetable(vegetable_number, vegetable_name, supplier_name, price, added_date):

    sql = ("UPDATE vegetables SET vegetable_name = %s, supplier_name = %s, price = %s, added_date = %s WHERE vegetable_number = %s")

    cursor.execute(sql, (vegetable_name, supplier_name, price, added_date, vegetable_number))

    database.commit() 


# Purpose: Deletes vegetable's from the table by its vegetable number.
def delete_vegetable(vegetable_number):

    sql = ("DELETE FROM vegetables WHERE vegetable_number = %s")

    cursor.execute(sql, (vegetable_number,))

    database.commit()


# Purpose: Adds a new row to the customers table.
def add_customer_transaction(transaction_id, customers_name, vegetable_name, supplier_name, quantity, total_price):

    try:

        sql = "INSERT INTO customers(transaction_id, customers_name, vegetable_name, supplier_name, quantity, total_price) VALUES (%s, %s, %s, %s, %s, %s)"

        cursor.execute(sql, (transaction_id, customers_name, vegetable_name, supplier_name, quantity, total_price))

        database.commit()
        
    except Error as err:

        print(f"Error Adding Customer: {err}")


# Purpose: Fetches all customers entries, ordered by oldest first.
# row[1] refers to the text column (since row[0] is transaction_id).
# NOTE: It doesn't print all details, only the text.
def get_customers():

    try:

        sql = ("SELECT * FROM customers ORDER BY transaction_id ASC")

        cursor.execute(sql)

        result = cursor.fetchall()

        return list(result)

    except Error as err:

        print(f"Error Getting Customers: {err}")


# Purpose: Fetches all customers entries, ordered by customer's name.
# row[1] refers to the text column (since row[0] is transaction_id).
def get_customer_by_name(customers_name):

    try:

        sql = ("SELECT * FROM customers WHERE customers_name IN (%s)")

        cursor.execute(sql, (customers_name,))

        result = cursor.fetchall()

        return list(result)

    except Error as err:

        print(f"Error Getting Customer's Name: {err}")


# Purpose: Fetches all customers entries, ordered by vegetable's name.
# row[1] refers to the text column (since row[0] is transaction_id).
def get_customer_by_vegetable_name(vegetable_name):

    try:

        sql = ("SELECT * FROM customers WHERE vegetable_name IN (%s)")

        cursor.execute(sql, (vegetable_name,))

        result = cursor.fetchall()

        return list(result)

    except Error as err:

        print(f"Error Getting Vegetable's Name: {err}")


# Purpose: Fetches all customers entries, ordered by supplier's name.
# row[1] refers to the text column (since row[0] is transaction_id).
def get_customer_by_supplier_name(supplier_name):

    try:

        sql = ("SELECT * FROM customers WHERE supplier_name IN (%s)")

        cursor.execute(sql, (supplier_name,))

        result = cursor.fetchall()

        return list(result)

    except Error as err:

        print(f"Error Getting Supplier's Name: {err}")