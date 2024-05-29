'''
frontend.py:

    Importing Libraries:

        The code imports necessary libraries json and tkinter.

    Global Variables:

        Global variables such as user, user_type, person, teacher, ug, pg, and login_attempts are declared.

    Function Definitions:

        Functions like set_page_data, create_entry, set_edit_page_data, handle_unsuccessful_login, delete_user, showStatusLabel, hideStatusLabel, and clear_input are defined.

        set_page_data(user) is a function for displaying user profile information.
        set_edit_page_data(user) is a function for editing user profile information.
        handle_unsuccessful_login(username) is a function for handling unsuccessful login attempts.
        delete_user(username) is a function for deleting user accounts. User is removed from the database.
        showStatusLabel(message) is a function for displaying status messages.
        hideStatusLabel(label) is a function for hiding status messages.
        clear_input() is a function for clearing entry fields and setting comboboxes to their default values.
        delete_account(user) is a function for deleting user accounts.
        addUser() is a function for adding new user accounts. User is added into the database.
        on_user_type_change(event) is a function for handling user type changes for first combobox.
        on_user_type_change2(event) is a function for handling user type changes for second combobox.
        signuppage() is a function for displaying sign-up page.
        signinpage() is a function for displaying sign-in page.
        signin() is a function for signing in.
        signout() is a function for signing out.
        editprofile(user) is a function for editing user profile.
        saveprofile() is a function for saving user profile. Changes are pushed to the database.

    User Interface (UI) Setup:

        The code creates the main tkinter.Tk window and sets up frames for various sections like sign-up, sign-in, user profile and edit profile.
        Entry widgets, labels, comboboxes, and buttons are placed within these frames for user interaction.

    User Authentication:

        There are functions for signing up, signing in, and handling unsuccessful login attempts.
        The code checks user types (Teacher/Student) and specific program types (Undergraduate/Postgraduate) during sign-up and sign-in.

    Profile Display and Editing:

        User profile information is displayed using labels.
        There is an edit profile feature with corresponding entry widgets for modifying user data.

    Buttons for Navigation:

        Buttons like "Edit," "Sign Out," and "Delete Account" provide user navigation options.

    Event Handling:

        The code binds functions to events, such as combobox selection changes.

    Layout Management:

        The code uses grid layout for organizing UI components within frames.
'''

import pickle
import tkinter as tk
from tkinter import ttk
from backend import *

#utils--------------------------------------------------------------------------
global user, user_type, person, teacher, ug, pg, login_attempts
user = {}
user_type = "Undergraduate"
person = Person("John", 20, 1, "b")
teacher = Teacher("John", 20, 1, "b", "Maths", 2, 3, 4, 5, 6)
ug = Undergraduate("Luna", 20, 2, "a", "Maths", 2, 3, 4, 5, 6)
pg = Postgraduate("Cena", 20, 3, "c", "Maths", 2, 3, 4, 5, 6, 1)
login_attempts = {}

