import tkinter as Tk
from MainWindows import SearchWindow as Srw,\
                        EditAddWindow as Eaw,\
                        CustomerWindow as Cuw


class MainWindow(Tk.Frame):
    def __init__(self, parent, **kwargs):
        Tk.Frame.__init__(self, parent, **kwargs)
        self.SearchWindow = Srw.SearchWindow(self)
        self.EditAddWindow = Eaw.EditAddWindow(self)
        self.CustomerWindow = Cuw.CustomerWindow(self)

    def clear_main_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.SearchWindow = Srw.SearchWindow(self)
        self.EditAddWindow = Eaw.EditAddWindow(self)
        self.CustomerWindow = Cuw.CustomerWindow(self)

    def display_searchpage(self, search=None):
        self.clear_main_window()
        if search:
            self.SearchWindow.display_all_people(search)
        else:
            self.SearchWindow.display_all_people()
        self.SearchWindow.search_people()
        self.SearchWindow.grid(padx=5, pady=5)

    def display_editaddpage(self):
        self.clear_main_window()
        self.EditAddWindow.edit_add()
        self.EditAddWindow.grid(padx=5, pady=5)

    def display_customerpage(self, customer):
        self.clear_main_window()
        self.CustomerWindow.generate_customerpage(customer)
        self.CustomerWindow.display_personal_notes(customer)
        self.CustomerWindow.grid(padx=5, pady=5)
