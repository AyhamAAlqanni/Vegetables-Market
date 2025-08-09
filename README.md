# 🥦 Vegetable Market Management System

# 📌 Overview

The Vegetable Market Management System is a Python-based desktop application that helps manage a vegetable shop’s inventory, customers, and transactions.
It uses:
1. Tkinter for the graphical user interface (GUI)
2. MySQL for storing data
3. PIL (Pillow) for image handling
This project is ideal for small market owners who need a lightweight system to track stock, sales, and suppliers.

# ✨ Features

- Inventory Management
    1. Add, view, and update vegetables.
    2. Track suppliers and prices.
- Customer Transactions
    1. Record purchases with quantity and total price.
    2. Automatically add timestamps to transactions.
- GUI Navigation
    1. Back buttons for easy navigation between pages.
    2. Simple, clean Tkinter layout.
- Database-Driven
    1. Persistent storage using MySQL.
    2. Tables automatically created if they don’t exist.

# 🛠️ Requirements

- Make sure you have the following installed:
    1. Python 3.8+
    2. MySQL Server
    3. Python Packages: pip install mysql-connector-python pillow

# ⚙️ Setup Instructions

1. Clone the Repository.
2. Configure Database Connection.
- In DataBase_Setup.py, set your MySQL credentials.
3. Create Database & Tables.
- Run: python DataBase_Create.py
- This will:
    1. Create the database vegetablemarket (if it doesn’t exist)
    2. Create the vegetables and customers tables
4. Run the Application.
- Run: python main.py

# 📎 Author
Developed by Ayham Alqanni