def set_page_data(user):
    page_username_var.set(user["name"])
    page_age_var.set(user["age"])
    page_id_var.set(user["id"])
    if "specialization" in user:
        page_specialization_var.set(user["specialization"])
    if "experience" in user:
        page_experience_var.set(user["experience"])
    if "projects" in user:
        page_projects_var.set(user["projects"])
    if "achievements" in user:
        page_achievements_var.set(user["achievements"])
    if "education" in user:
        page_education_var.set(user["education"])
    if "doctoral_advisor" in user:
        page_doctoral_advisor_var.set(user["doctoral_advisor"])
    if "program" in user:
        page_program_var.set(user["program"])
    if "year" in user:
        page_year_var.set(user["year"])
    if "department" in user:
        page_department_var.set(user["department"])
    if "roll_no" in user:
        page_roll_no_var.set(user["roll_no"])
    if "cgpa" in user:
        page_cgpa_var.set(user["cgpa"])

    if user_type == "Teacher":
        page_specialization_label.grid(row=5, column=0)
        page_specialization.grid(row=5, column=1)
        page_experience_label.grid(row=6, column=0)
        page_experience.grid(row=6, column=1)
        page_projects_label.grid(row=7, column=0)
        page_projects.grid(row=7, column=1)
        page_education_label.grid(row=8, column=0)
        page_education.grid(row=8, column=1)
        page_doctoral_advisor_label.grid(row=9, column=0)
        page_doctoral_advisor.grid(row=9, column=1)
    else:
        page_specialization_label.grid_remove()
        page_specialization.grid_remove()
        page_experience_label.grid_remove()
        page_experience.grid_remove()
        page_projects_label.grid_remove()
        page_projects.grid_remove()
        page_education_label.grid_remove()
        page_education.grid_remove()
        page_doctoral_advisor_label.grid_remove()
        page_doctoral_advisor.grid_remove()

    if user_type == "Undergraduate" or user_type == "Postgraduate":
        page_program_label.grid(row=6, column=0)
        page_program.grid(row=6, column=1)
        page_year_label.grid(row=7, column=0)
        page_year.grid(row=7, column=1)
        page_department_label.grid(row=8, column=0)
        page_department.grid(row=8, column=1)
        page_roll_no_label.grid(row=9, column=0)
        page_roll_no.grid(row=9, column=1)
        page_cgpa_label.grid(row=10, column=0)
        page_cgpa.grid(row=10, column=1)
    else:
        page_program_label.grid_remove()
        page_program.grid_remove()
        page_year_label.grid_remove()
        page_year.grid_remove()
        page_department_label.grid_remove()
        page_department.grid_remove()
        page_roll_no_label.grid_remove()
        page_roll_no.grid_remove()
        page_cgpa_label.grid_remove()
        page_cgpa.grid_remove()
        
    if user_type == "Postgraduate" or user_type == "Teacher":
        page_specialization_label.grid(row=4, column=0)
        page_specialization.grid(row=4, column=1)
    else:
        page_specialization_label.grid_remove()
        page_specialization.grid_remove()

def set_edit_page_data(user):
    edit_age_label.grid(row=0, column=0)
    edit_age_entry.grid(row=0, column=1)
    edit_achievements_label.grid(row=8, column=0)
    edit_achievements_entry.grid(row=8, column=1)

    if user_type == "Teacher":
        edit_specialization_label.grid(row=1, column=0)
        edit_specialization_entry.grid(row=1, column=1)

        edit_experience_label.grid(row=2, column=0)
        edit_experience_entry.grid(row=2, column=1)

        edit_projects_label.grid(row=3, column=0)
        edit_projects_entry.grid(row=3, column=1)

        edit_achievements_label.grid(row=4, column=0)
        edit_achievements_entry.grid(row=4, column=1)

        edit_education_label.grid(row=5, column=0)
        edit_education_entry.grid(row=5, column=1)

        edit_doctoral_advisor_label.grid(row=6, column=0)
        edit_doctoral_advisor_entry.grid(row=6, column=1)

    else:
        edit_specialization_label.grid_remove()
        edit_specialization_entry.grid_remove()
        edit_experience_label.grid_remove()
        edit_experience_entry.grid_remove()
        edit_projects_label.grid_remove()
        edit_projects_entry.grid_remove()
        edit_education_label.grid_remove()
        edit_education_entry.grid_remove()
        edit_doctoral_advisor_label.grid_remove()
        edit_doctoral_advisor_entry.grid_remove()

    if user_type == "Undergraduate" or user_type == "Postgraduate":
        edit_program_label.grid(row=1, column=0)
        edit_program_entry.grid(row=1, column=1)

        edit_year_label.grid(row=2, column=0)
        edit_year_entry.grid(row=2, column=1)

        edit_department_label.grid(row=3, column=0)
        edit_department_entry.grid(row=3, column=1)

        edit_roll_no_label.grid(row=4, column=0)
        edit_roll_no_entry.grid(row=4, column=1)

        edit_cgpa_label.grid(row=5, column=0)
        edit_cgpa_entry.grid(row=5, column=1)

        edit_achievements_label.grid(row=6, column=0)
        edit_achievements_entry.grid(row=6, column=1)

    else:
        edit_program_label.grid_remove()
        edit_program_entry.grid_remove()
        edit_year_label.grid_remove()
        edit_year_entry.grid_remove()
        edit_department_label.grid_remove()
        edit_department_entry.grid_remove()
        edit_roll_no_label.grid_remove()
        edit_roll_no_entry.grid_remove()
        edit_cgpa_label.grid_remove()
        edit_cgpa_entry.grid_remove()

    if user_type == "Postgraduate" or user_type == "Teacher":
        edit_specialization_label.grid(row=7, column=0)
        edit_specialization_entry.grid(row=7, column=1)
    else:
        edit_specialization_label.grid_remove()
        edit_specialization_entry.grid_remove()

