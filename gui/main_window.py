from PyQt6.QtWidgets import QMainWindow, QTabWidget, QVBoxLayout, QWidget, QSplitter
from PyQt6.QtCore import Qt
from .console_pane import ConsolePaneWidget
from .file_manager_pane import FileManagerPaneWidget
from .detail_pane import DetailPaneWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Linux Application GUI")
        self.setGeometry(100, 100, 1000, 600)

        # Enable resizing
        self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowMaximizeButtonHint | Qt.WindowType.WindowMinimizeButtonHint)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        
        # Create tab widget
        tab_widget = QTabWidget()
        layout.addWidget(tab_widget)

        # Create and add tabs
        main_tab = QWidget()
        tab_widget.addTab(main_tab, "Main")

        # Create layout for main tab
        main_layout = QVBoxLayout(main_tab)

        # Create splitter for resizable panes
        splitter = QSplitter(Qt.Orientation.Vertical)

        # Add panes to splitter
        self.console_pane = ConsolePaneWidget()
        self.file_manager_pane = FileManagerPaneWidget()
        self.detail_pane = DetailPaneWidget()

        splitter.addWidget(self.console_pane)
        splitter.addWidget(self.file_manager_pane)
        splitter.addWidget(self.detail_pane)

        # Set stretch factors for better initial sizing
        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 2)
        splitter.setStretchFactor(2, 2)

        main_layout.addWidget(splitter)

        # Connect signals
        self.file_manager_pane.file_selected.connect(self.detail_pane.update_content)