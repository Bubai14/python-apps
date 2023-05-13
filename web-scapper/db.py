import sqlite3


class Database:

    def __init__(self, database_file_path):
        # Establish the database connection
        # self is similar to this in Java and __init__ is the constructor in Java
        self.connection = sqlite3.connect(database_file_path)

    def get(self, row):
        """
        Queries the database with the row argument
        :param row:
        :return:
            the row
        """
        # Get the specific columns from the row
        band, city, date = row
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM events WHERE band = ? AND city = ? AND date = ?", (band, city, date))
        return cursor.fetchall()

    def save(self, row):
        """
        Inserts the row to the database.
        :param row:
            the row to be inserted
        :return:
        """
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO events VALUES(?, ?, ?)", row)
        self.connection.commit()
        print("New tour added!!!")
