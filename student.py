class Student ():
    def __init__(self, id : int, first_name : str, surname : str, account : int):
        self.id = id
        self.first_name = first_name
        self.surname = surname
        self.account = account
        self.choosen = False

    def choose_me (self):
        self.choosen = True