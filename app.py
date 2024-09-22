# import knihoven
import customtkinter as ctk
import tkinter as tk
from controlFrame import Frame as FuncFrame
from overviewFrame import Frame as OverwievFrame
from logic import Logic

class App(ctk.CTk):
    """Třída pracující s hlavním oknem aplikace."""
    def __init__(self) -> None:
        super().__init__()
        self.title('Třídní fond')
        self.minsize(900, 600)
        self.protocol('WM_DELETE_WINDOW', self._kill)
        self.logic = Logic()
        self.overview_frame = OverwievFrame(self, self.logic)
        self.functional_frame = FuncFrame(self, self.logic, self.overview_frame)
        self.functional_frame.pack(side=ctk.TOP, fill=ctk.X, ipadx=5, ipady=5, pady = (0, 3))
        self.overview_frame.pack(side=ctk.TOP, fill=ctk.BOTH, expand = True, ipadx=5, ipady=5)

    def _kill(self):
        self.destroy()

    def clear_frame(self, frame : ctk.CTkFrame):
        """Clear all frame widgets."""
        for widget in frame.winfo_children():
            widget.destroy()