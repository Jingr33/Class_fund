import customtkinter as ctk
from app import App

def main():
    ctk.set_appearance_mode('dark')
    App().mainloop()


if __name__ == '__main__':
    main()

# BUGS
# pokud je clovek oznaceni, nelze ho odebrat
# nekdy se špatně rozpočítá celková částka mezi studenty