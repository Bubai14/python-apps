import sqlite3

# Establish the database connection
connection = sqlite3.connect("data.db")


def get(row):
    """
    Queries the database with the row argument
    :param row:
    :return:
        the row
    """
    # Get the specific columns from the row
    band, city, date = row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE band = ? AND city = ? AND date = ?", (band, city, date))
    return cursor.fetchall()


def save(row):
    """
    Inserts the row to the database.
    :param row:
        the row to be inserted
    :return:
    """
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?, ?, ?)", row)
    connection.commit()
    print("New tour added!!!")
