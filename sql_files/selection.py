from connector import Connector


class Selection(Connector):
    def __init__(self):
        super(Selection, self).__init__()
        super(self.__class__, self).__init__()
        self.table_names = {1: 'people_table',
                            2: 'people_notes_table'}
        self.people_table_field_names = {0: 'id',
                                         1: 'name',
                                         2: 'type',
                                         3: 'affiliation_id',
                                         4: 'customer_since'
                                         }
        self.people_notes_table_field_names = {0: 'id',
                                               1: 'people_id',
                                               2: 'note',
                                               3: 'note_date',
                                              }

    def select_all_from_table(self, table_number, print_view=None):
        query = "SELECT * FROM " + self.table_names[table_number]
        if print_view:
            for item in self.connector(query):
                print(item)
        else:
            return self.connector(query)

    def select_all_from_table_descending(self, table_number, print_view=None):
        query = "SELECT * FROM " + self.table_names[table_number] + " ORDER BY name"
        if print_view:
            for item in self.connector(query):
                print(item)
        else:
            return self.connector(query)

    def select_from_people_table_with_conditions(self, field_number, condition, print_view=None):
        query = "SELECT * FROM people_table WHERE " + self.people_table_field_names[field_number] + " = (?)"
        if print_view:
            for item in self.connector(query, condition):
                print(item)
        else:
            return self.connector(query, condition)

    def select_latest_people_notes(self, people_id, print_view=None):
        query = "SELECT * FROM people_notes_table WHERE people_id = (?) ORDER BY id DESC LIMIT 1 "
        if print_view:
            for item in self.connector(query, people_id):
                print(item)
        else:
            return self.connector(query, people_id)

    def get_id_of_organization(self, organization_name, print_view=None):
        query = "SELECT * FROM people_table WHERE name = (?) ORDER BY id DESC LIMIT 1"
        if print_view:
            for item in self.connector(query, organization_name):
                print(item)
        else:
            return self.connector(query, organization_name)
