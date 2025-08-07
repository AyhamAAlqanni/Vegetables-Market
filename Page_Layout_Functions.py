
from tkinter import *
from tkcalendar import DateEntry
from tkinter import messagebox
from datetime import datetime
from DataBase_Folder.DataBase_Functions import *
import webbrowser

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
        self.vegetable_name_entry = ""
        self.supplier_name_entry = ""
        self.price_entry = ""
        self.date_entry = ""
        self.vegetables = ""
        self.customer_name_entry = ""
        self.quantity_entry = ""
        self.total_price_entry = ""
        self.total_price_input = 0


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
        self.date_entry = DateEntry(self.frame, width = 18, background = "darkblue", foreground = "white", borderwidth = 2)
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
                                "refresh" : self.refresh_vegetables_list,
                                "show picture" : self.picture_button_handle,
                                "buy" : self.buy_button_handle,
                                "total price" : self.total_price_button_handle}

        # Add Button.
        add_button = Button(self.frame, text = button_name, width = 15, command = functions_dictionary[command])
        add_button.grid(row = row_number, column = column_number, pady = pady_number)
        add_button.bind("<Enter>", self.on_enter)
        add_button.bind("<Leave>", self.on_leave)


    def vegetables_list(self, row_number, column_number):

        # Scrollbar for usability
        scrollbar = Scrollbar(self.frame)
        scrollbar.grid(row = row_number, column = column_number + 3, rowspan = 6, sticky = "ns")

        # Vegetables List (Listbox)
        self.vegetables = Listbox(self.frame, height = 8, width = 60, border = 3, font = ("bold", 10), yscrollcommand = scrollbar.set)
        self.vegetables.grid(row = row_number, column = column_number, columnspan = 3, rowspan = 6, padx = 20)

        scrollbar.config(command = self.vegetables.yview)

        self.vegetables.bind("<<ListboxSelect>>", self.select_item)

        self.refresh_vegetables_list()

        # Header row
        #self.vegetables.insert(END, f"{'#':<6} {'Name':<15} {'Supplier':<20} {'Price/lb':<10} {'Date':<15}")
        #self.vegetables.insert(END, "*" * 80)  # Divider line

    def refresh_vegetables_list(self):

        self.vegetables.delete(0, END)

        for item in get_vegetables():

            # Data rows
            self.vegetables.insert(END, f"{item[0]} {"-"} {item[1]} {item[2]} {item[3]} {item[4]}") #{item[2]} {item[3]} {item[4]}
            #self.vegetables.insert(END, f"{item}") #{item[2]} {item[3]} {item[4]}

        # Sample row
        # vegetables_list.insert(END, f"{'Tomato':<20} {'Green Farm':<20} {'2.50':<10} {'2025-08-02'}")

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
        date = datetime.strptime(date, "%m/%d/%y").strftime("%Y-%m-%d") #%H:%M:%S

        vegetable_number = self.vegetables_list_counter()

        add_vegetable(vegetable_number, vegetable_name, supplier_name, float(price), date)

        self.refresh_vegetables_list()


    def clear_button_handle(self):
        
        self.vegetable_name_entry.delete(0, END)
        self.supplier_name_entry.delete(0, END)
        self.price_entry.delete(0, END)
        self.date_entry.set_date(datetime.today())


    def select_item(self, event):

        #print("select")

        try:

            global selected_item

            index = self.vegetables.curselection()[0] + 1

            selected_item = get_single_vegetable(index)

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

            #parts_list.bind("<<ListboxSelect>>", select_item)


    def update_button_handle(self):

        #print(selected_item[1])

        update_vegetable(selected_item[0], self.vegetable_name_entry.get(), self.supplier_name_entry.get(), 
                         self.price_entry.get(), self.date_entry.get())
        
        self.refresh_vegetables_list()

        #self.vegetables.bind("<<ListboxSelect>>", self.select_item)

    #def update_item():

    #db.update(selected_item[0], part_text.get(), customer_text.get(), retailer_text.get(), price_text.get())

    #populate_list()

    def delete_button_handle(self):

        delete_vegetable(selected_item[0])

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
            add_customer_transaction(transaction_number, customer_name, vegetable_name, supplier_name, quantity_value, total_price)
            messagebox.showinfo("Purchase Successful", "The transaction was completed successfully.")

        #self.total_price_entry.delete(0, END)
        #self.total_price_entry.insert(END, total_price)

        #add_customer_transaction(transaction_number, customer_name, vegetable_name, supplier_name, quantity, total_price)