import tkinter as tk
from tkinter import ttk
from datetime import datetime
class CarRentalMenu:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AutoWave Rentals")
        self.root.geometry("700x350")
        self.root.attributes('-fullscreen', True)

        title_label = tk.Label(self.root, text="AutoWave Rentals", font=("Helvetica", 100),fg='black')
        title_label.pack(pady=20)

        customer_button = tk.Button(self.root, text="Customer Portal", command=self.open_customer_portal,font=("Helvetica", 50),fg='black')
        customer_button.place(x=530,y=300)



        admin_button = tk.Button(self.root, text="Admin Portal", command=self.open_admin_portal,activebackground='pink',font=("Helvetica", 50))
        admin_button.place(x=565,y=380)

        customer_button = tk.Button(self.root, text="Credits", command=self.credits,font=("Helvetica", 50))
        customer_button.place(x=620,y=460)

        exit_button = tk.Button(self.root, text="Exit", command=self.ex,font=("Helvetica", 50))
        exit_button.pack(pady=10)
        exit_button.place(x=660,y=540)


        self.root.mainloop()
    def ex(self):
        exit()

    def open_admin_portal(self):
        # instance of AdminPortalMenu and pass the callback function
        admin_menu = AdminPortalMenu(self.root, self.back_to_main_menu)

    def open_customer_portal(self):
        # instance of CustomerPortalMenu and pass the callback function, ughghghghghghghg im sleepy
        customer_menu = CustomerPortalMenu(self.root, self.back_to_main_menu)
    def credits(self):
        root = tk.Tk()
        title_label = tk.Label(root, text="Gitesh", font=("Helvetica", 60))
        title_label.pack(pady=20)

        title_label = tk.Label(root, text="Jafer", font=("Helvetica", 60))
        title_label.pack(pady=20)

        title_label = tk.Label(root, text="Nishanth reddy", font=("Helvetica", 60))
        title_label.pack(pady=20)

        title_label = tk.Label(root, text="Vishvas", font=("Helvetica", 60))
        title_label.pack(pady=20)

        title_label = tk.Label(root, text="George Lucas", font=("Helvetica", 60))
        title_label.pack(pady=20)



    def back_to_main_menu(self):
        # manu maximum
        self.root.deiconify()
class AdminPortalMenu:
    def __init__(self, parent, callback):
        self.parent = parent
        self.callback = callback

        self.root = tk.Tk()
        self.root.title("Admin Portal")


        title_label = tk.Label(self.root, text="Admin Portal", font=("Helvetica", 60),fg='black')
        title_label.pack(pady=20)

        title_label = tk.Label(self.root, text="", font=("Helvetica", 50))
        title_label.pack(pady=20)


        view_cars = tk.Button(self.root, text="view all vehicles", command=self.view_cars,bg='blue',font=("Helvetica", 50))
        view_cars.pack(pady=10)

        view_rented = tk.Button(self.root, text="view rented vehicles", command=self.view_rented,font=("Helvetica", 50))
        view_rented.pack(pady=10)

        update = tk.Button(self.root, text="update vehicle info", command=self.update,font=("Helvetica",50))
        update.pack(pady=10)



        back_button = tk.Button(self.root, text="Back", command=self.back_to_main_menu,font=("Helvetica",50))
        back_button.pack(pady=10)

        self.root.mainloop()

    def view_cars(self):
        view_all(Cars_list)

    def view_rented(self):
        view_rented(Cars_list)



    def update(self):
        update(Cars_list)

    def back_to_main_menu(self):
        #  back the main menu,less go indio disc is almost upon us
        self.root.destroy()
        self.parent.deiconify()
