from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication
import sys
from backend import Chatbot
import threading


class ChatbotWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setMinimumSize(700, 500)
        self.chatbot = Chatbot()

        # Add chat widgets
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # Add message field widget
        self.input_message = QLineEdit(self)
        self.input_message.setGeometry(10, 340, 480, 40)
        self.input_message.returnPressed.connect(self.send_message)

        # Add send button widget
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 40)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_message.text().strip()
        self.chat_area.append(f"<p><b style= 'color: #FF9900'>You</b>: {user_input}</p>")
        self.input_message.clear()

        thread = threading.Thread(target=self.get_bot_response, args=(user_input, ))
        thread.start()

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p><b style= 'color: #FF00FF'>Bot</b>: {response}</p>")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    chatbot_window = ChatbotWindow()
    sys.exit(app.exec())
