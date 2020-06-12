import PyQt5.QtWidgets as qtw 
allowSpecial = False

class mainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("r34-explorer")
        self.setLayout(qtw.QVBoxLayout())
        self.setStyleSheet("background-color: #121212;")
        self.body()

    def body(self): 
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout()) #layout setten

        termField = qtw.QLineEdit()
        termField.setPlaceholderText("Search terms: ")
        termField.setStyleSheet("color:black;background:white")
        container.layout().addWidget(termField, 0, 0, 1, 5)

        resetButton = qtw.QPushButton("Reset")
        resetButton.setStyleSheet("background:#2d2d2d")
        container.layout().addWidget(resetButton, 1, 0, 1, 2)

        searchButton = qtw.QPushButton("Search")
        searchButton.setStyleSheet("background:#2d2d2d")
        container.layout().addWidget(searchButton, 1, 3, 1, 2)



        self.show()

        self.layout().addWidget(container) # de container in de layout zetten

app = qtw.QApplication([])
app.setStyle("Fusion")
mw = mainWindow()
app.exec_() 
        

# textbox
# button (search <api call>)
# button (reset)
# box voor image display