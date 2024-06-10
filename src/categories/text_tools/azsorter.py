from PyQt6.QtWidgets import QWidget, QPlainTextEdit, QVBoxLayout, QHBoxLayout, QPushButton

class AZSorterView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        action_layout = QHBoxLayout()

        sort_ascending_btn = QPushButton("Sort Ascending")
        sort_descending_btn = QPushButton("Sort Descending")
        sort_ascending_btn.clicked.connect(self.sort_ascending)
        sort_descending_btn.clicked.connect(self.sort_descending)

        action_layout.addWidget(sort_ascending_btn)
        action_layout.addWidget(sort_descending_btn)

        self.editor = QPlainTextEdit()

        layout.addWidget(self.editor)
        layout.addLayout(action_layout)

        self.setLayout(layout)

    def sort_ascending(self):
        lines = self.editor.toPlainText().splitlines()
        self.editor.setPlainText("\n".join(sorted(lines)).strip())

    def sort_descending(self):
        lines = self.editor.toPlainText().splitlines()
        self.editor.setPlainText("\n".join(sorted(lines, reverse=True)).strip())

