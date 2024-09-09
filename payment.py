from datetime import date
from student import Student

class Payment():
    """Class of one payment."""
    def __init__(self, name : str, date : date, sum_value : int, one_value : int, pay_students : list, all_students : list):
        self.name = name
        self.date = date
        self.sum_value = sum_value
        self.one_value = one_value
        self.who_payed = self._assign_pay_students(pay_students, all_students)

    def _assign_pay_students(self, pay_students: list, all_students : list) -> list:
        """Find each student in student database and set bool value for every student if he/she pay or not."""
        who_payed = {}
        for student in all_students:
            if (student.surname in pay_students):
                who_payed[student] = True
            else:
                who_payed[student] = False
        return who_payed