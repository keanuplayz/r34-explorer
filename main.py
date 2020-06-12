import requests
import random
import os
import json
from PIL import Image
from os import path
from pathlib import Path
import PyQt5.QtWidgets as qtw 
import PyQt5.QtGui as qtg
import urllib.request

class mainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("r34-explorer")
        self.setLayout(qtw.QVBoxLayout())
        self.setStyleSheet("background-color: #121212;")
        self.body()

    def body(self): 
        container = qtw.QWidget()

        def r34call():
            base_url = "https://r34-json-api.herokuapp.com/posts?limit=100"
            complete_url = base_url + "&tags=" + str(self.termField.text())
            try:
                response = requests.get(complete_url)
            except BaseException:
                print("Error")
            res = response.json()
            number = random.randint(0, 100)
            image = res[number]["file_url"]

            url = image
            urllib.request.urlretrieve(url, './porn.jpg')
            
            img = Image.open('./porn.jpg')
            resized_porn = img.resize((300, 300))
            fixed_resized_porn = resized_porn.convert('RGB')
            fixed_resized_porn.save('newPorn.jpg')
            pixmap = qtg.QPixmap('./newPorn.jpg')
            self.kutLabel.setPixmap(pixmap)

        def r34save():
            with open("count.json", "w+") as count:
                # TODO #1 Fix JSONDecodeError
                data = json.load(count)
                currentCount = data['number']
                img = Image.open('./porn.jpg')
                img.save(f"./r34images/{currentCount}.jpg")
                nextCount = int(currentCount) + 1
                json.dump(data, count, indent=4)
                # nextCount = int(currentCount) + 1
                # currentCount = count.readlinecound(1)
                # count.write(str(nextCount))
                
        def clear():
            if path.exists('./newPorn.jpg'):
                os.remove('./newPorn.jpg')
            if path.exists('./porn.jpg'):
                os.remove('./porn.jpg')
            else:
                pass
            
        container.setLayout(qtw.QGridLayout()) #layout setten

        self.termField = qtw.QLineEdit()
        self.termField.setPlaceholderText("Search terms: ")
        self.termField.setMinimumWidth(150)
        self.termField.setStyleSheet("color:black;background:white")
        container.layout().addWidget(self.termField, 0, 2, 1, 2)


        # 1ste nummer = row = horizontal
        # 2de nummer = column = vertical
        # 3de nummer = aantal cells height (laat op 1 staan)
        # 4de nummer = aantal cells width 
        resetButton = qtw.QPushButton("Reset", clicked=clear)
        resetButton.setMinimumWidth(50)
        resetButton.setStyleSheet("background:#2d2d2d;color:white")
        container.layout().addWidget(resetButton, 1, 2, 1, 1)

        searchButton = qtw.QPushButton("Search", clicked=r34call)
        searchButton.setMinimumWidth(50)
        searchButton.setStyleSheet("background:#2d2d2d;color:white")
        container.layout().addWidget(searchButton, 1, 3, 1, 1)

        saveButton = qtw.QPushButton("Save", clicked=r34save)
        saveButton.setMinimumWidth(50)
        saveButton.setStyleSheet("background:#2d2d2d;color:white")
        container.layout().addWidget(saveButton, 5, 0, 1, 3 )

        # imageBox = qtw.QWidget()
        # imageBox.setMinimumHeight(500)
        # imageBox.setMinimumWidth(500)
        # imageBox.setStyleSheet("border:1px solid white; background-image: url('imgae.jpg'); width:50px;")
        # container.layout().addWidget(imageBox, 2, 0, 1, 6)

        self.kutLabel = qtw.QLabel()
        
        
        container.layout().addWidget(self.kutLabel, 4, 0, 1, 6)



        self.show()

        self.layout().addWidget(container) # de container in de layout zetten

if not os.path.exists('r34images'):
    os.makedirs('r34images')

if not os.path.exists('count.json'):
    Path('count.json').touch()
    data = {}
    data["number"] = 1
    with open("count.json", "w") as outfile:
        json.dump(data, outfile, indent=4)

app = qtw.QApplication([])
app.setStyle("Fusion")
mw = mainWindow()
app.exec_() 
        

# textbox
# button (search <api call>)
# button (reset)
# box voor image display