class CustomerPortalMenu:
    def __init__(self, parent, callback):
        self.parent = parent
        self.callback = callback

        self.root = tk.Tk()
        self.root.title("Customer Portal")


        title_label = tk.Label(self.root, text="Customer Portal",fg='black', font=("Helvetica", 60))
        title_label.pack(pady=20)
        title_label = tk.Label(self.root, text="", font=("Helvetica", 50))
        title_label.pack(pady=20)


        rent_vehicles_button = tk.Button(self.root, text="Rent Vehicles", command=self.rent_vehicles,font=("Helvetica", 50))
        rent_vehicles_button.pack(pady=10)

        # the Back button
        back_button = tk.Button(self.root, text="Back", command=self.back_to_main_menu,font=("Helvetica", 50))
        back_button.pack(pady=10)

        self.root.mainloop()


    def rent_vehicles(self):
         VehicleSelectionMenu(Cars_list)

    def back_to_main_menu(self):

        self.root.destroy()
        self.parent.deiconify()
class VehicleSelectionMenu:
    def __init__(self, tuples_list):
        self.root = tk.Tk()
        self.root.title("Vehicle Selection Menu")


        # Create a frame for headings with a black background
        heading_frame = tk.Frame(self.root, background='black')
        heading_frame.pack(side="top", fill="x")

        # Treeview widget
        columns = ("serial no.", "vehicle model", "color", "Type", "rent per day", "status", " ")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        self.tree.tag_configure('heading', foreground='blue')

        # column headings
        for col in columns:
            self.tree.heading(col, text=col, anchor="center")
            self.tree.column(col, width=100, anchor="center")
            self.tree.tag_configure('col', foreground='blue')# Adjust width as needed

        # Insert predetermined tuples into the table
        for tup in tuples_list:
            # Append an empty string to represent the "Rent" button
            self.tree.insert("", "end", values=list(tup) + [""], tags=tup)  # Using tags to store additional data

        # Configure the Rent button column with a button
        self.tree.column(" ", anchor="center", width=100)
        self.tree.heading(" ", text=" ", anchor="center")
        self.tree.bind("<ButtonRelease-1>", self.on_rent_button_click)

        # Back button to return to the main menu
        back_button = tk.Button(self.root, text="Back to Menu", command=self.root.destroy, font=("Helvetica", 50), bg='pink', fg='black')
        back_button.pack(pady=10)
        self.tree.tag_configure('heading', foreground='blue')

        self.tree.pack(pady=20)

        self.root.mainloop()
    def destr0y(self):
        self.root.destroy()
    def on_rent_button_click(self, event):
        item = self.tree.selection()
        if item:

            selected_tuple = self.tree.item(item, "values")[:-1]  # Exclude the last empty string

            # Check if the car is available or rented
            if selected_tuple[-1] == "Available":
                # Open a dialog for user input
                user_input_dialog = UserInputDialog(self.root, selected_tuple, self,VehicleSelectionMenu)


    def update_rented_status(self, selected_tuple):
        # Update the status in the Treeview
        item_id = self.get_item_id(selected_tuple)
        if item_id:
            self.tree.item(item_id, values=selected_tuple + ("Rented",))
            for index,i in enumerate(Cars_list):
                if i[1]==list(selected_tuple)[1]:
                    Cars_list[index][5]='Rented'
                    print('k')
                    print(Cars_list)
                    self.tree.item(item_id, values=selected_tuple)
                    self.destr0y()





    def get_item_id(self, selected_tuple):
        # Find the item ID in the Treeview based on the selected tuple
        for item_id in self.tree.get_children():
            values = self.tree.item(item_id, "values")[:-1]
            if values == selected_tuple:
                return item_id
        return None
    def update(self,tuples_list):
        for tup in tuples_list:
            # Append an empty string to represent the "Rent" button
            self.tree.insert("", "end", values=list(tup) + ["", ], tags=tup)
