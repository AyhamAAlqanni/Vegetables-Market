

# This Python script defines several functions (Create, Read, Update, Delete) for interacting with a MySQL tables. 
# It uses the cursor and database objects imported from a module called DataBase.py.

# cursor: Used to execute SQL statements.
# database: The MySQL connection object, used to commit changes.
from DataBase_Setup import cursor, database
from mysql.connector import Error


# Purpose: Adds a new row to the vegetables table.
def add_user(vegetable_number, vegetable_name, supplier_name, price, added_date):

    try:

        sql = "INSERT INTO vegetables(vegetable_number, vegetable_name, supplier_name, price, added_date) VALUES (%s, %s, %s, %s, %s)"

        cursor.execute(sql, (vegetable_number, vegetable_name, supplier_name, price, added_date))

        database.commit()
        
    except Error as err:

        print(f"Error Adding Vegetable: {err}")


# Purpose: Adds a new row to the transactions table.
""" def add_transaction(user_account_number, transaction_type, amount):

    try:

        sql = "INSERT INTO transactions(user_account_number, transaction_type, amount) VALUES (%s, %s, %s)"

        cursor.execute(sql, (user_account_number, transaction_type, amount))

        database.commit()
        
    except Error as err:

        print(f"Error Adding Transaction: {err}") """


# Purpose: Fetches all users entries, ordered by newest first.
# row[1] refers to the text column (since row[0] is id).
# NOTE: It doesn't print all details, only the text.
""" def get_users():

    try:

        sql = ("SELECT * FROM users ORDER BY balance DESC")

        cursor.execute(sql)

        result = cursor.fetchall()

        return list(result)

    except Error as err:

        print(f"Error Getting Users: {err}") """


# Purpose: Retrieves a single user by account number.
# fetchone() returns a single row (as a tuple).
""" def get_user_id(account_number):

    try:

        sql = ("SELECT * FROM users WHERE account_number = %s")

        cursor.execute(sql, (account_number,))

        result = cursor.fetchone()

        if result != None:

            return result[0]

    except Error as err:

        print(f"Error Getting User ID: {err}") """


# Purpose: Retrieves a user's transactions by account number.
# fetchone() returns a single row (as a tuple).
""" def get_user_transactions(account_number):

    try:

        sql = ("SELECT * FROM transactions WHERE user_account_number = %s ORDER BY transaction_date ASC")

        cursor.execute(sql, (account_number,))

        result = cursor.fetchall()

        if result != None:

            return result

    except Error as err:

        print(f"Error Getting Transactions: {err}") """


# Purpose: Retrieves a single user intire information by account number.
# fetchone() returns a single row (as a tuple).
""" def get_user(account_number):

    try:

        sql = ("SELECT * FROM users WHERE account_number = %s")

        cursor.execute(sql, (account_number,))

        result = cursor.fetchone()

        if result != None:

            return list(result)

    except Error as err:

        print(f"Error Getting User: {err}") """


# Purpose: Updates user's status by its account number.
""" def update_user_status(account_number, status):

    sql = ("UPDATE users SET status = %s WHERE account_number = %s")

    cursor.execute(sql, (status, account_number))

    database.commit() """

# Purpose: Updates user's balance by its account number.
""" def update_user_balance(account_number, balance):

    sql = ("UPDATE users SET balance = %s WHERE account_number = %s")

    cursor.execute(sql, (balance, account_number))

    database.commit() """