def handle_unsuccessful_login(username):
    if username in login_attempts:
        login_attempts[username] += 1
    else:
        login_attempts[username] = 1
    showStatusLabel(f"Wrong password. {3 - login_attempts[username]} attempts remaining.")

    if login_attempts[username] >= 3:
        delete_user(username)
        showStatusLabel("Your account has been deleted. Please create a new account.")

def delete_user(username):
    data = person.__get_json__("input_file")

    if user_type_var2.get() == "Student":
        if program_combobox2.get() == "Undergraduate":
            data["Student"]["Undergraduate"].pop(username, None)
            login_attempts.pop(username, None)
        elif program_combobox2.get() == "Postgraduate":
            data["Student"]["Postgraduate"].pop(username, None)
            login_attempts.pop(username, None)

    elif user_type_var2.get() == "Teacher":
        data["Teacher"].pop(username, None)
        login_attempts.pop(username, None)

    person.__update_json__("output_file", data)

def showStatusLabel(message):
    label = tk.Label(r, text=message)
    label.grid(row=4, columnspan=4)
    # Schedule the hideStatusLabel function to be called after 2000 milliseconds (2 seconds)
    r.after(2000, hideStatusLabel, label)

def hideStatusLabel(label):
    label.destroy()

def clear_input():
    # Iterate over all Entry widgets and set their values to an empty string
    for frame in r.winfo_children():
        for widget in frame.winfo_children():
            if isinstance(widget, tk.Entry):
                widget.delete(0, 'end')

            if isinstance(widget, ttk.Combobox):
                widget.set(widget["values"][0])
                
    program_combobox.grid_forget()
    program_combobox2.grid_forget()
    program_label.grid_forget()
    program_label2.grid_forget()

id_generator = UniqueIDGenerator()


# GUI---------------------------------------------------------------------------

r = tk.Tk()
r.title('Network')
# r.iconbitmap('D:/IIT KGP/SWEngLab/assignment2/icon.ico')

def delete_account(user):
    page_frame.grid_forget()
    signup_frame.grid(row=2, column=0, columnspan=4, pady=10, padx=20)
    delete_user(user)
    username_var.set("New to network?\nSign up!")
    clear_input()