class UserInputDialog:
    def __init__(self, parent, vehicle_data, menu_instance,VehicleSelectionMenu):
        self.parent = parent
        self.menu_instance = menu_instance
        self.root = tk.Toplevel(parent)
        self.root.title("User Input Dialog")
        self.vehicle_data = vehicle_data

        # Create and configure widgets for user input
        # (Entry widgets, labels, ettcc)
        name_label = tk.Label(self.root, text="", font=("Helvetica", 180), fg='black')
        name_label.pack()
        # Example: Entry widget for name
        name_label = tk.Label(self.root, text="Name:", font=("Helvetica", 50),fg='black')
        name_label.pack()

        self.name_entry = tk.Entry(self.root,width=23,font=("Helvetica", 30))
        self.name_entry.pack()

        # Example: Entry widget for phone number
        phone_label = tk.Label(self.root, text="Phone Number:", font=("Helvetica", 50),fg='black')
        phone_label.pack()

        self.phone_entry = tk.Entry(self.root,width=23,font=("Helvetica", 30))
        self.phone_entry.pack()

        # Example: Entry widget for number of days
        days_label = tk.Label(self.root, text="Number of Days:", font=("Helvetica", 50),fg='black')
        days_label.pack()

        self.days_entry = tk.Entry(self.root,width=23,font=("Helvetica", 30))
        self.days_entry.pack()

        # Example: Checkbutton for driver
        self.driver_var = tk.IntVar()
        driver_checkbox = tk.Checkbutton(self.root, text="Driver Needed", variable=self.driver_var, font=("Helvetica", 20),fg='black')
        driver_checkbox.pack()

        # Example: Button to confirm rental
        confirm_button = tk.Button(self.root, text="Confirm Rental", command=self.show_confirmation_page, font=("Helvetica", 20),fg='black')
        confirm_button.pack()

    def show_confirmation_page(self):
        # Create a new window to display the confirmation page
        confirmation_window = tk.Toplevel(self.root)
        confirmation_window.title("Confirmation Page")
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time_label = tk.Label(confirmation_window, text=f"Date and Time: {current_time}")
        time_label.pack()

        user_label = tk.Label(confirmation_window, text="", font=("Helvetica", 30))
        user_label.pack()

        # Display user information
        user_label = tk.Label(confirmation_window, text="receipt",font=("Helvetica", 30))
        user_label.pack()

        # Display user details
        user_details = [
            ("Name", self.name_entry.get()),
            ("Phone Number", self.phone_entry.get()),
            ("Number of Days", self.days_entry.get()),
            ("Driver Needed", "Yes" if self.driver_var.get() else "No")
        ]

        for label, value in user_details:
            user_info_label = tk.Label(confirmation_window, text=f"{label}: {value}")
            user_info_label.pack()




        # Display each piece of vehicle information
        for i, col_name in enumerate(["vehicle id", "name and model ", "Color", "status", "daily rent"]):
            info_label = tk.Label(confirmation_window, text=f"{col_name}: {self.vehicle_data[i]}")
            info_label.pack()
        cost=int((self.days_entry.get()))*int((self.vehicle_data[4]))

        if self.driver_var.get()=='Yes':
            cost=cost+1000
        print(cost)
        tx=('amount payable:'+str(cost))
        vehicle_label = tk.Label(confirmation_window, text=tx)
        vehicle_label.pack()

        # Example: Button to confirm the rent
        confirm_rent_button = tk.Button(confirmation_window, text="Confirm Rental", command=self.on_confirm_rent)
        confirm_rent_button.pack()

        # Example: Button to go back
        back_button = tk.Button(confirmation_window, text="Cancel", command=self.back_to_menu)
        back_button.pack()


    def on_confirm_rent(self):
        # Close the user input dialog and return to the main menu
        self.root.destroy()
        self.menu_instance.root.deiconify()
        self.menu_instance.update_rented_status(self.vehicle_data)
        VehicleSelectionMenu(Cars_list)



    def back_to_menu(self):
        # Close the user input dialog and return to the main menu
        self.root.destroy()
        self.menu_instance.root.deiconify()
class view_rented:
    def __init__(self, tuples_list):
        self.root = tk.Tk()
        self.root.title("all rented vehicles")

        # Create and configure t
        columns = ("serial no.", "vehicle model", "color", "Type", "rent per day", "status", "Rent")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")

        # Set column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")  # Adjust width as needed

        # Insert predetermined tuples
        for tup in tuples_list:
            if tup[5]!="Available":
            # Append an empty string to represent the "Rent" button
                 self.tree.insert("", "end", values=list(tup) + ["",], tags=tup)  # Using tags to store additional data

        # Configure the Rent button column with a button
        self.tree.column("Rent", anchor="center", width=100)
        self.tree.heading("Rent", text="Rent", anchor="center")


        # Back button to return to the main menu
        back_button = tk.Button(self.root, text="Back to Menu", command=self.root.destroy)
        back_button.pack(pady=10)

        self.tree.pack(pady=20)

        self.root.mainloop()
