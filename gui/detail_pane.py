from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit
from backend.file_processor import process_file

class DetailPaneWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        self.content_text = QTextEdit(self)
        self.content_text.setReadOnly(True)
        layout.addWidget(self.content_text)

    def update_content(self, file_path):
        content = process_file(file_path)
        self.content_text.setText(content)