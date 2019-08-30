from connector import Connector


class AdDel(Connector):
    def __init__(self):
        super(AdDel, self).__init__()
        super(self.__class__, self).__init__()

    def new_people_portal_entry(self, values):
        values_tuple = (values[0], values[1], values[2], values[3])
        query = 'INSERT INTO people_table (name, type, affiliation_id, customer_since) VALUES (?,?,?,?)'
        return self.connector(query, values_tuple)

    def new_people_notes_table_entry(self, values):
        values_tuple = (values[0], values[1], values[2])
        query = 'INSERT INTO people_notes_table (people_id, note, note_date) VALUES (?,?,?)'
        return self.connector(query, values_tuple)

    def delete_person(self, id):
        query = 'DELETE FROM people_table WHERE id = ?'
        return self.connector(query, id)

    def delete_notes(self, job_number):
        query = 'DELETE FROM people_notes_table WHERE people_id = ?'
        return self.connector(query, job_number)
