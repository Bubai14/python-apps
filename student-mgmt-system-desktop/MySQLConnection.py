import mysql.connector


class MySQLConnector:

    def __init__(self, host="host", user="user", password="password", database="database"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        connection = mysql.connector.connect(host=self.host, user=self.user,
                                             password=self.password, database=self.database)
        return connection


class Operations:

    def __init__(self):
        self.connection = MySQLConnector().connect()
        self.name = None
        self.course = None
        self.mobile = None

    def load(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * from students")
        results = cursor.fetchall()

    def insert(self):
        cursor = self.connection.cursor()
        cursor.execute("INSERT into students (name, course, mobile) VALUES (%s, %s, %s)",
                       (self.name, self.course, self.mobile))

    def update(self):
        id = None
        cursor = self.connection.cursor()
        cursor.execute("UPDATE students SET name = %s, course = %s, mobile = %s WHERE id = %s",
                       (self.name, self.course, self.mobile, id))