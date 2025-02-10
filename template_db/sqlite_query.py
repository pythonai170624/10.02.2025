from template_db.template_query import TemplateQuery

import sqlite3

class SqliteSelectQuery(TemplateQuery):

    def __init__(self, db_name):
        super().__init__(db_name)

    # 1
    def create_db_connection(self):
        self.conn = sqlite3.connect(self.db_name)
        print("connection created ...")

    # 2
    def open_connection(self):
        self.cursor = self.conn.cursor()
        print("connection opened ...")

    # 3
    def run_sql_select_query(self, query):
        self.rows = self.cursor.execute(query)
        print("select query finished")

    # 4
    def fetch_all(self):
        print("fetch all:")
        self.rows = self.cursor.fetchall()
        self.result = []
        for row in self.rows:
            self.result.append(row)

    # 5
    def close_connection(self):
        self.conn.close()
        print("Database connection closed.")