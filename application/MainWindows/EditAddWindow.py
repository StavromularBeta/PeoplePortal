import tkinter as Tk
import os, sys, inspect
# below 3 lines add the parent directory to the path, so that SQL_functions can be found.
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir+'/sql_files/')
import addel as ad
import selection as sel
import datetime
from tkinter import font as tkFont


class EditAddWindow(Tk.Frame):
    def __init__(self, parent, **kwargs):
        Tk.Frame.__init__(self, parent, **kwargs)
        self.parent = parent
        self.config(bg="#eceae6")
        self.large_bold_font_choice = tkFont.Font(size=18, weight='bold')
        self.bold_font_choice = tkFont.Font(size=14, weight='bold')
        self.add_delete_query = ad.AdDel()
        self.selection_query = sel.Selection()
        self.add_new_person_frame = Tk.Frame(self,
                                             bg='#eceae6')
        self.name_entry = Tk.Entry(self.add_new_person_frame,
                                   highlightbackground="#eceae6")
        self.org_entry = Tk.Entry(self.add_new_person_frame,
                                  highlightbackground="#eceae6")
        self.filler_canvas = Tk.Canvas(self, width=1100, height=600, bg="#eceae6", highlightbackground="#eceae6")
        self.organization_dictionary = {}
        self.organizations_list = ["None"]

    def clear_edit_add_frame(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.add_new_person_frame = Tk.Frame(self,
                                             bg='#eceae6')
        self.name_entry = Tk.Entry(self.add_new_person_frame,
                                   highlightbackground="#eceae6")
        self.org_entry = Tk.Entry(self.add_new_person_frame,
                                  highlightbackground="#eceae6")
        self.filler_canvas = Tk.Canvas(self, width=1100, height=600, bg="#eceae6", highlightbackground="#eceae6")

    def edit_add(self):
        new_job_entry_frame = self.generate_new_person_frame()
        new_job_entry_frame.grid(row=0, column=0, sticky=Tk.W, padx=5, ipadx=2, ipady=2)

    def generate_new_person_frame(self):
        self.select_organizations_from_database()
        Tk.Label(self.add_new_person_frame,
                 text="New Individual Entry",
                 font=self.large_bold_font_choice,
                 bg="#eceae6",
                 fg='#f47b74').grid(row=0, columnspan=2, sticky=Tk.W)
        Tk.Label(self.add_new_person_frame,
                 text="Name",
                 fg='#39475a',
                 bg="#eceae6",
                 font=self.bold_font_choice).grid(row=1, sticky=Tk.W)
        self.name_entry.grid(row=1, column=1, columnspan=2, sticky=Tk.W)
        Tk.Label(self.add_new_person_frame,
                 text="Organization",
                 fg='#39475a',
                 bg="#eceae6",
                 font=self.bold_font_choice).grid(row=2, column=0, sticky=Tk.W)
        Tk.Button(self.add_new_person_frame,
                  text="Enter Individual",
                  bg="#eceae6",
                  highlightbackground="#eceae6",
                  font=self.bold_font_choice,
                  command=lambda: self.input_new_entry()).grid(row=3, column=0, pady=10, sticky=Tk.W)
        self.organization_variable = Tk.StringVar(self.add_new_person_frame)
        self.organization_variable.set(self.organizations_list[0])
        w = Tk.OptionMenu(self.add_new_person_frame, self.organization_variable, *self.organizations_list)
        w.config(bg='#eceae6')
        w.config(font=self.bold_font_choice)
        w.grid(row=2, column=1, sticky=Tk.W)
        Tk.Label(self.add_new_person_frame,
                 text="New Organization Entry",
                 bg="#eceae6",
                 fg='#f47b74',
                 font=self.large_bold_font_choice).grid(row=4, columnspan=2, sticky= Tk.W)
        Tk.Label(self.add_new_person_frame,
                 text="Name",
                 fg='#39475a',
                 bg="#eceae6",
                 font=self.bold_font_choice).grid(row=5, sticky=Tk.W)
        self.org_entry.grid(row=5, column=1, columnspan=2, sticky=Tk.W)
        Tk.Button(self.add_new_person_frame,
                  text="Enter Organization",
                  bg="#eceae6",
                  highlightbackground="#eceae6",
                  font=self.bold_font_choice,
                  command=lambda: self.input_new_org_entry()).grid(row=6, column=0, pady=10, sticky=Tk.W)
        self.filler_canvas.grid(row=7, column=1, columnspan=1, sticky=Tk.W)
        return self.add_new_person_frame

    def input_new_entry(self):
        person = self.name_entry.get()
        if self.test_for_blank_person(person) is True:
            #This prevents you from entering a blank person.
            self.clear_edit_add_frame()
            self.edit_add()
            return False
        person_type = "Individual"
        person_entry = (person,
                        person_type,
                        self.organization_variable.get(),
                        datetime.date.today(),)
        self.add_delete_query.new_people_portal_entry(person_entry)
        self.clear_edit_add_frame()
        self.parent.display_searchpage()

    def input_new_org_entry(self):
        org = self.org_entry.get()
        if self.test_for_blank_person(org) is True:
            #This prevents you from entering a blank person.
            self.clear_edit_add_frame()
            self.edit_add()
            return False
        person_type = "Organization"
        person_entry = (org,
                        person_type,
                        " ",
                        datetime.date.today(),)
        self.add_delete_query.new_people_portal_entry(person_entry)
        self.clear_edit_add_frame()
        self.parent.display_searchpage()

    def test_for_blank_person(self, job_number):
        if len(job_number) == 0:
            return True

    def select_organizations_from_database(self):
        for item in self.selection_query.select_from_people_table_with_conditions(2, ("Organization",)):
            orgname = item[1]
            self.organizations_list.append(orgname)


