import tkinter as Tk
from MainWindows import SearchWindow as Srw,\
                        EditAddWindow as Eaw,\
                        JobpageWindow as Jpw


class MainWindow(Tk.Frame):
    def __init__(self, parent, **kwargs):
        Tk.Frame.__init__(self, parent, **kwargs)
        self.SearchWindow = Srw.SearchWindow(self)
        self.EditAddWindow = Eaw.EditAddWindow(self)
        self.JobpageWindow = Jpw.JobpageWindow(self)

    def clear_main_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.SearchWindow = Srw.SearchWindow(self)
        self.EditAddWindow = Eaw.EditAddWindow(self)
        self.JobpageWindow = Jpw.JobpageWindow(self)

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

    def display_jobpage(self, customer):
        self.clear_main_window()
        self.JobpageWindow.generate_jobpage(customer)
        self.JobpageWindow.update_job_information(customer)
        self.JobpageWindow.display_job_notes(customer)
        self.JobpageWindow.display_tests(customer)
        self.JobpageWindow.grid(padx=5, pady=5)
