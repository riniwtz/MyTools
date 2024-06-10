from PyQt6.QtWidgets import QApplication
from window import Window

app = QApplication([])
with open('resources/buttons.css', 'r') as style:
    app.setStyleSheet(style.read())
window = Window()
window.show()
app.exec()