
from tkinter import *
from tkcalendar import DateEntry

class PageLayout:

    def __init__(self, pages, page_name):
        # Create a frame to hold the buttons
        self.frame = Frame(pages[page_name], bg="#e0ffe0")
        self.frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.label_style = {
            "font": ("Bold", 14),
            "background": "#e0ffe0",
            "foreground": "black"
        }
        self.user_input_text = ""


    def add_field(self, label_text, row_number, column_number, pady_number, is_date = False):

        field_label = Label(self.frame, text = label_text, pady = pady_number, **self.label_style)
        field_label.grid(row = row_number, column = column_number)

        if is_date:

            field_entry = DateEntry(self.frame, width = 18, background = "darkblue", foreground = "white", borderwidth = 2)

        else:

            self.user_input_text = StringVar()
            field_entry = Entry(self.frame, textvariable = self.user_input_text)

        field_entry.grid(row = row_number, column = column_number + 1)

        return field_entry


    def add_button(self, button_name, row_number, column_number, pady_number, command=None):

         # Hover effect functions.
        def on_enter(event):
            event.widget['background'] = '#9a1717'
            event.widget['foreground'] = 'white'

        def on_leave(event):
            event.widget['background'] = '#60CC80'
            event.widget['foreground'] = 'black'

        button = Button(self.frame, text = button_name, width = 15, command = command)
        button.grid(row = row_number, column = column_number, pady = pady_number)
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)


    def vegetables_list(self, row_number, column_number):

        # Scrollbar for usability
        scrollbar = Scrollbar(self.frame)
        scrollbar.grid(row=row_number, column=column_number + 3, rowspan=6, sticky="ns")

        # Vegetables List (Listbox)
        vegetables_list = Listbox(self.frame, height = 8, width = 60, border = 3, font = ("bold", 10), yscrollcommand=scrollbar.set)
        vegetables_list.grid(row = row_number, column = column_number, columnspan = 3, rowspan = 6, padx = 20)

        scrollbar.config(command=vegetables_list.yview)

        return vegetables_list