def addUser():
    global user_type, user
    # Check if any of the required fields are empty
    if signup_name.get() == '' or signup_age.get() == '' or signup_password.get() == '' or signup_confirm_password.get() == '' or user_type_var.get() == '':
        showStatusLabel('Please enter all the fields')
        return
    
    # Check if passwords match
    if signup_password.get() != signup_confirm_password.get():
        showStatusLabel('Passwords do not match')
        return
    
    # Check if password is valid
    if not person.__is_valid_password__(signup_password.get()):
        showStatusLabel('Password must be 8-12 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character')
        return
        
    # Check if user type is valid
    if user_type_combobox.get() != "Teacher" and user_type_combobox.get() != "Student":
        showStatusLabel('Please select a valid user type')
        return
    
    # Check if program is valid
    if user_type_combobox.get() == "Student":
        if program_combobox.get() != "Undergraduate" and program_combobox.get() != "Postgraduate":
            showStatusLabel('Please select a valid program')
    
    # Check for duplicate names in the JSON file
    data = person.__get_json__("input_file")
    if user_type_var.get() == "Student":
        if signup_name.get() in data.get("Student", {}).get("Undergraduate", {}) or signup_name.get() in data.get("Student", {}).get("Postgraduate", {}):
            showStatusLabel(f'User with the name "{signup_name.get()}" already exists')
            return
    elif user_type_var.get() == "Teacher":
        if signup_name.get() in data.get("Teacher", {}):
            showStatusLabel(f'User with the name "{signup_name.get()}" already exists')
            return

    # If no duplicate names, proceed to add the new user
    
    data = person.__get_json__("input_file")
    if user_type_var.get() == "Student":
        if program_combobox.get() == "Undergraduate":
            data["Student"]["Undergraduate"][signup_name.get()] = user = {"id": id_generator.generate_id(), "password": signup_password.get(), "name": signup_name.get(), "age": int(signup_age.get())}
            ug.age = user["age"]
            ug.id = user["id"]
            ug.name = user["name"]
            ug.password = user["password"]
            user_type = "Undergraduate"
        elif program_combobox.get() == "Postgraduate":
            data["Student"]["Postgraduate"][signup_name.get()] = user = {"id": id_generator.generate_id(), "password": signup_password.get(), "name": signup_name.get(), "age": int(signup_age.get())}
            pg.age = user["age"]
            pg.id = user["id"]
            pg.name = user["name"]
            pg.password = user["password"]
            user_type = "Postgraduate"
    elif user_type_var.get() == "Teacher":
        data["Teacher"][signup_name.get()] = user = {"id": id_generator.generate_id(), "password": signup_password.get(), "name": signup_name.get(), "age": int(signup_age.get())}
        teacher.age = user["age"]
        teacher.id = user["id"]
        teacher.name = user["name"]
        teacher.password = user["password"]
        user_type = "Teacher"

    set_page_data(user)
    person.__update_json__("output_file", data)
    showStatusLabel('Account created successfully')

    signup_frame.grid_forget()
    page_frame.grid(row=3, column=0, columnspan=4, pady=10, padx=20)

    if user_type_var.get() == "Student":
        if program_combobox.get() == "Undergraduate":
            ug.__init__(signup_name.get(), int(signup_age.get()), user["id"], user["password"], 0, 0, 0, 0, 0, 0)
        elif program_combobox.get() == "Postgraduate":
            pg.__init__(signup_name.get(), int(signup_age.get()), user["id"], user["password"], 0, 0, 0, 0, 0, 0, 0)
    elif user_type_var.get() == "Teacher":
        teacher.__init__(signup_name.get(), int(signup_age.get()), user["id"], user["password"], 0, 0, 0, 0, 0, 0)

    # welcome_frame.grid(row=0, column=0, columnspan=4, pady=10)

    username_var.set(f'{signup_name.get()}')
    # welcome_user_label.grid(row=0, columnspan=4, sticky="ew", pady=10)
    try:
        with open("users_data.pickle", 'rb') as pickle_file:
            users_data = pickle.load(pickle_file)
    except FileNotFoundError:
        users_data = {}

    # Add the new user to the dictionary
    if user_type_var.get() == "Teacher":
        users_data[signup_name.get()] = teacher
    elif user_type_var.get() == "Student":
        if program_combobox.get() == "Undergraduate":
            users_data[signup_name.get()] = ug
        elif program_combobox.get() == "Postgraduate":
            users_data[signup_name.get()] = pg

    # Store the updated dictionary in the pickle file
    with open("users_data.pickle", 'wb') as pickle_file:
        pickle.dump(users_data, pickle_file)

    return

def on_user_type_change(event):
    if user_type_var.get() == "Student":
        program_label.grid(row=5, column=0)
        program_combobox.grid(row=5, column=1)
    else:
        program_label.grid_remove()
        program_combobox.grid_remove()
        
def on_user_type_change2(event):
    if user_type_var2.get() == "Student":
        program_label2.grid(row=3, column=0)
        program_combobox2.grid(row=3, column=1)
    else:
        program_label2.grid_remove()
        program_combobox2.grid_remove()

def signuppage():
    page_frame.grid_forget()
    signin_frame.grid_forget()
    signup_frame.grid(row=2, column=0, columnspan=4, pady=10, padx=20)
    username_var.set('New to network?\nSign up!')

def signinpage():
    signup_frame.grid_forget()
    signin_frame.grid(row=2, column=0, columnspan=4, pady=10, padx=20)
    username_var.set('Sign in!')

