
from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox
from datetime import datetime
from DataBase_Folder.DataBase_Functions import *
import webbrowser
from tkinter import ttk # Treeview.

class PageFunctions:

    def __init__(self, pages, page_name):

        # Create a frame to hold the buttons
        self.frame = Frame(pages[page_name], bg="#e0ffe0")
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.label_style = {
            "font": ("Bold", 14),
            "background": "#e0ffe0",
            "foreground": "black"
        }

        self.calendar_style = {
            "width": 18, 
            "background": "darkgreen", 
            "foreground": "white", 
            "borderwidth": 2,
            "selectbackground": "#F9F990",   # Selected date background in calendar
            "selectforeground": "black", # Selected date text
            "headersbackground": "#75DA6E", # Day-of-week header background
            "headersforeground": "#000000",# Day-of-week header text
            "weekendbackground": "#53B64B",  # Weekend cell background
            "weekendforeground": "#000000"      # Weekend cell text
        }

        self.button_style = {
        "width": 15,
        "bd": 2,                    # Border width
        "relief": "raised",          # Border style (try: 'solid', 'groove', 'sunken', etc.)
        "background": "#60CC80",    # Background color
        "foreground": "black",          # Text color
        "activebackground": "#9a1717",  # Hover color
        "activeforeground": "white"
        }

        # Create a style object
        self.style = ttk.Style()

        # 1. Set the overall theme to something that allows custom colors
        self.style.theme_use("default")  # Other options: 'clam', 'alt', 'classic'

        # 2. Style the headings (header row)
        self.style.configure(
            "Treeview.Heading",
            background="#4CAF50",  # Green header
            foreground="black",    # White text
            font=("Arial", 8, "bold"),
            padding=[0, 5]  # Wider and taller header
        )

        # 3. Style the table cells
        self.style.configure(
            "Treeview",
            background="white",
            foreground="black",
            rowheight=20,
            fieldbackground="white",
            font=("Arial", 10)
        )

        # 4. Add striped rows
        self.style.map(
            "Treeview",
            background=[("selected", "#F9F990")],  # Yellow when selected 
            foreground=[("selected", "black")]
        )
        
        self.vegetable_name_entry = ""
        self.supplier_name_entry = ""
        self.price_entry = ""
        self.date_entry = ""
        self.vegetables = ""
        self.customer_name_entry = ""
        self.quantity_entry = ""
        self.total_price_entry = ""
        self.total_price_input = 0
        self.transactions = ""


    def fields(self):

        # Vegetable Name Field.
        vegetable_name_label = Label(self.frame, text = "Vegetable Name", pady = 20, **self.label_style)
        vegetable_name_label.grid(row = 1, column = 0)
        vegetable_name_input = StringVar()
        self.vegetable_name_entry = Entry(self.frame, textvariable = vegetable_name_input)
        self.vegetable_name_entry.grid(row = 1, column = 1)

        # Supplier Name Field.
        supplier_name_label = Label(self.frame, text = "Supplier Name", **self.label_style)
        supplier_name_label.grid(row = 1, column = 2)
        supplier_name_input = StringVar()
        self.supplier_name_entry = Entry(self.frame, textvariable = supplier_name_input)
        self.supplier_name_entry.grid(row = 1, column = 3)

        # Price Field.
        price_label = Label(self.frame, text = "Price/lb", **self.label_style)
        price_label.grid(row = 2, column = 0)
        price_input = StringVar()
        self.price_entry = Entry(self.frame, textvariable = price_input)
        self.price_entry.grid(row = 2, column = 1)

        # Date Field.
        date_label = Label(self.frame, text = "Date", **self.label_style)
        date_label.grid(row = 2, column = 2)
        self.date_entry = DateEntry(self.frame, **self.calendar_style, style = "Custom.DateEntry")
        self.date_entry.grid(row = 2, column = 3)


    def buy_fields(self):

        # Customer Name Field.
        customer_name_label = Label(self.frame, text = "Customer Name", pady = 20, **self.label_style)
        customer_name_label.grid(row = 1, column = 0)
        customer_name_input = StringVar()
        self.customer_name_entry = Entry(self.frame, textvariable = customer_name_input)
        self.customer_name_entry.grid(row = 1, column = 1)

        # Vegetable Name Field.
        vegetable_name_label = Label(self.frame, text = "Vegetable Name", pady = 20, **self.label_style)
        vegetable_name_label.grid(row = 1, column = 2)
        vegetable_name_input = StringVar()
        self.vegetable_name_entry = Entry(self.frame, textvariable = vegetable_name_input)
        self.vegetable_name_entry.grid(row = 1, column = 3)

        # Quantity Field.
        quantity_label = Label(self.frame, text = "Quantity", **self.label_style)
        quantity_label.grid(row = 2, column = 0)
        quantity_input = StringVar()
        self.quantity_entry = Entry(self.frame, textvariable = quantity_input)
        self.quantity_entry.grid(row = 2, column = 1)

        # Total Price Field.
        total_price_label = Label(self.frame, text = "Total Price", **self.label_style)
        total_price_label.grid(row = 2, column = 2)
        self.total_price_input = StringVar()
        self.total_price_entry = Entry(self.frame, textvariable = self.total_price_input)
        self.total_price_entry.grid(row = 2, column = 3)


    # Hover effect functions.
    def on_enter(self, event):
        event.widget['background'] = '#9a1717'
        event.widget['foreground'] = 'white'

    def on_leave(self, event):
        event.widget['background'] = '#60CC80'
        event.widget['foreground'] = 'black'


    # def add_button(self, button_name, row_number, column_number, pady_number, command=None):
    def buttons(self, button_name, row_number, column_number, pady_number, command=None):

        functions_dictionary = {"add" : self.add_button_handle,
                                "clear" : self.clear_button_handle,
                                "update" : self.update_button_handle,
                                "delete" : self.delete_button_handle,
                                "refresh vegetable" : self.refresh_vegetables_list,
                                "show picture" : self.picture_button_handle,
                                "buy" : self.buy_button_handle,
                                "total price" : self.total_price_button_handle,
                                "search" : self.search_button_handle,
                                "refresh transaction" : self.refresh_transactions_list,
                                "transactions clear" : self.transaction_clear_button_handle}

        # Add Button.
        add_button = Button(self.frame, text = button_name, command = functions_dictionary[command], **self.button_style)
        add_button.grid(row = row_number, column = column_number, pady = pady_number)
        add_button.bind("<Enter>", self.on_enter)
        add_button.bind("<Leave>", self.on_leave)


    def vegetables_list(self, row_number, column_number):

        # Scrollbar for usability
        self.scrollbar = Scrollbar(self.frame)
        self.scrollbar.grid(row = row_number, column = column_number + 3, rowspan = 6, sticky = "ns")

        # Define columns for the treeview
        columns = ("VEGETABLE#", "VEGETABLE", "SUPPLIER", "PRICE/LB", "ADDED DATE")

        # Create Treeview
        self.vegetables_tree = ttk.Treeview(self.frame, columns = columns, show = "headings", height = 7, yscrollcommand = self.scrollbar.set)
        self.vegetables_tree.grid(row = row_number, column = column_number, columnspan = 3, rowspan = 6, padx = 20)

        self.scrollbar.config(command = self.vegetables_tree.yview)

        # Set column headings
        for col in columns:

            self.vegetables_tree.heading(col, text = col)
            self.vegetables_tree.column(col, width = 100, anchor = "center")

        # Apply striped rows manually
        self.vegetables_tree.tag_configure("oddrow", background = "#f2f2f2")  # Light gray
        self.vegetables_tree.tag_configure("evenrow", background = "white")
        self.vegetables_tree.tag_configure("hoverrow", background = "#F9F990")  # Hover highlight color

        # Hover event binding
        self.vegetables_tree.bind("<Motion>", self.vegetable_list_row_hover)
        self.hovered_item = None  # Keep track of which row is currently hovered

        self.vegetables_tree.selection_remove(self.vegetables_tree.selection())
        self.vegetables_tree.focus("")

        self.refresh_vegetables_list()

        self.vegetables_tree.bind("<<TreeviewSelect>>", self.select_item)

        # Vegetables List (Listbox)
        #self.vegetables = Listbox(self.frame, height = 8, width = 60, border = 3, font = ("bold", 10), yscrollcommand = scrollbar.set)
        #self.vegetables.grid(row = row_number, column = column_number, columnspan = 3, rowspan = 6, padx = 20)

        #scrollbar.config(command = self.vegetables.yview)

        #self.vegetables.bind("<<ListboxSelect>>", self.select_item)

        #self.refresh_vegetables_list()

        # Header row
        #self.vegetables.insert(END, f"{'#':<6} {'Name':<15} {'Supplier':<20} {'Price/lb':<10} {'Date':<15}")
        #self.vegetables.insert(END, "*" * 80)  # Divider line

    def refresh_vegetables_list(self):

        # Clear existing rows
        for item in self.vegetables_tree.get_children():

            self.vegetables_tree.delete(item)

        # Insert updated data with alternating row colors
        for i, vegetable in enumerate(get_vegetables()):

            vegetable = list(vegetable)

            vegetable[4] = vegetable[4].date().strftime("%m-%d-%y")

            tag = "evenrow" if i % 2 == 0 else "oddrow"

            self.vegetables_tree.insert("", "end", values = vegetable, tags=(tag,))

        # Insert updated data
        #for vegetable in get_vegetables():

            #vegetable = list(vegetable)

            #vegetable[4] = vegetable[4].date().strftime("%m-%d-%y")

            #self.vegetables_tree.insert("", "end", values = vegetable)


    def vegetables_list_counter(self):

        vegetables_counter = 0

        for vegetable in get_vegetables():

            vegetables_counter += 1

        return vegetables_counter + 1

        
    def add_button_handle(self):
        
        vegetable_name = self.vegetable_name_entry.get()
        supplier_name = self.supplier_name_entry.get()
        price = self.price_entry.get()
        date = self.date_entry.get()

        # 1. Check for empty fields
        if vegetable_name == "" or supplier_name == "" or price == "" or date == "":

            messagebox.showerror("Required Fields!", "Please Include All Fields")

            return
        
        # 2. Check if price is a valid float
        try:
            
            price_value = float(price)
            
            if price_value < 0:
                
                raise ValueError
        
        except ValueError:
            
            messagebox.showerror("Input Error", "Price must be a positive number.")
            
            return

        # Convert 'MM/DD/YYYY' or 'DD/MM/YYYY' to 'YYYY-MM-DD HH:MM:SS'
        #date = datetime.strptime(date, "%m/%d/%y").strftime("%Y-%m-%d") #%H:%M:%S

        # Convert selected date + current time to full timestamp
        selected_date = datetime.strptime(self.date_entry.get(), "%m/%d/%y").date()
        current_time = datetime.now().time()
        full_datetime = datetime.combine(selected_date, current_time)

        date = full_datetime.strftime("%Y-%m-%d %H:%M:%S")

        vegetable_number = self.vegetables_list_counter()

        add_vegetable(vegetable_number, vegetable_name.capitalize(), supplier_name.capitalize(), float(price), date)

        self.vegetables_tree.selection_remove(self.vegetables_tree.selection())
        self.vegetables_tree.focus("")

        self.refresh_vegetables_list()


    def clear_button_handle(self):

        try:
        
            self.vegetable_name_entry.delete(0, END)
            self.supplier_name_entry.delete(0, END)
            self.price_entry.delete(0, END)
            self.date_entry.set_date(datetime.today())

        except AttributeError:

            pass


    def select_item(self, event):

        try:

            """ selected_row = self.vegetables_tree.focus()
        
            if not selected_row:  # No focus
                return
            
            if not self.vegetables_tree.exists(selected_row):  # Item deleted
                return

            values = self.vegetables_tree.item(selected_row, "values")
            if not values:
                return """

            global selected_item

            # Get selected row in the treeview
            selected_row = self.vegetables_tree.focus()
            values = self.vegetables_tree.item(selected_row, "values")

            if not values:
                return  # No selection made
            
            #print(values)

            # values is a tuple like: (id, name, supplier, price, date)
            selected_item = get_single_vegetable(int(values[0]))  # Assuming values[0] is the ID

            self.vegetable_name_entry.delete(0, END)
            self.vegetable_name_entry.insert(END, selected_item[1])

            self.supplier_name_entry.delete(0, END)
            self.supplier_name_entry.insert(END, selected_item[2])

            self.price_entry.delete(0, END)
            self.price_entry.insert(END, selected_item[3])

            self.date_entry.delete(0, END)
            self.date_entry.insert(END, selected_item[4])

        except IndexError:
            pass

        except AttributeError:
            pass

        #print("select")

        #try:

            #global selected_item

            #index = self.vegetables.curselection()[0] + 1

            #selected_item = get_single_vegetable(index)

            #self.vegetable_name_entry.delete(0, END)
            #self.vegetable_name_entry.insert(END, selected_item[1])

            #self.supplier_name_entry.delete(0, END)
            #self.supplier_name_entry.insert(END, selected_item[2])

            #self.price_entry.delete(0, END)
            #self.price_entry.insert(END, selected_item[3])

            #self.date_entry.delete(0, END)
            #self.date_entry.insert(END, selected_item[4])

        #except IndexError:

            #pass

        #except AttributeError:

            #pass

            #parts_list.bind("<<ListboxSelect>>", select_item)


    def update_button_handle(self):

        #print(selected_item[1])

        update_vegetable(selected_item[0], self.vegetable_name_entry.get().capitalize(), self.supplier_name_entry.get().capitalize(), 
                         self.price_entry.get(), self.date_entry.get())
        
        self.vegetables_tree.selection_remove(self.vegetables_tree.selection())
        self.vegetables_tree.focus("")
        
        self.refresh_vegetables_list()

        #self.vegetables.bind("<<ListboxSelect>>", self.select_item)

    #def update_item():

    #db.update(selected_item[0], part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())

    #populate_list()

    def delete_button_handle(self):

        delete_vegetable(selected_item[0])

        self.vegetables_tree.selection_remove(self.vegetables_tree.selection())
        self.vegetables_tree.focus("")

        self.refresh_vegetables_list()


    def picture_button_handle(self):

        url = "https://www.pexels.com/search/" + selected_item[1] # https://google.com/search?q=

        webbrowser.get().open(url)


    def customers_list_counter(self):

        customers_counter = 0

        for customer in get_customers():

            customers_counter += 1

        return customers_counter + 1
    

    def total_price_button_handle(self):

        quantity = self.quantity_entry.get()
        total_price = float(selected_item[3])

        # 2. Check if quantity is a valid float
        try:
            
            quantity_value = float(quantity)
            
            if quantity_value < 0:
                
                raise ValueError
        
        except ValueError:
            
            messagebox.showerror("Input Error", "Price must be a positive number.")
            
            return
        
        total_price *= float(quantity)

        self.total_price_entry.delete(0, END)
        self.total_price_entry.insert(END, total_price)


    def buy_button_handle(self):

        customer_name = self.customer_name_entry.get()
        vegetable_name = self.vegetable_name_entry.get()
        supplier_name = selected_item[2]
        quantity = self.quantity_entry.get()
        total_price = float(selected_item[3])

        # 1. Check for empty fields
        if customer_name == "" or vegetable_name == "" or quantity == "":

            messagebox.showerror("Required Fields!", "Please Include All Fields")

            return
        
        # 2. Check if quantity is a valid float
        try:
            
            quantity_value = float(quantity)
            
            if quantity_value < 0:
                
                raise ValueError
        
        except ValueError:
            
            messagebox.showerror("Input Error", "Price must be a positive number.")
            
            return

        transaction_number = self.customers_list_counter()

        total_price *= float(quantity)

        # 3. Confirmation message before completing the purchase
        confirm = messagebox.askyesno("Confirm Purchase", 
        f"Do you want to buy {quantity_value} lb of {vegetable_name} from {supplier_name} for a total of ${total_price:.2f}?")

        if confirm:
            add_customer_transaction(transaction_number, customer_name.capitalize(), vegetable_name.capitalize(), 
                                     supplier_name.capitalize(), float(quantity_value), float(total_price))
            messagebox.showinfo("Purchase Successful", "The transaction was completed successfully.")

        #self.total_price_entry.delete(0, END)
        #self.total_price_entry.insert(END, total_price)

        #add_customer_transaction(transaction_number, customer_name, vegetable_name, supplier_name, quantity, total_price)


    def transactions_list(self, row_number, column_number):

        # Scrollbar
        self.transactions_scrollbar = Scrollbar(self.frame)
        self.transactions_scrollbar.grid(row = row_number, column = column_number + 3, rowspan = 6, sticky = "ns")

        # Define columns for the treeview
        columns = ("TRANS#", "CUSTOMER", "VEGETABLE", "SUPPLIER", "QUANTITY", "PRICE", "DATE")

        # Create Treeview
        self.transactions_tree = ttk.Treeview(self.frame, columns=columns, show='headings', height=7, yscrollcommand=self.transactions_scrollbar.set)
        self.transactions_tree.grid(row = row_number, column = column_number, columnspan = 3, rowspan = 6, padx = 20, pady = 5)

        self.transactions_scrollbar.config(command = self.transactions_tree.yview)

        # Set column headings
        for col in columns:

            self.transactions_tree.heading(col, text = col)
            self.transactions_tree.column(col, width = 80, anchor = "center")

        # Apply striped rows manually
        self.transactions_tree.tag_configure("oddrow", background = "#f2f2f2")  # Light gray
        self.transactions_tree.tag_configure("evenrow", background = "white")
        self.transactions_tree.tag_configure("hoverrow", background = "#F9F990")  # Hover highlight color

        # Hover event binding
        self.transactions_tree.bind("<Motion>", self.transaction_list_row_hover)
        self.hovered_item = None  # Keep track of which row is currently hovered

        self.refresh_transactions_list()


    def refresh_transactions_list(self):

        # Clear existing rows
        for item in self.transactions_tree.get_children():

            self.transactions_tree.delete(item)

        # Insert updated data with alternating row colors
        for i, transaction in enumerate(get_customers()):

            transaction = list(transaction)

            transaction[6] = transaction[6].date().strftime("%m-%d-%y")

            tag = "evenrow" if i % 2 == 0 else "oddrow"

            self.transactions_tree.insert("", "end", values = transaction, tags=(tag,))

            #transaction = list(transaction)

            #transaction[6] = transaction[6].date().strftime("%m-%d-%y")

            #self.transactions_tree.insert("", "end", values = transaction) 


    def transaction_list_row_hover(self, event):

        row_id = self.transactions_tree.identify_row(event.y)

        if row_id != self.hovered_item:

            # Restore the old row's original color
            if self.hovered_item:

                index = self.transactions_tree.index(self.hovered_item)
                original_tag = "evenrow" if index % 2 == 0 else "oddrow"
                self.transactions_tree.item(self.hovered_item, tags=(original_tag,))

            # Apply hover highlight to the new row
            if row_id:

                self.transactions_tree.item(row_id, tags=("hoverrow",))

            self.hovered_item = row_id


    """ def vegetable_list_row_hover(self, event):

        row_id = self.vegetables_tree.identify_row(event.y)

        if row_id != self.hovered_item:

            # Restore the old row's original color
            if self.hovered_item:

                index = self.vegetables_tree.index(self.hovered_item)
                original_tag = "evenrow" if index % 2 == 0 else "oddrow"
                self.vegetables_tree.item(self.hovered_item, tags=(original_tag,))

            # Apply hover highlight to the new row
            if row_id:
                
                self.vegetables_tree.item(row_id, tags=("hoverrow",))

            self.hovered_item = row_id """
    
    def vegetable_list_row_hover(self, event):
        
        row_id = self.vegetables_tree.identify_row(event.y)

        if row_id != self.hovered_item:
            # Restore the old row's original color if it still exists
            if self.hovered_item and self.vegetables_tree.exists(self.hovered_item):
                index = self.vegetables_tree.index(self.hovered_item)
                original_tag = "evenrow" if index % 2 == 0 else "oddrow"
                self.vegetables_tree.item(self.hovered_item, tags=(original_tag,))

            # Apply hover highlight to the new row if it exists
            if row_id and self.vegetables_tree.exists(row_id):
                self.vegetables_tree.item(row_id, tags=("hoverrow",))

            self.hovered_item = row_id


    def transaction_fields(self):

        # Customer Name Field.
        customer_name_label = Label(self.frame, text = "Customer Name", pady = 20, **self.label_style)
        customer_name_label.grid(row = 1, column = 0)
        customer_name_input = StringVar()
        self.customer_name_entry = Entry(self.frame, textvariable = customer_name_input)
        self.customer_name_entry.grid(row = 1, column = 1)

        # Vegetable Name Field.
        vegetable_name_label = Label(self.frame, text = "Vegetable Name", pady = 20, **self.label_style)
        vegetable_name_label.grid(row = 1, column = 2)
        vegetable_name_input = StringVar()
        self.vegetable_name_entry = Entry(self.frame, textvariable = vegetable_name_input)
        self.vegetable_name_entry.grid(row = 1, column = 3)

        # Supplier Name Field.
        supplier_name_label = Label(self.frame, text = "Supplier Name", **self.label_style)
        supplier_name_label.grid(row = 2, column = 0)
        supplier_name_input = StringVar()
        self.supplier_name_entry = Entry(self.frame, textvariable = supplier_name_input)
        self.supplier_name_entry.grid(row = 2, column = 1)


    def search_button_handle(self):

        customer_name = self.customer_name_entry.get()
        vegetable_name = self.vegetable_name_entry.get()
        supplier_name = self.supplier_name_entry.get()

        if customer_name != "" or vegetable_name != "" or supplier_name != "":

            # Clear existing rows
            for item in self.transactions_tree.get_children():

                self.transactions_tree.delete(item)

            if customer_name != "":

                # Insert updated data with alternating row colors
                for i, transaction in enumerate(get_customer_by_name(customer_name)):

                    transaction = list(transaction)

                    transaction[6] = transaction[6].date().strftime("%m-%d-%y")

                    tag = "evenrow" if i % 2 == 0 else "oddrow"

                    self.transactions_tree.insert("", "end", values = transaction, tags=(tag,))

            if vegetable_name != "":

                # Insert updated data with alternating row colors
                for i, transaction in enumerate(get_customer_by_vegetable_name(vegetable_name)):

                    transaction = list(transaction)

                    transaction[6] = transaction[6].date().strftime("%m-%d-%y")

                    tag = "evenrow" if i % 2 == 0 else "oddrow"

                    self.transactions_tree.insert("", "end", values = transaction, tags=(tag,))

            if supplier_name != "":

                # Insert updated data with alternating row colors
                for i, transaction in enumerate(get_customer_by_supplier_name(supplier_name)):

                    transaction = list(transaction)

                    transaction[6] = transaction[6].date().strftime("%m-%d-%y")

                    tag = "evenrow" if i % 2 == 0 else "oddrow"

                    self.transactions_tree.insert("", "end", values = transaction, tags=(tag,))

        else:

            messagebox.showerror("Required Fields!", "Please Include One Field At Least!")

            return
        

    def transaction_clear_button_handle(self):

        try:
            
            self.customer_name_entry.delete(0, END)
            self.vegetable_name_entry.delete(0, END)
            self.supplier_name_entry.delete(0, END)

        except AttributeError:

            pass
