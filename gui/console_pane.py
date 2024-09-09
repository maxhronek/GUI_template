from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLineEdit
from PyQt6.QtCore import pyqtSignal
from backend.command_executor import execute_command

class ConsolePaneWidget(QWidget):
    command_executed = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.output_text = QTextEdit(self)
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        self.input_line = QLineEdit(self)
        self.input_line.returnPressed.connect(self.execute_command)
        layout.addWidget(self.input_line)

    def execute_command(self):
        command = self.input_line.text()
        self.input_line.clear()
        output = execute_command(command)
        self.output_text.append(f"$ {command}\n{output}\n")
        self.command_executed.emit(command, output)