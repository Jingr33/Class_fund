import customtkinter as ctk
import tkinter as tk
from logic import Logic
from overviewFrame import Frame as overview_frame

class Frame (ctk.CTkFrame):
    """Frame for functional buttons."""
    def __init__(self, master: ctk.CTkBaseClass, logic : Logic, overview_frame) -> None:
        super().__init__(master)
        self.master = master
        self.logic = logic
        self.students = logic.students
        self.overview_frame = overview_frame
        self._init_widget_consts()
        self._init_widgets()

    def _init_widget_consts(self) -> None:
        """Define a widget constants (colors, padding, sizes, ...)."""
        self.fg_color = "gray17"
        self.padx = 10
        self.small_padx = 3
        self.width = 100
        self.label_width = 150
        self.amount_width = 80
        self.error_color = "red"
        self.top_pad = (10, 0)
        
    def _init_widgets (self):
        """Add all functional frame widgets."""
        self._stats_frame()
        self._fund_admin()
        self._students_admin()

    def _stats_frame(self):
        """Add frame with fund statistics."""
        self.stats_frame = ctk.CTkFrame(self)
        self.stats_frame.pack(side = ctk.LEFT, fill = ctk.BOTH, expand = True, ipadx = 3, ipady = 3, padx = 0, pady = 0)
        self.stats_frame.configure(fg_color = self.fg_color)

        fund_sum = self.logic._total_amount(self.students)
        total_average = self.logic._student_ave(fund_sum, self.students)

        label1 = ctk.CTkLabel(self.stats_frame, text = "Celkem ve fondu: ", width = self.label_width)
        label1.grid(row = 0, column = 0, padx = self.padx, pady = self.top_pad)
        self.sum_lbl = ctk.CTkLabel(self.stats_frame, text = "{0} Kč".format(fund_sum), font = ("Arial", 15, "bold"), fg_color = "darkgoldenrod", height = 30, width = self.amount_width, corner_radius = 4)
        self.sum_lbl .grid(row = 0, column = 1, padx = self.padx, pady = self.top_pad)
        label2 = ctk.CTkLabel(self.stats_frame, text = "Průměr na studenta: ", width = self.label_width)
        label2.grid(row = 1, column = 0, padx = self.padx, pady = self.top_pad)
        self.ave_lbl = ctk.CTkLabel(self.stats_frame, text = "{0} Kč".format(total_average), font = ("Arial", 15, "bold"), width = self.amount_width)
        self.ave_lbl.grid(row = 1, column = 1, padx = self.padx, pady = self.top_pad)
        label3 = ctk.CTkLabel(self.stats_frame, text = "Celkem ve výběru: ", width = self.label_width)
        label3.grid(row = 2, column = 0, padx = self.padx, pady = self.top_pad)
        self.sum_marked_lbl = ctk.CTkLabel(self.stats_frame, text = "0 Kč",font = ("Arial", 15, "bold"), width = self.amount_width)
        self.sum_marked_lbl.grid(row = 2, column = 1, padx = self.padx, pady = self.top_pad)
        label4 = ctk.CTkLabel(self.stats_frame, text = "Průměr vybraných: ", width = self.label_width)
        label4.grid(row = 3, column = 0, padx = self.padx, pady = self.top_pad)
        self.ave_marked_lbl = ctk.CTkLabel(self.stats_frame, text = "0 Kč", font = ("Arial", 15, "bold"), width = self.amount_width)
        self.ave_marked_lbl.grid(row = 3, column = 1, padx = self.padx, pady = self.top_pad)

    def _fund_admin(self):
        """Add frame with a fund administration."""
        self.fund_frame = ctk.CTkFrame(self)
        self.fund_frame.pack(side = ctk.LEFT, fill = ctk.BOTH, expand = True, ipadx = 3, ipady = 3, padx = 0, pady = 0)
        self.fund_frame.configure(fg_color = self.fg_color)

        label0 = ctk.CTkLabel(self.fund_frame, text = "Název platby:")
        label0.grid(row = 0, column = 0, padx = self.padx, pady = self.top_pad)
        self.pay_name = ctk.CTkEntry(self.fund_frame, width = 280)
        self.pay_name.grid(row = 0, column = 1, columnspan = 3, padx = self.padx, pady = self.top_pad)

        label5 = ctk.CTkLabel(self.fund_frame, text = "Celková částka: ")
        label5.grid(row = 1, column = 0, padx = self.padx, pady = self.top_pad)
        label6 = ctk.CTkLabel(self.fund_frame, text = "Částka na žáka: ")
        label6.grid(row = 2, column = 0, padx = self.padx, pady = self.top_pad)

        self.sum_var = tk.StringVar(value = "")
        self.sum_input = ctk.CTkEntry(self.fund_frame, textvariable = self.sum_var, width = self.width)
        self.sum_input.grid(row = 1, column = 1, padx = self.padx, pady = self.top_pad)
        self.one_var = tk.StringVar(value = "")
        self.one_input = ctk.CTkEntry(self.fund_frame, textvariable = self.one_var, width = self.width)
        self.one_input.grid(row = 2, column = 1, padx = self.padx, pady = self.top_pad)

        self.add_sum_button = ctk.CTkButton(self.fund_frame, text = "Přidat", command = self._add_sum_event, width = self.width - 20)
        self.add_sum_button.grid(row = 1, column = 2, pady = self.top_pad, padx = self.small_padx)
        self.remove_sum_button = ctk.CTkButton(self.fund_frame, text = "Odebrat", command = self._remove_sum_event, width = self.width - 20)
        self.remove_sum_button.grid(row = 1, column = 3, pady = self.top_pad, padx = self.small_padx)
        self.add_one_button = ctk.CTkButton(self.fund_frame, text = "Přidat", command = self._add_one_event, width = self.width - 20)
        self.add_one_button.grid(row = 2, column = 2, pady = self.top_pad, padx = self.small_padx)
        self.remove_one_button = ctk.CTkButton(self.fund_frame, text = "Odebrat", command = self._remove_one_event, width = self.width - 20)
        self.remove_one_button.grid(row = 2, column = 3, pady = self.top_pad, padx = self.small_padx)

        self.fund_admin_error = ctk.CTkLabel(self.fund_frame, text = "", font = ("Arial", 12), text_color = self.error_color)
        self.fund_admin_error.grid(row = 3, column = 0, columnspan = 4, pady = self.top_pad)

        self.create_table = ctk.CTkButton(self.fund_frame, text = "Vytvořit tabulku", command = self.logic.create_table)
        self.create_table.grid(row = 4, column = 2, columnspan = 2)

    def _students_admin(self):
        """add frame with a student administration."""
        self.students_frame = ctk.CTkFrame(self)
        self.students_frame.pack(side = ctk.LEFT, fill = ctk.BOTH, expand = True, ipadx = 3, ipady = 3, padx = 0, pady = 0)
        self.students_frame.configure(fg_color = self.fg_color)

        label7 = ctk.CTkLabel(self.students_frame, text = "Přidat žáka", font = ("Arial", 13, "bold"))
        label7.grid(row = 0, column = 0)
        label8 = ctk.CTkLabel(self.students_frame, text = "Křestní jméno:")
        label8.grid(row = 1, column = 0)
        self.var_first_name = tk.StringVar(value = "")
        self.first_name = ctk.CTkEntry(self.students_frame, textvariable=self.var_first_name, width=self.width)
        self.first_name.grid(row = 2, column = 0, padx = self.padx)
        label9 = ctk.CTkLabel(self.students_frame, text = "Příjmení:")
        label9.grid(row = 3, column = 0)
        self.var_surname = tk.StringVar(value = "")
        self.surname = ctk.CTkEntry(self.students_frame, textvariable=self.var_surname, width=self.width)
        self.surname.grid(row = 4, column = 0, padx = self.padx)
        self.add_stud_error = ctk.CTkLabel(self.students_frame, text = "", font = ("Arial", 9), text_color=self.error_color)
        self.add_stud_error.grid(row = 5, column = 0)
        self.add_student_btn = ctk.CTkButton(self.students_frame, text = "Přidat", command = self._add_student_event, width=self.width)
        self.add_student_btn.grid(row = 6, column = 0, padx = self.padx)

        label10 = ctk.CTkLabel(self.students_frame, text = "Odebrat žáka", font = ("Arial", 13, "bold"))
        label10.grid(row = 0, column = 1)
        label11 = ctk.CTkLabel(self.students_frame, text = "Číslo žáka:")
        label11.grid(row = 1, column = 1)
        self.var_remove_id = tk.StringVar(value = "")
        self.remove_id = ctk.CTkEntry(self.students_frame, textvariable=self.var_remove_id, width = self.width)
        self.remove_id.grid(row = 2, column = 1,padx = self.padx)
        self.remove_stud_error = ctk.CTkLabel(self.students_frame, text = "", font = ("Arial", 9), text_color=self.error_color)
        self.remove_stud_error.grid(row = 5, column = 1)
        self.remove_student_btn = ctk.CTkButton(self.students_frame, text = "Odebrat", command = self._remove_student_event, width=self.width)
        self.remove_student_btn.grid(row = 6, column = 1, padx = self.padx)

    def _add_sum_event(self):
        """Add average of the sum to each student."""
        if (not self._check_int_entry(self.sum_var.get(), 30000, self.fund_admin_error)):
            return
        sum_value = int(self.sum_var.get())
        self.logic._add_amount_from_sum(sum_value, self.logic._get_marked_students())
        self.fund_admin_error.configure(text = "")
        self._update_students_accounts()
        
    def _remove_sum_event(self):
        """Remova average of the sum to each student of it is possible."""
        if (not self._check_int_entry(self.sum_var.get(), 30000, self.fund_admin_error)):
            return
        sum_value = int(self.sum_var.get())
        checked = self.logic._remove_amount_from_sum(sum_value, self.logic._get_marked_students())
        if (not checked):
            self.fund_admin_error.configure(text = "Částku nebylo možné odečíst. Nízký stav účtu žáka.")
        else:
            self.fund_admin_error.configure(text = "")
            self._update_students_accounts()

    def _add_one_event(self):
        """Add this amount to every marked student."""
        if (not self._check_int_entry(self.one_var.get(), 5000, self.fund_admin_error)):
            return
        one_value = int(self.one_var.get())
        self.logic._add_eachone_amount(one_value, self.logic._get_marked_students())
        self.fund_admin_error.configure(text = "")
        self._update_students_accounts()

    def _remove_one_event(self):
        """Remove this amount from account of every marked student if it is possible."""
        if (not self._check_int_entry(self.one_var.get(), 5000, self.fund_admin_error)):
            return
        one_value = int(self.one_var.get())
        checked = self.logic._remove_eachone_amount(one_value, self.logic._get_marked_students())
        if (not checked):
            self.fund_admin_error.configure(text = "Částku nebylo možné odečíst. Nízký stav účtu žáka.")
        else:
            self.fund_admin_error.configure(text = "")
            self._update_students_accounts()           

    def _add_student_event (self) -> None:
        """Check the entries and add student into a database."""
        first_name = self._check_str_entry(self.first_name.get(), self.add_stud_error)
        surname = self._check_str_entry(self.surname.get(), self.add_stud_error)
        if (not first_name or not surname):
            return
        self.logic._add_student(self.var_first_name.get(), self.var_surname.get())
        self.overview_frame.create_table_content()

    def _remove_student_event (self) -> None:
        """Check entry and remove student from the database."""
        if (not self._check_int_entry(self.var_remove_id.get(), len(self.students), self.remove_stud_error)):
            return
        self.logic._remove_student(int(self.var_remove_id.get()))
        self.overview_frame.create_table_content()


    def _check_int_entry(self, entry : str, max_value : int, error_label : ctk.CTkLabel) -> bool:
        """Check, if the integer entry is in right format."""
        checked = False
        try:
            entry = int(entry)
            if (entry <= 0 or entry > max_value):
                checked =  False
            else:
                checked =  True
                error_label.configure(text = "")
        except:
            checked =  False
        if (not checked):
            error_label.configure(text = "Formulář byl špatně vyplněn.")
        return checked
    
    def _check_str_entry(self, entry : str, error_label : ctk.CTkLabel) -> bool :
        """check, if the entry is not empty."""
        if (entry == ""):
            error_label.configure(text = "Špatně vyplněný formulář.")
            return False
        else:
            error_label.configure(text = "")
            return True
        
    def _update_students_accounts(self):
        """Update content of the overview frame table."""
        for i in range(len(self.students)):
            text = "{0} Kč".format(int(self.students[i].account))
            self.overview_frame.student_frames[i].account.configure(text = text)

    def update_stats (self) -> None:
        """Update stats of the fund."""
        sum = self.logic._total_amount(self.students)
        ave = self.logic._student_ave(sum, self.students)
        marked_sum = self.logic._total_amount(self.logic._get_marked_students())
        marked_ave = self.logic._student_ave(marked_sum, self.logic._get_marked_students())
        self.sum_lbl.configure(text = "{0} Kč".format(sum))
        self.ave_lbl.configure(text = "{0} Kč".format(ave))
        self.sum_marked_lbl.configure(text = "{0} Kč".format(marked_sum))
        self.ave_marked_lbl.configure(text = "{0} Kč".format(marked_ave))