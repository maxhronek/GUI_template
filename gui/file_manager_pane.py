from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTreeView, QFileSystemModel
from PyQt6.QtCore import pyqtSignal, QDir

class FileManagerPaneWidget(QWidget):
    file_selected = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # Remove margins for better scaling

        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.rootPath())

        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(QDir.homePath()))
        self.tree.clicked.connect(self.on_file_selected)
        self.tree.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)  # Allow the tree to expand

        layout.addWidget(self.tree)

    def on_file_selected(self, index):
        file_path = self.model.filePath(index)
        self.file_selected.emit(file_path)