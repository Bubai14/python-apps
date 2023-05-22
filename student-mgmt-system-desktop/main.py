from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QGridLayout, QLineEdit, QPushButton, QMainWindow, \
    QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout, QComboBox, QToolBar, QStatusBar, QMessageBox
import sys
import sqlite3


class MainWindow(QMainWindow):  # QMainWindow allows to add menu and status bars.

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        self.setMinimumSize(800, 600)
        # Create the menus
        self.addmenubar()

        # add the table
        self.table = QTableWidget()
        self.add_table()

        # add status bar
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
        self.table.cellClicked.connect(self.cell_clicked)

    def cell_clicked(self):
        edit_button = QPushButton("Edit Student")
        edit_button.clicked.connect(self.edit_student)
        delete_button = QPushButton("Delete Student")
        delete_button.clicked.connect(self.delete_student)

        children = self.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusbar.removeWidget(child)
        self.statusbar.addWidget(edit_button)
        self.statusbar.addWidget(delete_button)

    def addmenubar(self):
        file_menu = self.menuBar().addMenu("&File")
        help_menu = self.menuBar().addMenu("&Help")
        search_menu = self.menuBar().addMenu("&Search")

        add_student_action = QAction(QIcon("icons/add.png"), "Add Student", self)
        add_student_action.triggered.connect(self.add_student)
        about_action = QAction("About", self)
        search_action = QAction(QIcon("icons/search.png"), "Search", self)

        file_menu.addAction(add_student_action)
        help_menu.addAction(about_action)
        # For Mac computers
        about_action.setMenuRole(QAction.MenuRole.NoRole)
        about_action.triggered.connect(self.about)

        # create the toolbar
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)

        toolbar.addAction(add_student_action)
        toolbar.addAction(search_action)

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

    def edit_student(self):
        dialog = EditStudent()
        dialog.exec()

    def delete_student(self):
        dialog = DeleteStudent()
        dialog.exec()

    def about(self):
        dialog = About()
        dialog.exec()


class About(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        content = """
        Project: Student Management System \n
        Version: 1.0 \n
        Developer: Bubai Bal
        """
        self.setText(content)


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


class EditStudent(QDialog):
    def __init__(self):
        super().__init__()
        # Set the window size
        self.selected_id = None
        self.mobile = None
        self.course = None
        self.student_name = None
        self.setWindowTitle("Edit Student")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        # Add widgets
        self.add_widgets()

    def add_widgets(self):
        layout = QVBoxLayout()

        # Get the selected row values
        index = main_window.table.currentRow()
        self.selected_id = main_window.table.item(index, 0).text()
        selected_name = main_window.table.item(index, 1).text()
        selected_course = main_window.table.item(index, 2).text()
        selected_mobile = main_window.table.item(index, 3).text()

        # Student Name
        self.student_name = QLineEdit(selected_name)
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        # Courses
        self.course = QComboBox()
        courses = ["Biology", "Maths", "Astronomy", "Physics"]
        self.course.addItems(courses)
        self.course.setCurrentText(selected_course)
        layout.addWidget(self.course)

        # Mobile
        self.mobile = QLineEdit(selected_mobile)
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)

        # Add button
        button = QPushButton("Update")
        button.clicked.connect(self.update_student)
        layout.addWidget(button)

        self.setLayout(layout)

    def update_student(self):
        name = self.student_name.text()
        course = self.course.itemText(self.course.currentIndex())
        mobile = self.mobile.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("UPDATE students SET name = ?, course = ?, mobile = ? WHERE id = ?",
                       (name, course, mobile, self.selected_id))
        connection.commit()
        cursor.close()
        connection.close()
        main_window.load_data()


class DeleteStudent(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete Student")

        layout = QGridLayout()
        confirm_box = QLabel("Are you sure you want to delete?")
        yes = QPushButton("Yes")
        no = QPushButton("No")

        layout.addWidget(confirm_box, 0, 0, 1, 2)
        layout.addWidget(yes, 1, 0)
        layout.addWidget(no, 1, 1)
        self.setLayout(layout)

        yes.clicked.connect(self.delete_student)

    def delete_student(self):
        index = main_window.table.currentRow()
        selected_id = main_window.table.item(index, 0).text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("DELETE from students WHERE id = ?",
                       (selected_id, ))
        connection.commit()
        cursor.close()
        connection.close()
        main_window.load_data()

        self.close()
        confirmation = QMessageBox()
        confirmation.setWindowTitle("Success")
        confirmation.setText("The student was delete successfully!!")
        confirmation.exec()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    main_window.load_data()
    sys.exit(app.exec())
