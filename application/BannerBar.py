import tkinter as Tk
from tkinter import font as tkFont


class BannerBar(Tk.Frame):
    def __init__(self, parent, **kwargs):
        Tk.Frame.__init__(self, parent, **kwargs)
        self.banner_font = tkFont.Font(size=48, weight='bold')

    def make_banner(self):
        main_banner = Tk.Label(self, text="PeoplePortal", font=self.banner_font, bg='#39475a', fg='#f47b74')
        main_banner.grid()
