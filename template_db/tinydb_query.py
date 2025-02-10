from tinydb import TinyDB, Query

from template_db.template_query import TemplateQuery

import sqlite3

class TinydbSelectQuery(TemplateQuery):

    def __init__(self, db_name):
        super().__init__(db_name)
        self.conn_db = None

    # 1
    def create_db_connection(self):
        self.conn_db = TinyDB(self.db_name)
        print("connection created ...")

    # 2
    def open_connection(self):
        pass

    # 3
    def run_sql_select_query(self, query):
        self.result = self.conn_db.search(query)

    # 4
    def fetch_all(self):
        pass

    # 5
    def close_connection(self):
        self.conn_db.close()
        print("Database connection closed.")