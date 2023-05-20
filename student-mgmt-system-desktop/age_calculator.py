import sys
from datetime import datetime
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QGridLayout, QLineEdit, QPushButton


class AgeCalculator(QWidget):

    def __init__(self):
        super().__init__()
        grid = QGridLayout()

        # Create the widgets
        name_label = QLabel("Name:")
        self.name = QLineEdit()

        dob_label = QLabel("Date of birth (mm/dd/yyyy):")
        self.dob = QLineEdit()

        calculate_button = QPushButton("Calculate age")
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel("")

        # Add widgets to the grid
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name, 0, 1)
        grid.addWidget(dob_label, 1, 0)
        grid.addWidget(self.dob, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2) # 2 - row position, 0 - column position, 1 - rowspan, 2 - column span
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_age(self):
        current_year = datetime.now().year
        date_of_birth = self.dob.text()
        year_of_birth = datetime.strptime(date_of_birth, "%m/%d/%Y").date().year
        age = current_year - year_of_birth
        self.output_label.setText(f"{self.name.text()} is {age} years old")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    age_calculator = AgeCalculator()
    age_calculator.show()
    sys.exit(app.exec())

