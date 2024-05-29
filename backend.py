'''
backend.py:

    Class: UniqueIDGenerator
        This class is responsible for generating unique IDs using the uuid module.

        Methods:
            generate_id(self) -> str:
                Generates and returns a new unique ID using uuid.uuid4().

    Class: Person
        This is the base class for both teachers and students. It includes common attributes and methods for all persons.

        Attributes:
            id (str):
                Unique identifier for a person.
            password (str):
                Password for authentication.
            name (str):
                Name of the person.
            age (int):
                Age of the person.

        Methods:
            init(self, name, age, id, password):
                Initializes a Person object with the provided name, age, id, and password.
            get_json(self, file) -> dict:
                Reads and returns JSON data from the specified file.
            update_json(self, file, data):
                Writes the provided data as JSON to the specified file.
            is_valid_password(self, password) -> bool:
                Validates if the given password meets the specified criteria.
            set_data(self, user):
                Sets the data of a Person object based on the provided user dictionary.
                Parameters:
                - user (dict): A dictionary containing user data, such as name, age, id, etc.
            display_person_attributes(self, grid_start_row):
                Displays the common attributes of a Person in a Tkinter frame.
                Parameters:
                - grid_start_row (int): The starting row in the Tkinter frame for displaying attributes.

    Class: Teacher (Inherits from Person)
        This class represents a teacher and includes additional attributes specific to teachers.

        Attributes:
            specialization (str):
                Area of specialization for the teacher.
            experience (int):
                Years of teaching experience.
            projects (list):
                List of projects the teacher has worked on.
            achievements (list):
                List of achievements of the teacher.
            education (str):
                Educational background of the teacher.
            doctoral_advisor (str):
                Name of the teacher's doctoral advisor.

        Methods:
            init(self, name, age, id, password, specialization, experience, projects, achievements, education, doctoral_advisor):
                Initializes a Teacher object with the provided attributes.
            set_data(self, user):
                Sets the data of a Teacher object based on the provided user dictionary.
                Parameters:
                - user (dict): A dictionary containing teacher-specific data.
            display_person_attributes(self, grid_start_row):
                Displays the common attributes of a Person in a Tkinter frame.
                Parameters:
                - grid_start_row (int): The starting row in the Tkinter frame for displaying attributes.

    Class: Student (Inherits from Person)
        This class represents a student and includes additional attributes specific to students.

        Attributes:
            program (str):
                Academic program of the student.
            year (int):
                Current academic year of the student.
            department (str):
                Department of study for the student.
            roll_no (str):
                Roll number of the student.
            cgpa (float):
                Cumulative Grade Point Average of the student.
            achievements (list):
                List of achievements of the student.

        Methods:
            init(self, name, age, id, password, program, year, department, roll_no, cgpa, achievements):
                Initializes a Student object with the provided attributes.
            set_data(self, user):
                Sets the data of a Student object based on the provided user dictionary.
                Parameters:
                - user (dict): A dictionary containing student-specific data.
            display_student_attributes(self, frame, grid_start_row):
                Displays the attributes specific to a Student in a Tkinter frame.
                Parameters:
                - frame (tk.Frame): The Tkinter frame in which attributes will be displayed.
                - grid_start_row (int): The starting row in the Tkinter frame for displaying attributes.

    Class: Undergraduate (Inherits from Student)
        This class represents an undergraduate student and inherits attributes and methods from the Student class.

        Attributes:
            program (str):
                Academic program of the undergraduate student.
            year (int):
                Current academic year of the undergraduate student.
            department (str):
                Department of study for the undergraduate student.
            roll_no (str):
                Roll number of the undergraduate student.
            cgpa (float):
                Cumulative Grade Point Average of the undergraduate student.
            achievements (list):
                List of achievements of the undergraduate student.

        Methods:
            init(self, name, age, id, password, program, year, department, roll_no, cgpa, achievements):
                Initializes an Undergraduate object with the provided attributes.
            set_data(self, user):
                Sets the data of an Undergraduate object based on the provided user dictionary.
                Parameters:
                - user (dict): A dictionary containing undergraduate-specific data.
            display_undergraduate_attributes(self, frame, grid_start_row):
                Displays the attributes specific to an Undergraduate in a Tkinter frame.
                Parameters:
                - frame (tk.Frame): The Tkinter frame in which attributes will be displayed.
                - grid_start_row (int): The starting row in the Tkinter frame for displaying attributes.

    Class: Postgraduate (Inherits from Student)
        This class represents a postgraduate student and inherits attributes and methods from the Student class. It also includes a specialization attribute.

        Attributes:
            specialization (str):
                Area of specialization for the postgraduate student.

        Methods:
            init(self, name, age, id, password, program, specialization, year, department, roll_no, cgpa, achievements):
                Initializes a Postgraduate object with the provided attributes.
            set_data(self, user):
                Sets the data of a Postgraduate object based on the provided user dictionary.
                Parameters:
                - user (dict): A dictionary containing postgraduate-specific data.
            display_postgraduate_attributes(self, frame, grid_start_row):
                Displays the attributes specific to a Postgraduate in a Tkinter frame.
                Parameters:
                - frame (tk.Frame): The Tkinter frame in which attributes will be displayed.
                - grid_start_row (int): The starting row in the Tkinter frame for displaying attributes.

    Example Usage:

        # Creating an instance of UniqueIDGenerator
        id_generator = UniqueIDGenerator()

        # Generating a unique ID
        new_id = id_generator.generate_id()

        # Creating a Teacher instance
        teacher = Teacher(
            name="John Doe",
            age=35,
            id=new_id,
            password="Pass123!",
            specialization="Computer Science",
            experience=10,
            projects=["Project A", "Project B"],
            achievements=["Award X", "Award Y"],
            education="Ph.D. in Computer Science",
            doctoral_advisor="Dr. Smith"
        )

        # Validating a password
        is_valid_password = teacher.is_valid_password("Pass123!")

        # Displaying teacher attributes in a Tkinter window
        root = tk.Tk()
        frame = tk.Frame(root)
        frame.pack()

        teacher.display_person_attributes(0)
        teacher.display_teacher_attributes(frame, 4)

        root.mainloop()

'''
import tkinter as tk
import uuid
import json
import re
import os

