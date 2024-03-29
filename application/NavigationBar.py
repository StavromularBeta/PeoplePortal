import tkinter as Tk
from tkinter import font as tkFont


class NavigationBar(Tk.Frame):
    def __init__(self, parent, **kwargs):
        Tk.Frame.__init__(self, parent, **kwargs)
        self.parent = parent
        self.nav_bar_button_font = tkFont.Font(size=18)

    def make_navbar(self):
        search_button = Tk.Button(self,
                                  text=" Current \n Customers",
                                  command=self.parent.MainWindow.display_searchpage,
                                  font=self.nav_bar_button_font)
        edit_add_button = Tk.Button(self,
                                    text="Enter New\n Customers",
                                    command=self.parent.MainWindow.display_editaddpage,
                                    font=self.nav_bar_button_font)
        search_button.grid(row=0, padx=5, pady=5)
        edit_add_button.grid(row=1, padx=5)