def signin():
    global user_type, user
    data = person.__get_json__("input_file")

    #check if fields are empty
    if username.get() == "" or password.get() == "":
        showStatusLabel('Please fill in all fields')
        return
    
    if user_type_combobox2.get() != "Student" and user_type_combobox2.get() != "Teacher":
        showStatusLabel('Please select a valid user type')

    if user_type_combobox2.get() == "Student" and program_combobox2.get() != "Undergraduate" and program_combobox2.get() != "Postgraduate":
        showStatusLabel('Please select a valid program')

    #check if username.get() exists in ug or pg or teacher and password.get() matches with that users respective password
    if user_type_var2.get() == "Student":
        if program_combobox2.get() == "Undergraduate":
            if username.get() in data.get("Student", {}).get("Undergraduate", {}):
                if password.get() == data["Student"]["Undergraduate"][username.get()]["password"]:
                    user = data["Student"]["Undergraduate"][username.get()]
                    signin_frame.grid_forget()
                    page_frame.grid(row=3, column=0, columnspan=4, pady=10, padx=20)
                    ug.__init__(user["name"], user["age"], user["id"], user["password"], 0, 0, 0, 0, 0, 0)

                    username_var.set(f'{username.get()}')
                    user_type = "Undergraduate"
                    set_page_data(user)

                else:
                    handle_unsuccessful_login(username.get())
            
            else:
                showStatusLabel('User does not exist')

        elif program_combobox2.get() == "Postgraduate":
            if username.get() in data.get("Student", {}).get("Postgraduate", {}):
                if password.get() == data["Student"]["Postgraduate"][username.get()]["password"]:
                    user = data["Student"]["Postgraduate"][username.get()]
                    signin_frame.grid_forget()
                    page_frame.grid(row=3, column=0, columnspan=4, pady=10, padx=20)
                    pg.__init__(user["name"], user["age"], user["id"], user["password"], 0, 0, 0, 0, 0, 0, 0)

                    username_var.set(f'{username.get()}')
                    user_type = "Postgraduate"
                    set_page_data(user)

                else:
                    handle_unsuccessful_login(username.get())

            else:
                showStatusLabel('User does not exist')

    elif user_type_var2.get() == "Teacher":
        if username.get() in data.get("Teacher", {}):
            if password.get() == data["Teacher"][username.get()]["password"]:
                user = data["Teacher"][username.get()]
                signin_frame.grid_forget()
                page_frame.grid(row=3, column=0, columnspan=4, pady=10, padx=20)
                teacher.__init__(user["name"], user["age"], user["id"], user["password"], 0, 0, 0, 0, 0, 0)

                username_var.set(f'{user["name"]}')  
                user_type = "Teacher"
                set_page_data(user)

            else:
                handle_unsuccessful_login(username.get())

        else:
            showStatusLabel('User does not exist')

def signout():
    page_frame.grid_forget()
    edit_frame.grid_forget()
    signup_frame.grid(row=2, column=0, columnspan=4, pady=10, padx=20)
    username_var.set('New to network?\nSign up!')
    clear_input()

def editprofile(user):
    page_frame.grid_forget()
    set_edit_page_data(user)
    edit_frame.grid(row=2, column=0, columnspan=4, pady=10, padx=20)

def saveprofile():
    # global user
    edit_frame.grid_forget()
    page_age_var.set(int(edit_age_entry.get()))
    user["age"] = int(edit_age_entry.get())

    if user_type == "Teacher":
        user["specialization"] = edit_specialization_entry.get()
        user["experience"] = edit_experience_entry.get()
        user["projects"] = edit_projects_entry.get()
        user["achievements"] = edit_achievements_entry.get()
        user["education"] = edit_education_entry.get()
        user["doctoral_advisor"] = edit_doctoral_advisor_entry.get()
        data = person.__get_json__("input_file")
        data["Teacher"][user["name"]] = user

    elif user_type == "Undergraduate" or user_type == "Postgraduate":
        user["program"] = edit_program_entry.get()
        user["year"] = edit_year_entry.get()
        user["department"] = edit_department_entry.get()
        user["roll_no"] = edit_roll_no_entry.get()
        user["cgpa"] = edit_cgpa_entry.get()
        user["achievements"] = edit_achievements_entry.get()
        data = person.__get_json__("input_file")
        data["Student"]["Undergraduate"][user["name"]] = user

    if user_type == "Postgraduate":
        user["specialization"] = edit_specialization_entry.get()
        data = person.__get_json__("input_file")
        data["Student"]["Postgraduate"][user["name"]] = user

    set_page_data(user)
    data = person.__update_json__("output_file", data)

    page_frame.grid(row=2, column=0, columnspan=4, pady=10, padx=20)

