from PyQt6.QtWidgets import QWidget, QLabel, QStackedWidget, QListWidget, QListWidgetItem, QVBoxLayout, QStackedLayout, QSplitter
from widgets.tool_category import ToolCategory
from categories.text_tools.azsorter import AZSorterView

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("RinTools")


        layout = QVBoxLayout()

        tool_category = ToolCategory()
        
        tool_list = QListWidget()
        tool_list.currentRowChanged.connect(self.update_content_view)
        tool_list.addItem("A-Z Sorter")
        tool_list.addItem("...")
        tool_list.addItem("...")

        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(AZSorterView())

        splitter = QSplitter()
        splitter.addWidget(tool_list)
        splitter.addWidget(self.stacked_widget)

        layout.addWidget(tool_category)
        layout.addWidget(splitter)
        self.setLayout(layout)
    
    def update_content_view(self, index):
        self.stacked_widget.setCurrentIndex(index)