class view_all:
    def __init__(self, tuples_list):
        self.root = tk.Tk()
        self.root.title("all rented vehicles")


        columns = ("serial no.", "vehicle model", "color", "Type", "rent per day", "status", " ")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")

        # Set column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")

        # Insert into the table
        for tup in tuples_list:
            self.tree.insert("", "end", values=list(tup) + ["",], tags=tup)

        # Back button to return to the main menu
        back_button = tk.Button(self.root, text="Back to Menu", command=self.root.destroy)
        back_button.pack(pady=10)

        self.tree.pack(pady=20)

        self.root.mainloop()
class update:
    def __init__(self, tuples_list):
        self.root = tk.Tk()
        self.root.title("Vehicle Selection Menu")


        self.tuples_list = tuples_list

        columns = ("serial no.", "vehicle model", "color", "Type", "rent per day", "status")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")

        # Set column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")


        for tup in self.tuples_list:
            self.tree.insert("", "end", values=tup, tags=tup)

        #
        add_button = tk.Button(self.root, text="Add Entry", command=self.add_entry)
        add_button.pack(pady=5)

        remove_button = tk.Button(self.root, text="Remove Entry", command=self.remove_entry)
        remove_button.pack(pady=5)

        # Create and configure Back button
        back_button = tk.Button(self.root, text="Back", command=self.root.destroy)
        back_button.pack(pady=10)

        self.tree.pack(pady=20)

        self.root.mainloop()

    def add_entry(self):

        entry_window = tk.Toplevel(self.root)
        entry_window.title("Add Entry")

        entry_labels = ["serial no.", "vehicle model", "color", "Type", "rent per day", "status"]

        entry_vars = []
        entry_entries = []
        for label in entry_labels:
            tk.Label(entry_window, text=label).pack()
            entry_var = tk.StringVar()
            entry_entry = tk.Entry(entry_window, textvariable=entry_var)
            entry_entry.pack()
            entry_vars.append(entry_var)
            entry_entries.append(entry_entry)

        add_button = tk.Button(entry_window, text="Add Entry",
                               command=lambda: self.on_add_entry(entry_vars, entry_entries, entry_window))
        add_button.pack()

    def on_add_entry(self, entry_vars, entry_entries, entry_window):
        new_entry = list(entry_entry.get() for entry_entry in entry_entries)
        if all(new_entry):
            self.tuples_list.append(new_entry)
            self.update_tree()
            entry_window.destroy()

    def remove_entry(self):
        selected_item = self.tree.selection()
        if selected_item:
            selected_index = self.tree.index(selected_item)
            del self.tuples_list[selected_index]
            self.update_tree()

    def update_tree(self):
        # Clear existing items in Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Add updated entries to Treeview
        for tup in self.tuples_list:
            self.tree.insert("", "end", values=tup, tags=tup)
Cars_list = [
    [0,'Chervrolet C1 Corvette','pink','Car',12000,'Rented'],
    [1,"BMW M3 GTR E46", "Silver", 'Car', 3000, "Available"],
    [2, "Bat mobile", "Black", 'Car', 9800, "Rented"],
    [3, "Aston Martin DB5", "Silver", 'Car', 6000, "Available"],
    [4,"Millennium Falcon",'White','Corellian light freighter',9009,'Rented'],
    [5,'Fire Bolt','Brown','Broom',9888,'Available'],
    [6,'Rocii','silver','Light Frigate',7878,'Rented'],
    [7,'Oro Jackson','Red','Ship',87878,'Available'],
    [8,'Neiman Marcus LE','Silver','Bike',34988,'Rented'],
    [9,'Nissan Skyline','White','Car',98787,'Available'],
    [10,'Nissan 240SX','orange','Car',8874,'Rented'],
    [11,'Koridon','Red','Agais',8999,'Rented']

]
CarRentalMenu()