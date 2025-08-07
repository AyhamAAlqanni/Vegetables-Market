
import mysql.connector                      # Imports the MySQL connector module to interact with MySQL databases.
from mysql.connector import errorcode       # Imports symbolic error codes used to handle specific MySQL errors.
from DataBase_Setup import cursor                 

# Defines the name of the database to be created or used.
DATABASE_NAME = "vegetablemarket"

# Initializes an empty dictionary to store SQL table definitions.
TABLES = {}

# Adds a table definition for a table named vegetables.
TABLES["vegetables"] = (
    "CREATE TABLE `vegetables` ("
    "`vegetable_number` INT(11) NOT NULL,"
    "`vegetable_name` VARCHAR(250) NOT NULL,"
    "`supplier_name` VARCHAR(250) NOT NULL,"
    "`price` FLOAT NOT NULL,"
    "`added_date` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    "PRIMARY KEY (`vegetable_number`)"
    ") ENGINE=InnoDB"
)

# Adds a table definition for a table named customers.
TABLES["customers"] = (
    "CREATE TABLE `customers` ("
    "`transaction_id` INT(11) NOT NULL,"
    "`customers_name` VARCHAR(250) NOT NULL,"
    "`vegetable_name` VARCHAR(250) NOT NULL,"
    "`supplier_name` VARCHAR(250) NOT NULL,"
    "`quantity` FLOAT NOT NULL,"
    "`total_price` FLOAT NOT NULL,"
    "`buy_date` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    "PRIMARY KEY (`transaction_id`)"
    ") ENGINE=InnoDB"
)


# Executes a SQL command to create the database if it doesn't already exist.
def create_database():

    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME} DEFAULT CHARACTER SET 'utf8'")

    print("Database {} Has Been Created!".format(DATABASE_NAME))


def create_tables():

    cursor.execute("USE {}".format(DATABASE_NAME))      # Sets the current active database to bankDB.

    # Loops through the TABLES dictionary to get each table’s SQL definition.
    for table_name in TABLES:           

        table_description = TABLES[table_name]

        # Tries to execute the SQL command to create the table.
        # Displays a message indicating the table being created.
        try:

            cursor.execute(table_description)

            print("Created Table ({}) ".format(table_name), end = "")

        # Catches errors from the MySQL connector:
        # If the table already exists, prints a message.
        # Otherwise, prints the error message.
        except mysql.connector.Error as err:

            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:

                print("Table Already Exists")

            else:

                print(err.msg)


# DataBase Main Function.
def database_main():

    # Calling create_database Function.
    # Creates the database if it doesn’t already exist.
    create_database()

    # Calling create_tables Function.
    # Creates the table inside that database.
    create_tables()


# Calling database_main Function.
database_main()