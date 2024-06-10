from PyQt6.QtWidgets import QComboBox


class ToolCategory(QComboBox):
    def __init__(self):
        super().__init__()
        self.addItem("Text Tools")
        self.addItem("Media Converters")
        self.addItem("Media Editor")
