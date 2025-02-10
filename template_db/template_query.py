
from abc import ABC, abstractmethod

class TemplateQuery(ABC):

    def __init__(self, db_name):
        self.conn = ""
        self.cursor = ""
        self.rows = ""
        self.result = ""
        self.db_name = db_name

    @abstractmethod
    def create_db_connection(self):
        pass

    @abstractmethod
    def open_connection(self):
        pass

    @abstractmethod
    def run_sql_select_query(self, query):
        pass

    @abstractmethod
    def fetch_all(self):
        pass

    @abstractmethod
    def close_connection(self):
        pass

    def get_query_result(self):
        return self.result

    def run(self, query):
        """Template method defining the sequence of operations."""
        self.create_db_connection()  # 1
        self.open_connection()  # 2
        self.run_sql_select_query(query)  # 3
        self.fetch_all()  # 4
        self.close_connection()  # 5
