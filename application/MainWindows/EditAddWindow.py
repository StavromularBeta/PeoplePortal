import tkinter as Tk
import os, sys, inspect
# below 3 lines add the parent directory to the path, so that SQL_functions can be found.
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir+'/sql_files/')
import addel as ad
import datetime
from tkinter import font as tkFont


class EditAddWindow(Tk.Frame):
    def __init__(self, parent, **kwargs):
        Tk.Frame.__init__(self, parent, **kwargs)
        self.parent = parent
        self.config(bg="#e0fcf4")
        self.large_bold_font_choice = tkFont.Font(size=16, weight='bold')
        self.add_delete_query = ad.AdDel()
        self.add_new_person_frame = Tk.Frame(self,
                                             bg='#e0fcf4')
        self.name_entry = Tk.Entry(self.add_new_person_frame)
        self.type_entry = Tk.Entry(self.add_new_person_frame)
        self.filler_canvas = Tk.Canvas(self, width=1100, height=600, bg="#e0fcf4", highlightbackground="#e0fcf4")

    def clear_edit_add_frame(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.add_new_person_frame = Tk.Frame(self,
                                             bg='#e0fcf4')
        self.name_entry = Tk.Entry(self.add_new_person_frame)
        self.type_entry = Tk.Entry(self.add_new_person_frame)
        self.filler_canvas = Tk.Canvas(self, width=1100, height=600, bg="#e0fcf4", highlightbackground="#e0fcf4")

    def edit_add(self):
        new_job_entry_frame = self.generate_new_person_frame()
        new_job_entry_frame.grid(row=0, column=0, sticky=Tk.W, padx=5, ipadx=2, ipady=2)

    def generate_new_person_frame(self):
        Tk.Label(self.add_new_person_frame, text="New Person", font=self.large_bold_font_choice).grid(row=0,
                                                                                                      columnspan=2,
                                                                                                      sticky= Tk.W)
        Tk.Label(self.add_new_person_frame, text="Name").grid(row=1, sticky=Tk.W)
        Tk.Label(self.add_new_person_frame, text="Type").grid(row=2, sticky=Tk.W)
        #Tk.Label(self.add_new_person_frame, text="Organization").grid(row=3, sticky=Tk.W)
        self.name_entry.grid(row=1, column=1, columnspan=2, sticky=Tk.W)
        self.type_entry.grid(row=2, column=1, columnspan=2, sticky=Tk.W)
        Tk.Button(self.add_new_person_frame, text="Enter Job", command=self.input_entry).grid(row=3,
                                                                                              column=0,
                                                                                              pady=10,
                                                                                              sticky=Tk.W)
        self.filler_canvas.grid(row=2, column=1, columnspan=1, sticky=Tk.W)
        return self.add_new_person_frame

    def input_entry(self):
        person = self.name_entry.get()
        if self.test_for_blank_person(person) is True:
            #This prevents you from entering a blank person.
            self.clear_edit_add_frame()
            self.edit_add()
            return False
        person_type = self.type_entry.get()
        person_entry = (person,
                        person_type,
                        0,
                        datetime.date.today(),)
        self.add_delete_query.new_people_portal_entry(person_entry)
        self.clear_edit_add_frame()
        self.edit_add()

    def test_for_blank_person(self, job_number):
        if len(job_number) == 0:
            return True