#UI-------------------------------------------------------------------------
#tk.Vars
username_var = tk.StringVar()
username_var.set('New to network?\nSign up!')
user_type_var = tk.StringVar()
user_type_var2 = tk.StringVar()
page_username_var = tk.StringVar()
page_id_var = tk.StringVar()
page_age_var = tk.StringVar()
page_specialization_var = tk.StringVar()
page_experience_var = tk.StringVar()
page_projects_var = tk.StringVar()
page_achievements_var = tk.StringVar()
page_education_var = tk.StringVar()
page_doctoral_advisor_var = tk.StringVar()
page_program_var = tk.StringVar()
page_department_var = tk.StringVar()
page_year_var = tk.StringVar()
page_roll_no_var = tk.StringVar()
page_cgpa_var = tk.StringVar()

#Frames

#Welcome Frame
welcome_frame = tk.Frame(r)
welcome_frame.grid(row=0, column=0, columnspan=4, pady=10, padx=20)
welcome_label1 = tk.Label(welcome_frame, text='Welcome!', font=('Helvetica', 30, 'bold'))
welcome_label1.grid(row=0, columnspan=4, sticky="ew", pady=10)
welcome_label2 = tk.Label(welcome_frame, font=('Helvetica', 15, 'bold'), textvariable=username_var)
welcome_label2.grid(row=1, columnspan=4, sticky="ew")

#Signup Frame
signup_frame = tk.Frame(r, relief="groove", borderwidth=5)
signup_frame.grid(row=2, column=0, columnspan=4, pady=10, padx=20)

signup_name_label = tk.Label(signup_frame, text='Username:')
signup_name_label.grid(row=0, column=0)
signup_name = tk.Entry(signup_frame)
signup_name.grid(row=0, column=1)

signup_password_label = tk.Label(signup_frame, text='Password:')
signup_password_label.grid(row=1, column=0)
signup_password = tk.Entry(signup_frame, show="*")
signup_password.grid(row=1, column=1)

signup_confirm_password_label = tk.Label(signup_frame, text='Confirm Password:')
signup_confirm_password_label.grid(row=2, column=0)
signup_confirm_password = tk.Entry(signup_frame, show="*")
signup_confirm_password.grid(row=2, column=1)

signup_age_label = tk.Label(signup_frame, text='Age:')
signup_age_label.grid(row=3, column=0)
signup_age = tk.Entry(signup_frame)
signup_age.grid(row=3, column=1)

user_type_label = tk.Label(signup_frame, text='Account Type:')
user_type_label.grid(row=4, column=0)
user_type_combobox = ttk.Combobox(signup_frame, textvariable=user_type_var, values=["Teacher", "Student"])
user_type_combobox.grid(row=4, column=1)
user_type_combobox.bind("<<ComboboxSelected>>", on_user_type_change)

signup_button = tk.Button(signup_frame, text='Sign Up', command=addUser, relief=tk.GROOVE)
signup_button.grid(row=6, column=0, columnspan=2, sticky="ew", pady=2)

program_label = tk.Label(signup_frame, text='Program:')
program_combobox = ttk.Combobox(signup_frame, values=["Undergraduate", "Postgraduate"])

signin_label = tk.Label(signup_frame, text='Already have an account?')
signin_label.grid(row=7, column=0, columnspan=1, sticky="ew")

signinpage_button = tk.Button(signup_frame, text='Sign In', command=signinpage, relief=tk.GROOVE)
signinpage_button.grid(row=7, column=1, columnspan=1, sticky="ew", pady=2)

#Signin Frame
signin_frame = tk.Frame(r, relief="groove", borderwidth=5)

username_label = tk.Label(signin_frame, text='Username:')
username_label.grid(row=0, column=0)
username = tk.Entry(signin_frame)
username.grid(row=0, column=1)

