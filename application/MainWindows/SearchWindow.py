import tkinter as Tk
import datetime
import os, sys, inspect
# below 3 lines add the parent directory to the path, so that SQL_functions can be found.
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir+'/sql_files/')
import selection as sel
from tkinter import font as tkFont


class SearchWindow(Tk.Frame):
    def __init__(self, parent, **kwargs):
        Tk.Frame.__init__(self, parent, **kwargs)
        self.parent = parent
        self.config(bg="#eceae6")
        self.people_display_frame = Tk.Frame(self, bg="#eceae6")
        self.search_frame = Tk.Frame(self, borderwidth=1, relief='solid', bg='#eceae6')
        self.all_people_display_frame = Tk.Frame(self, bg="#eceae6")
        self.selection = sel.Selection()
        self.search_table_field_font = tkFont.Font(size=18, weight='bold')
        self.search_table_results_font = tkFont.Font(size=14, weight='bold')
        self.people_id_font = tkFont.Font(size=16)

    def clear_search_window(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.people_display_frame = Tk.Frame(self, bg="#eceae6")
        self.search_frame = Tk.Frame(self, borderwidth=1, relief='solid', bg='#eceae6')
        self.all_people_display_frame = Tk.Frame(self, bg="#eceae6")

    def display_all_people(self, search=None):
        self.clear_search_window()
        display_all_people_canvas = Tk.Canvas(self.people_display_frame,
                                              width=1080,
                                              height=700,
                                              scrollregion=(0, 0, 0, 2000),
                                              bg="#eceae6",
                                              highlightbackground="#eceae6")
        all_entries_scroll = Tk.Scrollbar(self.people_display_frame,
                                          orient="vertical",
                                          command=display_all_people_canvas.yview,
                                          bg='#eceae6')
        self.all_people_display_frame = Tk.Frame(self,
                                                 bg='#eceae6')  # I don't understand why this needs to be here.
        display_all_people_canvas.configure(yscrollcommand=all_entries_scroll.set)
        all_entries_scroll.pack(side='right',
                                fill='y')
        display_all_people_canvas.pack(side="left",
                                       fill='y')
        display_all_people_canvas.create_window((0, 0),
                                                window=self.all_people_display_frame,
                                                anchor='nw')
        Tk.Label(self.all_people_display_frame,
                 text="Name",
                 fg='#f47b74',
                 font=self.search_table_field_font,
                 highlightbackground="#eceae6",
                 bg="#eceae6").grid(row=0, column=0, sticky=Tk.W, padx=2, pady=2)
        Tk.Label(self.all_people_display_frame,
                 text="Customer Type",
                 fg='#f47b74',
                 font=self.search_table_field_font,
                 highlightbackground="#eceae6",
                 bg="#eceae6").grid(row=0, column=1, sticky=Tk.W, padx=2, pady=2)
        Tk.Label(self.all_people_display_frame,
                 text="Organization",
                 fg='#f47b74',
                 font=self.search_table_field_font,
                 highlightbackground="#eceae6",
                 bg="#eceae6").grid(row=0, column=2, sticky=Tk.W, padx=2, pady=2)
        #Tk.Label(self.all_people_display_frame,
        #         text="Client Since",
        #         fg='#f47b74',
        #         font=self.search_table_field_font,
        #         highlightbackground="#eceae6",
        #         bg="#eceae6").grid(row=0, column=3, sticky=Tk.E, padx=2, pady=2)
        if search:
            self.return_people(search)
        else:
            self.return_people()
        self.people_display_frame.grid(row=1, column=0, pady=5)

    def return_people(self, search=None):
        if search:
            all_people_data = search
        else:
            all_people_data = self.selection.select_all_from_table_descending(1)
        first_customer_row = 1
        for item in all_people_data:
            name = item[1]
            customer_type = item[2]
            organization = item[3]
            #client_since = item[4]
            if (first_customer_row % 2) == 1:
                Tk.Button(self.all_people_display_frame,
                          text=name,
                          command=lambda item=item: self.parent.display_customerpage(item),
                          highlightbackground="#eceae6",
                          font=self.search_table_results_font,
                          fg='#39475a',
                          bg="#eceae6").grid(row=first_customer_row,
                                             column=0,
                                             sticky=Tk.W,
                                             padx=2,
                                             pady=2)
                Tk.Label(self.all_people_display_frame,
                         text=customer_type,
                         highlightbackground="#eceae6",
                         font=self.search_table_results_font,
                         fg='#39475a',
                         bg="#eceae6").grid(row=first_customer_row, column=1, sticky=Tk.W, padx=2, pady=2)
                Tk.Label(self.all_people_display_frame,
                         text=organization,
                         highlightbackground="#eceae6",
                         font=self.search_table_results_font,
                         fg='#39475a',
                         bg="#eceae6").grid(row=first_customer_row, column=2, sticky=Tk.W, padx=2, pady=2)
                #Tk.Label(self.all_people_display_frame,
                #         text=client_since,
                #         highlightbackground="#eceae6",
                #         font=self.search_table_results_font,
                #         fg='#39475a',
                #         bg="#eceae6").grid(row=first_customer_row, column=3, sticky=Tk.E, padx=2, pady=2)
                first_customer_row += 1
            else:
                Tk.Button(self.all_people_display_frame,
                          text=name,
                          command=lambda item=item: self.parent.display_customerpage(item),
                          highlightbackground="#eceae6",
                          font=self.search_table_results_font,
                          bg="#eceae6").grid(row=first_customer_row,
                                             column=0,
                                             sticky=Tk.W,
                                             padx=2,
                                             pady=2)
                Tk.Label(self.all_people_display_frame,
                         text=customer_type,
                         highlightbackground="#eceae6",
                         font=self.search_table_results_font,
                         bg="#eceae6").grid(row=first_customer_row, column=1, sticky=Tk.W, padx=2, pady=2)
                Tk.Label(self.all_people_display_frame,
                         text=organization,
                         highlightbackground="#eceae6",
                         font=self.search_table_results_font,
                         bg="#eceae6").grid(row=first_customer_row, column=2, sticky=Tk.W, padx=2, pady=2)
                #Tk.Label(self.all_people_display_frame,
                #         text=client_since,
                #         highlightbackground="#eceae6",
                #         font=self.search_table_results_font,
                #         bg="#eceae6").grid(row=first_customer_row, column=3, sticky=Tk.E, padx=2, pady=2)
                first_customer_row += 1

    def search_people(self):
        self.search_frame = Tk.Frame(self, bg='#eceae6')
        Tk.Label(self.search_frame,
                 text="Search Customers",
                 font=self.search_table_field_font,
                 fg="#f47b74",
                 bg="#eceae6").grid(row=0, column=0)
        search_result_frame = Tk.Frame(self.search_frame, bg="#eceae6")
        search_result_frame.grid(row=1, column=0, columnspan=3, padx=5, ipadx=2, ipady=2, pady=5)
        self.option_variable = Tk.StringVar(search_result_frame)
        self.option_variable.set('Name')
        search_options = Tk.OptionMenu(search_result_frame, self.option_variable, "Name", "Type", "Organization")
        search_options.config(font=self.search_table_results_font)
        search_options["menu"].config(font=self.search_table_results_font)
        search_options.config(bg="#eceae6")
        search_options["menu"].config(bg="#eceae6")
        search_options["menu"].config(fg="#39475a")
        search_options.grid(row=0)
        self.search_entry_field = Tk.Entry(search_result_frame,
                                           highlightbackground="#eceae6",
                                           font=self.search_table_results_font)
        self.search_entry_field.grid(row=0, column=1)
        Tk.Button(search_result_frame,
                  text="search",
                  command=self.search_database_for_people,
                  highlightbackground="#eceae6",
                  font=self.search_table_results_font).grid(row=1, column=0, sticky=Tk.E)
        Tk.Button(search_result_frame,
                  text="all",
                  command=self.parent.display_searchpage,
                  highlightbackground="#eceae6",
                  font=self.search_table_results_font).grid(row=1, column=1, sticky=Tk.W)
        self.search_frame.grid(row=0, column=0, sticky=Tk.NW)

    def search_database_for_people(self):
        search_type = self.option_variable.get()
        entry_field = self.search_entry_field.get()
        if search_type == "Name":
            search_results = self.selection.select_from_people_table_with_conditions(1, (entry_field,))
        elif search_type == "Type":
            search_results = self.selection.select_from_people_table_with_conditions(2, (entry_field,))
        elif search_type == "Organization":
            search_results = self.selection.select_from_people_table_with_conditions(3, (entry_field,))
        self.parent.display_searchpage(search_results)

