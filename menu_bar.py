#!/usr/bin/python
# -'''- coding: utf-8 -'''-

from PySide2 import QtWidgets
import sys
from PySide2 import QtGui

from lista_stajni import main




class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplikacja do zarządzania stajnią")
        self.setGeometry(100, 100, 800, 200)
        self.setWindowIcon(QtGui.QIcon('koń.jpg'))
        self.create_menu()
        #self.setPixmap(QPixmap('koń.jpg'))
        #label = QLabel
        #label.setPixmap(QPixmap(""))
        self.setCentralWidget((QtWidgets.QLabel("Witaj użytkowniku ! Witamy Cię w aplikacji do zarządzania stajnią. "
                                      "\n Znajdziesz tu funkcje pomocne przy organizacji stajni. W pasku menu znajdują się: "
                                      "\n zarzędzanie stajną, panel dodawania nowych danych do bazy, podręczna lista koni oraz użytkowników, a także dodatkowe informację, "
                                      "\n w których odnajdziesz listy wizyt, harmonogramy, karmienie oraz "
                                      "funkcję zajmowane przez użytkowników."
                                      "\n By skorzystać z interesującego nas modułu należy kliknąć na odpowiednią zakładkę w pasku menu. "
                                      "\n Następnie wyświetli się nam lista dostępnych funkcji. Za pomocą myszki bądź skrótu klawiszowego wybieramy konkretną zakładkę. ")))
        self.show()

        window = QtWidgets.QWidget()
        label = QtWidgets.QLabel()
        label.setPixmap(QtGui.QPixmap('koń.jpg'))
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label)
        window.setLayout(layout)
        window.show()

    def create_menu(self):
        mainMenu = self.menuBar()
        stableMenu = mainMenu.addMenu("Zarządzaj stajnią")
        addMenu = mainMenu.addMenu("Dodaj dane do bazy")
        horseMenu = mainMenu.addMenu("Lista koni")
        userMenu = mainMenu.addMenu("Lista użytkowników")
        informationMenu = mainMenu.addMenu("Dodatkowe informacje")
        #helpMenu = mainMenu.addMenu("Help")

        openAction = QtWidgets.QAction(QtGui.QIcon('open.png'), "Lista stajni", self)
        openAction.setShortcut("Ctrl+O")
        openAction.triggered.connect(self.show_lista_stajni)
        self.show()

        saveAction = QtWidgets.QAction(QtGui.QIcon('save.png'), "Lista zapisu koni do stajni", self)
        saveAction.setShortcut("Ctrl+S")

        exitAction = QtWidgets.QAction(QtGui.QIcon('exit.png'), "Dodaj stajnię", self)
        exitAction.setShortcut("Ctrl+X")

        exitAction.triggered.connect(self.exit_app)

        exit2Action = QtWidgets.QAction(QtGui.QIcon('exit.png'), "Dodaj zapis konia do stajni", self)
        exit2Action.setShortcut("Ctrl+f")

        stableMenu.addAction(openAction)
        stableMenu.addAction(saveAction)
        stableMenu.addAction(exitAction)
        stableMenu.addAction(exit2Action)

        open2Action = QtWidgets.QAction(QtGui.QIcon('open.png'), "Dodaj konia", self)
        open2Action.setShortcut("Ctrl+K")

        open3Action = QtWidgets.QAction(QtGui.QIcon('open.png'), "Dodaj użytkownika", self)
        open3Action.setShortcut("Ctrl+U")

        open4Action = QtWidgets.QAction(QtGui.QIcon('open.png'), "Dodaj właściciela", self)
        open4Action.setShortcut("Ctrl+W")

        open5Action = QtWidgets.QAction(QtGui.QIcon('open.png'), "Dodaj funkcję", self)
        open5Action.setShortcut("Ctrl+E")

        open6Action = QtWidgets.QAction(QtGui.QIcon('open.png'), "Dodaj wizytę", self)
        open6Action.setShortcut("Ctrl+V")

        open7Action = QtWidgets.QAction(QtGui.QIcon('open.png'), "Dodaj harmonogram", self)
        open7Action.setShortcut("Ctrl+H")

        open8Action = QtWidgets.QAction(QtGui.QIcon('open.png'), "Dodaj karmienie", self)
        open8Action.setShortcut("Ctrl+L")

        addMenu.addAction(open2Action)
        addMenu.addAction(open3Action)
        addMenu.addAction(open4Action)
        addMenu.addAction(open5Action)
        addMenu.addAction(open6Action)
        addMenu.addAction(open7Action)
        addMenu.addAction(open8Action)

        open9Action = QtWidgets.QAction(QtGui.QIcon('open.png'), "Lista właścicieli", self)
        open9Action.setShortcut("Ctrl+J")

        open10Action = QtWidgets.QAction(QtGui.QIcon('open.png'), "Lista funkcji", self)
        open10Action.setShortcut("Ctrl+M")

        open11Action = QtWidgets.QAction(QtGui.QIcon('open.png'), "Lista wizyt", self)
        open11Action.setShortcut("Ctrl+N")

        open12Action = QtWidgets.QAction(QtGui.QIcon('open.png'), "Lista harmonogramów", self)
        open12Action.setShortcut("Ctrl+C")

        open13Action = QtWidgets.QAction(QtGui.QIcon('open.png'), "Lista karmienia", self)
        open13Action.setShortcut("Ctrl+P")

        informationMenu.addAction(open9Action)
        informationMenu.addAction(open10Action)
        informationMenu.addAction(open11Action)
        informationMenu.addAction(open12Action)
        informationMenu.addAction(open13Action)

    def exit_app(self):
        self.close()

    def show_lista_stajni(self):
       self.show_lista_stajni()


app = QtWidgets.QApplication.instance()
if app == None:
    app = QtWidgets.QApplication([])
window = Window()
app.exec_()
sys.exit(0)
