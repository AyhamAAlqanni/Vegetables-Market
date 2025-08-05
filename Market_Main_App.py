
# "*" means importing everything from this module.
from tkinter import *
from tkinter import messagebox
from Page_Layout_Functions import PageFunctions


def vegetable_add_page(pages):

    add_page = PageFunctions(pages, "add")

    add_page.fields()

    add_page.buttons("Add Vegetable", 3, 0, 20, "add")
    add_page.buttons("Clear Fields", 3, 1, 0, "clear")
    add_page.buttons("Refresh List", 3, 2, 0, "refresh")

    add_page.vegetables_list(4, 0)


# Vegetable Update Page Setup.
def vegetable_update_page(pages):

    update_page = PageFunctions(pages, "update")

    update_page.fields()

    update_page.buttons("Update Vegetable", 3, 0, 20, "update")
    update_page.buttons("Clear Fields", 3, 1, 0, "clear")
    update_page.buttons("Refresh List", 3, 2, 0, "refresh")

    update_page.vegetables_list(4, 0)


# Vegetable Delete Page Setup.
def vegetable_delete_page(pages):

    delete_page = PageFunctions(pages, "delete")

    delete_page.fields()

    delete_page.buttons("Delete Vegetable", 3, 0, 20, "delete")
    delete_page.buttons("Clear Fields", 3, 1, 0, "clear")
    delete_page.buttons("Refresh List", 3, 2, 0, "refresh")

    delete_page.vegetables_list(4, 0)

    #add_page.add_button("Delete Vegetable", 3, 0, 20)
    #add_page.add_button("Clear Fields", 3, 1, 0)


# Hover effect functions.
def on_enter(event):
    event.widget['background'] = '#9a1717'
    event.widget['foreground'] = 'white'

def on_leave(event):
    event.widget['background'] = '#60CC80'
    event.widget['foreground'] = 'black'


# Show a given page/frame
def frame_display(frame):

    frame.tkraise()


# Function to create all pages
def create_pages(app):
    pages = {}

    for name in ["main", "list", "add", "update", "delete"]:
        page = Frame(app, bg="#e0ffe0")
        page.place(relwidth=1, relheight=1)  # Fill the entire window
        pages[name] = page

        # Simple label for each page
        label = Label(page, text=f"This is the {name.capitalize()} Page", font=("Arial", 20), bg="white")
        #label.grid()

        # Back button to return to main page
        if name != "main":
            Button(page, text="Back", command=lambda: frame_display(pages["main"])).grid(row = 0, column = 0)

    return pages


# Function to hold buttons inside a frame.
def buttons_frame(app, pages):

    # Create a frame to hold the buttons
    # button_frame = Frame(app)
    # button_frame.place(relx=0.5, rely=0.5, anchor=CENTER)  # Center the frame

    # Create a frame to hold the buttons
    button_frame = Frame(pages["main"], bg="#e0ffe0")
    button_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Common style for all buttons
    button_style = {
        "width": 20,
        "bd": 5,                    # Border width
        "relief": "raised",          # Border style (try: 'solid', 'groove', 'sunken', etc.)
        "background": "#60CC80",    # Background color
        "foreground": "black",          # Text color
        "activebackground": "#9a1717",  # Hover color
        "activeforeground": "white",
        "padx": 5,
        "pady": 5
    }

    # Buttons and their corresponding pages
    buttons = [
        ("Vegetables List", "list"),
        ("Add Vegetable", "add"),
        ("Update Vegetable", "update"),
        ("Delete Vegetable", "delete")
    ]

    for i, (text, page_name) in enumerate(buttons):
        btn = Button(button_frame, text=text, command=lambda p=page_name: frame_display(pages[p]), **button_style)
        btn.grid(row=i, column=0, pady=5)
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

    # Add buttons to the frame (centered)
    # Vegetables list button.
    # vegetable_list_button = Button(button_frame, text="Vegetables List", **button_style)
    # vegetable_list_button.grid(row=0, column=0, pady=5) 
    # vegetable_list_button.bind("<Enter>", on_enter)
    # vegetable_list_button.bind("<Leave>", on_leave)

    # Add vegetable button.
    # add_vegetable_button = Button(button_frame, text="Add Vegetable", **button_style)
    # add_vegetable_button.grid(row=1, column=0, pady=5)
    # add_vegetable_button.bind("<Enter>", on_enter)
    # add_vegetable_button.bind("<Leave>", on_leave)

    # Update vegetable button.
    # update_vegetable_button = Button(button_frame, text="Update Vegetable", **button_style)
    # update_vegetable_button.grid(row=2, column=0, pady=5)
    # update_vegetable_button.bind("<Enter>", on_enter)
    # update_vegetable_button.bind("<Leave>", on_leave)

    # Delete vegetable button.
    # delete_vegetable_button = Button(button_frame, text="Delete Vegetable", **button_style)
    # delete_vegetable_button.grid(row=3, column=0, pady=5)
    # delete_vegetable_button.bind("<Enter>", on_enter)
    # delete_vegetable_button.bind("<Leave>", on_leave)


# Main Function.
def main():

    # Creating window object.
    app = Tk()

    app.title("Vegetable Market")
    app.geometry("700x350")
    app.configure(background="#e0ffe0")  # Background color

    # buttons_frame(app)

    # Create all pages
    pages = create_pages(app)

    # Add main page buttons
    buttons_frame(app, pages)

    # Show main page initially
    frame_display(pages["main"])

    vegetable_add_page(pages)
    vegetable_update_page(pages)
    vegetable_delete_page(pages)

    # Starting Program.
    app.mainloop()


# Calling Main Function.
main()