from connector import Connector


class EditEntry(Connector):
    def __init__(self):
        super(EditEntry, self).__init__()
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

    def edit_people_table_entry(self, field, update, customer_id):
        query = 'UPDATE cannajobs SET ' + self.cannajobs_field_names[field] + " = '" + str(update) + "' WHERE id = " +\
                str(customer_id)
        return self.connector(query)