input_file = 'database.json'
output_file = 'database.json'

if not os.path.exists(input_file):
    print("Input file not found. Creating a new one...")
    with open(input_file, 'w') as file:
        default_data = {
            "Teacher": {},
            "Student": {
                "Undergraduate": {},
                "Postgraduate": {}
            }
        }
        json.dump(default_data, file)

class UniqueIDGenerator:
    def generate_id(self):
        return str(uuid.uuid4())

class Person:
    def __init__(self):
        pass
    def __init__(self, name, age, id, password):
        self.id = id
        self.password = password
        self.name = name
        self.age = age

    def __get_json__(self, file):
        if file == "input_file":
            filename = input_file
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
        
    def __update_json__(self, file, data):
        if file == "output_file":
            filename = output_file
        with open(filename, 'w') as file:
            data = json.dumps(data, indent=4)
            file.write(data)

    def __is_valid_password__(self, password):
        return re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%&*])[A-Za-z\d!@#$%&*]{8,12}$', password) and ' ' not in password
    
    def set_data(self, user):
        self.name = user.get("name", "")
        self.age = user.get("age", "")
        self.id = user.get("id", "")

    def display_person_attributes(self, grid_start_row):
        labels = ["Name", "Age", "ID"]
        attributes = [self.name, self.age, self.id]

        for i, (label, attribute) in enumerate(zip(labels, attributes)):
            tk.Label(self.frame, text=label).grid(row=grid_start_row + i, column=0)
            tk.Label(self.frame, text=attribute).grid(row=grid_start_row + i, column=1)

        tk.Button(self.frame, text="Edit", command=self.edit_person).grid(row=grid_start_row + len(labels), column=0)

class Teacher(Person):
    def __init__(self):
        pass
    def __init__(self, name, age, id, password, specialization, experience, projects, achievements, education, doctoral_advisor):
        super().__init__(name, age, id, password)
        self.specialization = specialization
        self.experience = experience
        self.projects = projects
        self.achievements = achievements
        self.education = education
        self.doctoral_advisor = doctoral_advisor

    def set_data(self, user):
        super().set_data(user)
        self.specialization = user.get("specialization", "")
        self.experience = user.get("experience", "")
        self.projects = user.get("projects", "")
        self.achievements = user.get("achievements", "")
        self.education = user.get("education", "")
        self.doctoral_advisor = user.get("doctoral_advisor", "")
        # Set other teacher-specific attributes

    def display_teacher_attributes(self, frame, grid_start_row):
        labels = ["Specialization", "Experience", "Projects", "Education", "Doctoral Advisor"]
        attributes = [self.specialization, self.experience, self.projects, self.education, self.doctoral_advisor]

        for i, (label, attribute) in enumerate(zip(labels, attributes)):
            label_widget = tk.Label(frame, text=f"{label}:")
            label_widget.grid(row=grid_start_row + i, column=0)

            attribute_widget = tk.Label(frame, textvariable=tk.StringVar(value=attribute))
            attribute_widget.grid(row=grid_start_row + i, column=1)

    def remove_teacher_attributes(self, page_specialization_label, page_specialization, page_experience_label, page_experience, page_projects_label, page_projects, page_education_label, page_education, page_doctoral_advisor_label, page_doctoral_advisor):
        attributes_widgets = [
            page_specialization_label, page_specialization,
            page_experience_label, page_experience,
            page_projects_label, page_projects,
            page_education_label, page_education,
            page_doctoral_advisor_label, page_doctoral_advisor
        ]

        for widget in attributes_widgets:
            widget.grid_remove()

class Student(Person):
    def __init__(self):
        pass
    def __init__(self, name, age, id, password, program, year, department, roll_no, cgpa, achievements):
        super().__init__(name, age, id, password)
        self.program = program
        self.year = year
        self.department = department
        self.roll_no = roll_no
        self.cgpa = cgpa
        self.achievements = achievements

    def set_data(self, user):
        super().set_data(user)
        self.program = user.get("program", "")
        self.year = user.get("year", "")
        self.department = user.get("department", "")
        self.roll_no = user.get("roll_no", "")
        self.cgpa = user.get("cgpa", "")
        # Set other student-specific attributes

    def display_student_attributes(self, frame, grid_start_row):
        labels = ["Program", "Year", "Department", "Roll No", "CGPA"]
        attributes = [self.program, self.year, self.department, self.roll_no, self.cgpa]

        for i, (label, attribute) in enumerate(zip(labels, attributes)):
            label_widget = tk.Label(frame, text=f"{label}:")
            label_widget.grid(row=grid_start_row + i, column=0)

            attribute_widget = tk.Label(frame, textvariable=tk.StringVar(value=attribute))
            attribute_widget.grid(row=grid_start_row + i, column=1)

class Undergraduate(Student):
    def __init__(self):
        pass
    def __init__(self, name, age, id, password, program, year, department, roll_no, cgpa, achievements):
        super().__init__(name, age, id, password, program, year, department, roll_no, cgpa, achievements)

    def set_data(self, user):
        super().set_data(user)
        self.program = user.get("program", "")
        self.year = user.get("year", "")
        self.department = user.get("department", "")
        self.roll_no = user.get("roll_no", "")
        self.cgpa = user.get("cgpa", "")
        
    def display_undergraduate_attributes(self, frame, grid_start_row):
        labels = ["Program", "Year", "Department", "Roll No", "CGPA"]
        attributes = [self.program, self.year, self.department, self.roll_no, self.cgpa]

        for i, (label, attribute) in enumerate(zip(labels, attributes)):
            label_widget = tk.Label(frame, text=f"{label}:")
            label_widget.grid(row=grid_start_row + i, column=0)

            attribute_widget = tk.Label(frame, textvariable=tk.StringVar(value=attribute))
            attribute_widget.grid(row=grid_start_row + i, column=1)

class Postgraduate(Student):
    def __init__(self):
        pass
    def __init__(self, name, age, id, password, program, specialization, year, department, roll_no, cgpa, achievements):
        super().__init__(name, age, id, password, program, year, department, roll_no, cgpa, achievements)
        self.specialization = specialization

    def set_data(self, user):
        super().set_data(user)
        self.program = user.get("program", "")
        self.year = user.get("year", "")
        self.department = user.get("department", "")
        self.roll_no = user.get("roll_no", "")
        self.cgpa = user.get("cgpa", "")
        self.specialization = user.get("specialization", "")
        # Set other postgraduate-specific attributes

    def display_postgraduate_attributes(self, frame, grid_start_row):
        labels = ["Program", "Year", "Department", "Roll No", "CGPA", "Specialization"]
        attributes = [self.program, self.year, self.department, self.roll_no, self.cgpa, self.specialization]

        for i, (label, attribute) in enumerate(zip(labels, attributes)):
            label_widget = tk.Label(frame, text=f"{label}:")
            label_widget.grid(row=grid_start_row + i, column=0)

            attribute_widget = tk.Label(frame, textvariable=tk.StringVar(value=attribute))
            attribute_widget.grid(row=grid_start_row + i, column=1)