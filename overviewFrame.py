import customtkinter as ctk
import tkinter as tk
from logic import Logic

class Frame (ctk.CTkFrame):
    """Frame for a students overwiev."""
    def __init__(self, master: ctk.CTkBaseClass, logic : Logic) -> None:
        super().__init__(master)
        self.logic = logic
        self.students = logic.students
        self.fg_color = "gray20"
        self.padx = 12
        self.pady = 8
        self.pady2 = 2
        self.configure(fg_color = self.fg_color)
        self._init_table()

    def _init_table (self):
        legend_frame = ctk.CTkFrame(self)
        legend_frame.pack(side=ctk.TOP, fill=ctk.X, ipadx=self.padx, ipady=self.pady)
        self._create_legend(legend_frame)
        content_frame = ctk.CTkFrame(self)
        content_frame.pack(side=ctk.TOP, fil=ctk.X, ipadx=self.padx, ipady=self.pady)
        content_frame.configure(fg_color = self.fg_color)
        self._create_table_content(content_frame)
    
    def _create_legend(self, frame : ctk.CTkFrame):
        ctk.CTkLabel(frame, text = "Pořadí").pack(side=ctk.LEFT, padx=self.padx, pady=self.pady)
        ctk.CTkLabel(frame, text = "Jméno").pack(side=ctk.LEFT, padx=self.padx, pady=self.pady)
        ctk.CTkLabel(frame, text = "Přijímení").pack(side=ctk.LEFT, padx=self.padx, pady=self.pady)
        ctk.CTkLabel(frame, text = "Částka").pack(side=ctk.LEFT, padx=self.padx, pady=self.pady)

        value = tk.BooleanVar(value = False)
        all_marked = ctk.CTkCheckBox(frame, text = "vybrat vše", variable = value, command = lambda: self.logic.choose_all_students(self.student_frames, value))
        all_marked.pack(side = ctk.LEFT, padx=10, pady=self.pady)

    def _create_table_content(self, frame : ctk.CTkFrame):
        """Create frames with student informations."""
        self.student_frames=  []
        for i in range((len(self.students))):
            max_in_column = 10
            student_frame = ctk.CTkFrame(frame)
            student_frame.grid(row = i % max_in_column, column = int(i / max_in_column), ipadx = 3, ipady = 3, padx = (0, 3))

            bg_color = self.fg_color
            if (i % 2 == 0):
                bg_color = "gray25"

            self._one_student_content(student_frame, i, bg_color)
            self.student_frames.append(student_frame)

    def _one_student_content(self, student_frame : ctk.CTkFrame, i : int, bg_color : str):
            """Set one student frame content."""
            student_frame.configure(fg_color = bg_color)
            student_frame.id = ctk.CTkLabel(student_frame, text = self.students[i].id)
            student_frame.id.pack(side = ctk.LEFT, pady=self.pady2)
            student_frame.id.configure(bg_color = bg_color, width = 55)
            student_frame.first_name = ctk.CTkLabel(student_frame, text = self.students[i].first_name)
            student_frame.first_name.pack(side = ctk.LEFT, pady=self.pady2)
            student_frame.first_name.configure(bg_color = bg_color, width = 70)
            student_frame.surname = ctk.CTkLabel(student_frame, text = self.students[i].surname)
            student_frame.surname.pack(side = ctk.LEFT, pady=self.pady2)
            student_frame.surname.configure(bg_color = bg_color, width = 70)
            student_frame.account = ctk.CTkLabel(student_frame, text = "{0} Kč".format(self.students[i].account))
            student_frame.account.pack(side = ctk.LEFT, pady=self.pady2)
            student_frame.account.configure(bg_color = bg_color, width = 75)

            student_frame.value = tk.BooleanVar(value = self.students[i].choosen)
            student_frame.checkbox = ctk.CTkCheckBox(student_frame, text = "", variable = student_frame.value)
            student_frame.checkbox.pack(side = ctk.LEFT, pady=self.pady2)
