from connector import Connector


class CreateTb(Connector):
    def __init__(self):
        super(CreateTb, self).__init__()
        super(self.__class__, self).__init__()
        self.table_dictionary = {0: """ CREATE TABLE IF NOT EXISTS people_table ( id integer PRIMARY KEY,
                                        name text,
                                        type text,
                                        affiliation_id integer,
                                        customer_since date) """,
                                 1: """ CREATE TABLE IF NOT EXISTS people_notes_table ( id integer PRIMARY KEY,
                                        people_id integer,
                                        note text,
                                        note_date date) """}

    def create_table(self, dictionary_index):
        query = self.table_dictionary[dictionary_index]
        return self.connector(query)


db = CreateTb()
db.create_table(0)
db.create_table(1)