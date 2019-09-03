import tkinter as Tk
import os, sys, inspect
# below 3 lines add the parent directory to the path, so that SQL_functions can be found.
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir+'/sql_files/')
import selection
import datetime
import addel
from tkinter import font as tkFont


class CustomerWindow(Tk.Frame):
    def __init__(self, parent, **kwargs):
        Tk.Frame.__init__(self, parent, **kwargs)
        self.parent = parent
        self.config(bg="#eceae6")
        self.title_font = tkFont.Font(size=18, weight='bold')
        self.regular_font = tkFont.Font(size=12, weight='bold')
        self.basic_information_window = Tk.Frame(self, bg="#eceae6")
        self.person_font = tkFont.Font(size=24, weight='bold')
        self.selection = selection.Selection()
        self.addel = addel.AdDel()
        self.notes_for_person_frame = Tk.Frame(self, bg="#eceae6")
        self.notes_for_organization_frame = Tk.Frame(self, bg='#eceae6')
        self.person_notes = Tk.Text(self.notes_for_person_frame,
                                    borderwidth=1,
                                    width=55,
                                    height=20,
                                    font=self.regular_font,
                                    wrap="word")
        self.organization_notes = Tk.Text(self.notes_for_organization_frame,
                                          borderwidth=1,
                                          width=55,
                                          height=20,
                                          font=self.regular_font,
                                          wrap="word")

    def clear_customer_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.basic_information_window = Tk.Frame(self, bg="#eceae6")
        self.notes_for_person_frame = Tk.Frame(self, bg="#eceae6")
        self.notes_for_organization_frame = Tk.Frame(self, bg='#eceae6')
        self.person_notes = Tk.Text(self.notes_for_person_frame,
                                    borderwidth=1,
                                    width=65,
                                    height=20,
                                    wrap="word")
        self.organization_notes = Tk.Text(self.notes_for_organization_frame,
                                          borderwidth=1,
                                          width=65,
                                          height=20,
                                          wrap="word")

    def generate_customerpage(self, customer):
        self.basic_information_window.grid(row=0,
                                           column=0,
                                           sticky=Tk.NW,
                                           padx=5,
                                           pady=5,
                                           ipadx=2,
                                           ipady=2)
        Tk.Label(self.basic_information_window,
                 text=str(customer[1]),
                 bg="#eceae6",
                 fg='#f47b74',
                 font=self.person_font).grid(row=1, column=0, sticky=Tk.W)
        Tk.Button(self.basic_information_window,
                  text="Delete Entry",
                  bg="#eceae6",
                  highlightbackground='#eceae6',
                  font= self.regular_font,
                  command=lambda: self.delete_job(customer[0])).grid(row=6, column=0, pady=5, sticky=Tk.W)
        Tk.Label(self.basic_information_window,
                 text="Type: " + str(customer[2]),
                 fg='#39475a',
                 font=self.regular_font,
                 bg="#eceae6").grid(row=2, column=0, sticky=Tk.W)
        if str(customer[2]) == 'Individual':
            Tk.Label(self.basic_information_window,
                     text="Organization: " + str(customer[3]),
                     bg="#eceae6",
                     font=self.regular_font,
                     fg='#f47b74').grid(row=5, column=0, sticky=Tk.W)
        Tk.Label(self.basic_information_window,
                 text="Client Since: " + str(customer[4]),
                 fg='#39475a',
                 font=self.regular_font,
                 bg="#eceae6").grid(row=4, column=0, sticky=Tk.W)

    def display_personal_notes(self, job):
        self.notes_for_person_frame.grid(row=2, column=0, rowspan=1, columnspan=3, sticky=Tk.NW, pady=5, padx=5, ipadx=2, ipady=2)
        try:
            for item in self.selection.select_latest_people_notes(str(job[0])):
                latest_job_note = item[2]
            self.person_notes.insert('end-1c', latest_job_note)
        except UnboundLocalError:
            bummer_note = "Add notes here."
            self.person_notes.insert('end-1c', bummer_note)
        Tk.Label(self.notes_for_person_frame,
                 text="Notes",
                 bg="#eceae6",
                 fg='#f47b74',
                 font=self.title_font).grid(row=0, column=0, sticky=Tk.W)
        Tk.Button(self.notes_for_person_frame,
                  text="Update Notes",
                  bg="#eceae6",
                  highlightbackground='#eceae6',
                  font=self.regular_font,
                  command=lambda: self.update_notes(job)).grid(row=3,
                                                               column=0,
                                                               pady=5,
                                                               sticky=Tk.W)
        self.person_notes.grid(row=1, column=0, sticky=Tk.W, padx=2, pady=2)
        if str(job[2]) == "Individual":
            for item in self.selection.get_id_of_organization((job[3],)):
                self.display_organization_notes(item, job)
        Tk.Canvas(self, width=620, height=600, bg="#eceae6", highlightbackground="#eceae6").grid(row=4, column=6)

    def display_organization_notes(self, job, original_id):
        self.notes_for_organization_frame.grid(row=2, column=4, rowspan=1, columnspan=3, sticky=Tk.NW, pady=5, padx=5, ipadx=2, ipady=2)
        try:
            for item in self.selection.select_latest_people_notes(str(job[0])):
                latest_job_note = item[2]
            self.organization_notes.insert('end-1c', latest_job_note)
        except UnboundLocalError:
            bummer_note = "Add notes here."
            self.organization_notes.insert('end-1c', bummer_note)
        Tk.Label(self.notes_for_organization_frame,
                 text="Organization Notes",
                 bg="#eceae6",
                 fg='#f47b74',
                 font=self.title_font).grid(row=0, column=0, sticky=Tk.W)
        Tk.Button(self.notes_for_organization_frame,
                  text="Update Notes",
                  bg="#eceae6",
                  highlightbackground='#eceae6',
                  font=self.regular_font,
                  command=lambda: self.update_org_notes(job, original_id)).grid(row=3,
                                                               column=0,
                                                               pady=5,
                                                               sticky=Tk.W)
        self.organization_notes.grid(row=1, column=0, sticky=Tk.W, padx=2, pady=2)

    def delete_job(self, id):
        self.addel.delete_person((id,))
        self.addel.delete_notes((id,))
        self.parent.display_searchpage()

    def update_notes(self, customer):
        entry = (customer[0],
                 self.person_notes.get("1.0", 'end-1c'),
                 datetime.date.today())
        self.addel.new_people_notes_table_entry(entry)
        self.parent.display_customerpage(customer)

    def update_org_notes(self, customer, original_id):
        entry = (customer[0],
                 self.organization_notes.get("1.0", 'end-1c'),
                 datetime.date.today())
        self.addel.new_people_notes_table_entry(entry)
        self.parent.display_customerpage(original_id)
