import numpy as np
import customtkinter as ctk
import tkinter as tk
from student import Student
import os 
import sys

class Logic ():
    """Programm logic."""
    def __init__(self):
        self.students = self._load_db()

##### STUDENTS DATABASE #####
    def _load_db (self) -> list:
        """Load data from database."""
        lines = []
        with open(self._get_resource_path("database.txt"), "r") as f:
            lines = f.readlines()
        
        students = []
        for i in range(len(lines)):
            data = lines[i].replace("\n", "").split(" ")
            student = Student(data[0], data[1], data[2], int(float(data[3])))
            students.append(student)
        return students
    
    def _add_student(self, first_name : str, surname : str):
        """Add student into the student list."""
        student = Student(len(self.students) + 1, first_name.capitalize(), surname.capitalize(), 0)
        self.students.append(student)
        self.students.sort(key = lambda student: student.surname)
        self._regenerate_ids()
        self._save_db()

    def _remove_student(self, id : int):
        """Remove student from the student list."""
        for student in self.students:
            if (student.id == id):
                self.students.remove(student)
        self._regenerate_ids()
        self._save_db()
    
    def _regenerate_ids (self) -> None:
        """Set new id for every student."""
        for i in range(len(self.students)):
            self.students[i].id = i + 1

    def _save_db (self):
        """Save students into the database."""
        with open(self._get_resource_path("database.txt"), "w") as f:
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
        
    def choose_all_students (self, student_frames, value : bool):
        """Switch to all students selected or to noone stelected variant, if it is clicked to the select all checkbox."""
        if (value):
            self._set_students_marks(student_frames, True)
        else:
            self._set_students_marks(student_frames, False)

    def _set_students_marks(self, student_frames, value : bool) -> None:
        """Set all students attributes and checkboxes to entered value."""
        for student in self.students:
            student.choosen = value
        for frame in student_frames:
            frame.value.set(value)

    def _set_one_student_mark(self, elected_student : Student, value : bool) -> None:
        """Set a right mark value to elected student."""
        for student in self.students:
            if (student == elected_student):
                student.choosen = value

    def _get_marked_students (self) -> list:
        """Return a list of choosen students."""
        marked = []
        for student in self.students:
            if (student.choosen):
                marked.append(student)
        return marked

#### ACCOUNT ####
    def _total_amount(self, students : list) -> int:
        """Sum of total amout in the fund."""
        sum = 0
        for student in students:
            sum = sum + student.account
        return sum
    
    def _student_ave(self, sum : int, students : list) -> int:
        """Average of a one student from total amount."""
        if (len(students) == 0):
            return 0
        return np.ceil(sum / len(students))
    
    def _add_eachone_amount(self, amount : int, students : list) -> None:
        """Add an entered amount for each marked student."""
        for student in students:
            student.account = student.account + amount

    def _add_amount_from_sum(self, sum : int, students : list) -> None:
        """Add average of entred sum to each marked student."""
        if (len(students) == 0):
            return
        average = np.floor(sum / len(students))
        self._add_eachone_amount(average, students)

    def _remove_eachone_amount(self, amount : int, students : list) -> bool:
        """Check if it is possible to remove entered value and remove an entered amount for each marked student."""
        for student in students:
            if (student.account < amount): 
                return False
        for student in students:
            student.account = student.account - amount
        return True
    
    def _remove_amount_from_sum(self, sum : int, students : list) -> bool:
        """Check if it is possoble to remove average value from each student account a remove average of entred sum to each marked student."""
        if (len(students) == 0):
            return
        average = np.ceil(sum / len(students))
        checked = self._remove_eachone_amount(average, students)
        return checked

#### FILE PATH ####
    def _get_resource_path(self, relative_path):
        """Find the right file path if the app runs in python and also in exe file"""
        try:
            # if the app runs in exe file
            base_path = sys._MEIPASS
        except AttributeError:
            # if the app runs in python
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)