password_label = tk.Label(signin_frame, text='Password:')
password_label.grid(row=1, column=0)
password = tk.Entry(signin_frame, show="*")
password.grid(row=1, column=1)

user_type_label2 = tk.Label(signin_frame, text='Account Type:')
user_type_label2.grid(row=2, column=0)
user_type_combobox2 = ttk.Combobox(signin_frame, textvariable=user_type_var2, values=["Teacher", "Student"])
user_type_combobox2.grid(row=2, column=1)
user_type_combobox2.bind("<<ComboboxSelected>>", on_user_type_change2)

program_label2 = tk.Label(signin_frame, text='Program:')
program_combobox2 = ttk.Combobox(signin_frame, values=["Undergraduate", "Postgraduate"])

signin_button = tk.Button(signin_frame, text='Sign In', command=signin, relief=tk.GROOVE)
signin_button.grid(row=4, column=0, columnspan=2, sticky="ew", pady=2)

create_account_label = tk.Label(signin_frame, text='Don\'t have an account?')
create_account_label.grid(row=5, column=0, columnspan=1, sticky="ew", pady=2)

createaccountpage_button = tk.Button(signin_frame, text='Create Account', command=signuppage, relief=tk.GROOVE)
createaccountpage_button.grid(row=5, column=1, columnspan=1, sticky="ew", pady=2)

for i in range(5):
    r.grid_rowconfigure(i, weight=1)
for i in range(4):
    r.grid_columnconfigure(i, weight=1)
    
page_frame=tk.Frame(r, relief="groove", borderwidth=5)

page_username_label = tk.Label(page_frame, text='Username:')
page_username_label.grid(row=0, column=0)
page_username = tk.Label(page_frame, textvariable=username_var)
page_username.grid(row=0, column=1)

page_age_label = tk.Label(page_frame, text='Age:')
page_age_label.grid(row=1, column=0)
page_age = tk.Label(page_frame, textvariable=page_age_var)
page_age.grid(row=1, column=1)

page_id_label = tk.Label(page_frame, text='ID:')
page_id_label.grid(row=2, column=0)
page_id = tk.Label(page_frame, textvariable=page_id_var)
page_id.grid(row=2, column=1)

page_achievements_label = tk.Label(page_frame, text='Achievements:')
page_achievements_label.grid(row=3, column=0)
page_achievements = tk.Label(page_frame, textvariable=page_achievements_var)
page_achievements.grid(row=3, column=1)

page_specialization_label = tk.Label(page_frame, text='Specialization:')
# page_specialization_label.grid(row=3, column=0)
page_specialization = tk.Label(page_frame, textvariable=page_specialization_var)
# page_specialization.grid(row=3, column=1)

page_experience_label = tk.Label(page_frame, text='Experience:')
# page_experience_label.grid(row=4, column=0)
page_experience = tk.Label(page_frame, textvariable=page_experience_var)
# page_experience.grid(row=4, column=1)

page_projects_label = tk.Label(page_frame, text='Projects:')
# page_projects_label.grid(row=5, column=0)
page_projects = tk.Label(page_frame, textvariable=page_projects_var)
# page_projects.grid(row=5, column=1)

page_achievements_label = tk.Label(page_frame, text='Achievements:')
# page_achievements_label.grid(row=6, column=0)
page_achievements = tk.Label(page_frame, textvariable=page_achievements_var)
# page_achievements.grid(row=6, column=1)

page_education_label = tk.Label(page_frame, text='Education:')
# page_education_label.grid(row=7, column=0)
page_education = tk.Label(page_frame, textvariable=page_education_var)
# page_education.grid(row=7, column=1)

page_doctoral_advisor_label = tk.Label(page_frame, text='Doctoral Advisor:')
# page_doctoral_advisor_label.grid(row=8, column=0)
page_doctoral_advisor = tk.Label(page_frame, textvariable=page_doctoral_advisor_var)
# page_doctoral_advisor.grid(row=8, column=1)

page_program_label = tk.Label(page_frame, text='Program:')
# page_program_label.grid(row=9, column=0)
page_program = tk.Label(page_frame, textvariable=page_program_var)
# page_program.grid(row=9, column=1)

