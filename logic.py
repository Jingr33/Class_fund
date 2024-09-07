import numpy as np
import customtkinter as ctk
import tkinter as tk
from student import Student

class Logic ():
    """Programm logic."""
    def __init__(self):
        self.students = self._load_db()

##### STUDENTS DATABASE #####
    def _load_db (self) -> list:
        """Load data from database."""
        lines = []
        with open("database.txt", "r") as f:
            lines = f.readlines()
        
        students = []
        for i in range(len(lines)):
            data = lines[i].replace("\n", "").split(" ")
            student = Student(data[0], data[1], data[2], data[3])
            students.append(student)
        return students
    
    def _add_student(self, id : int, first_name : str, surname : str, account : int):
        """Add student into the student list."""
        student = Student(id, first_name, surname, account)
        self.students.append(student)

    def _remove_student(self, id : int):
        """Remove student from the student list."""
        for student in self.students:
            if (student.id == id):
                self.students.remove(student)

    def _save_db (self):
        """Save students into the database."""
        with open("database.txt", "w") as f:
            for student in self.students:
                line = "{0} {1} {2} {3}\n".format(student.id, student.first_name, student.surname, student.account)
                f.write(line)

    def _choose_some(self, ids : list) -> list:
        """Choose some elected students from all students."""
        elected_students = []
        for student in self.students():
            if (student.id in ids):
                elected_students.append(student)
        return elected_students
        
    def choose_all_students (self, student_frames, value : tk.BooleanVar):
        if (value.get()):
            self._set_students_marks(student_frames, True)
        else:
            self._set_students_marks(student_frames, False)

    def _set_students_marks(self, student_frames, value : bool) -> None:
        for student in self.students:
            student.choosen = value
        for frame in student_frames:
            frame.value.set(value)

#### ACCOUNT ####
    def _total_amount(self, students : list) -> int:
        """Sum of total amout in the fund."""
        sum = 0
        for student in students:
            sum = sum + student.account
        return sum
    
    def _student_ave(self, sum : int, students : list) -> int:
        """Average of a one student from total amount."""
        return np.ceil(sum / len(students))
    
