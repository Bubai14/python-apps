from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QGridLayout, QLineEdit, QPushButton, QMainWindow, \
    QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout, QComboBox
import sys
import sqlite3


class MainWindow(QMainWindow):  # QMainWindow allows to add menu and status bars.

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        # Create the menus
        self.addmenubar()

        # add the table
        self.table = QTableWidget()
        self.add_table()

    def addmenubar(self):
        file_menu = self.menuBar().addMenu("&File")
        help_menu = self.menuBar().addMenu("&Help")

        add_student_action = QAction("Add Student", self)
        add_student_action.triggered.connect(self.add_student)
        about_action = QAction("About", self)

        file_menu.addAction(add_student_action)
        help_menu.addAction(about_action)
        # For Mac computers
        about_action.setMenuRole(QAction.MenuRole.NoRole)

    def add_table(self):
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        # Hide the duplicate index column
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

    def load_data(self):
        connection = sqlite3.connect("database.db")
        results = connection.execute("SELECT * FROM students")
        # Initialize the table to zero to prevent duplicate insertions
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(results):
            self.table.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(column_data)))
        connection.close()

    def add_student(self):
        dialog = AddStudent()
        dialog.exec()


class AddStudent(QDialog):

    def __init__(self):
        super().__init__()
        # Set the window size
        self.mobile = None
        self.course = None
        self.student_name = None
        self.setWindowTitle("Add Student")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        # Add widgets
        self.add_widgets()

    def add_widgets(self):
        layout = QVBoxLayout()

        # Student Name
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        # Courses
        self.course = QComboBox()
        courses = ["Biology", "Maths", "Astronomy", "Physics"]
        self.course.addItems(courses)
        layout.addWidget(self.course)

        # Mobile
        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)

        # Add button
        button = QPushButton("Register")
        button.clicked.connect(self.register_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def register_student(self):
        name = self.student_name.text()
        course = self.course.itemText(self.course.currentIndex())
        mobile = self.mobile.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)", (name, course, mobile))
        connection.commit()
        cursor.close()
        connection.close()
        main_window.load_data()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.load_data()
    sys.exit(app.exec())