page_year_label = tk.Label(page_frame, text='Year:')
# page_year_label.grid(row=10, column=0)
page_year = tk.Label(page_frame, textvariable=page_year_var)
# page_year.grid(row=10, column=1)

page_department_label = tk.Label(page_frame, text='Department:')
# page_department_label.grid(row=11, column=0)
page_department = tk.Label(page_frame, textvariable=page_department_var)
# page_department.grid(row=11, column=1)

page_roll_no_label = tk.Label(page_frame, text='Roll No:')
# page_roll_no_label.grid(row=12, column=0)
page_roll_no = tk.Label(page_frame, textvariable=page_roll_no_var)
# page_roll_no.grid(row=12, column=1)

page_cgpa_label = tk.Label(page_frame, text='CGPA:')
# page_cgpa_label.grid(row=13, column=0)
page_cgpa = tk.Label(page_frame, textvariable=page_cgpa_var)
# page_cgpa.grid(row=13, column=1)



edit_button = tk.Button(page_frame, text='Edit', command=lambda: editprofile(username_var.get()), relief=tk.GROOVE)
edit_button.grid(row=30, column=0, columnspan=2, pady=2, sticky="ew")

signout_button = tk.Button(page_frame, text='Sign Out', command=signout, relief=tk.GROOVE)
signout_button.grid(row=31, column=0, columnspan=2, pady=2, sticky="ew")

delete_account_button = tk.Button(page_frame, text='Delete Account', command=lambda: delete_account(username_var.get()), relief=tk.GROOVE, bg="red")
delete_account_button.grid(row=32, column=0, columnspan=2, pady=2, sticky="ew")

edit_frame = tk.Frame(r, relief="groove", borderwidth=5)

edit_age_label = tk.Label(edit_frame, text='Age:')
edit_specialization_label = tk.Label(edit_frame, text='Specialization:')
edit_experience_label = tk.Label(edit_frame, text='Experience:')
edit_projects_label = tk.Label(edit_frame, text='Projects:')
edit_achievements_label = tk.Label(edit_frame, text='Achievements:')
edit_education_label = tk.Label(edit_frame, text='Education:')
edit_doctoral_advisor_label = tk.Label(edit_frame, text='Doctoral Advisor:')
edit_program_label = tk.Label(edit_frame, text='Program:')
edit_year_label = tk.Label(edit_frame, text='Year:')
edit_department_label = tk.Label(edit_frame, text='Department:')
edit_roll_no_label = tk.Label(edit_frame, text='Roll No:')
edit_cgpa_label = tk.Label(edit_frame, text='CGPA:')

edit_age_entry = tk.Entry(edit_frame, textvariable=page_age_var)
edit_specialization_entry = tk.Entry(edit_frame, textvariable=page_specialization_var)
edit_experience_entry = tk.Entry(edit_frame, textvariable=page_experience_var)
edit_projects_entry = tk.Entry(edit_frame, textvariable=page_projects_var)
edit_achievements_entry = tk.Entry(edit_frame, textvariable=page_achievements_var)
edit_education_entry = tk.Entry(edit_frame, textvariable=page_education_var)
edit_doctoral_advisor_entry = tk.Entry(edit_frame, textvariable=page_doctoral_advisor_var)
edit_program_entry = tk.Entry(edit_frame, textvariable=page_program_var)
edit_year_entry = tk.Entry(edit_frame, textvariable=page_year_var)
edit_department_entry = tk.Entry(edit_frame, textvariable=page_department_var)
edit_roll_no_entry = tk.Entry(edit_frame, textvariable=page_roll_no_var)
edit_cgpa_entry = tk.Entry(edit_frame, textvariable=page_cgpa_var)

# Add "Edit" and "Sign Out" buttons
edit_button = tk.Button(edit_frame, text='Save', command=saveprofile, relief=tk.GROOVE)
edit_button.grid(row=12, column=0, columnspan=2, pady=2, sticky="ew")

signout_button = tk.Button(edit_frame, text='Sign Out', command=signout, relief=tk.GROOVE)
signout_button.grid(row=13, column=0, columnspan=2, pady=2, sticky="ew")

clear_input()

r.mainloop()