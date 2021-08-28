import operator
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:@localhost/dbTEST")
conn = engine.connect()

class MyWindow(QtWidgets.QWidget):
    def __init__(self, data_list, header, *args):
        QtWidgets.QWidget.__init__(self, *args)

        self.setGeometry(300, 200, 570, 450)
        self.setWindowTitle("KLiknij na tytuł kolumny by posortować")
        table_model = MyTableModel(self, data_list, header)
        table_view = QtWidgets.QTableView()
        table_view.setModel(table_model)

        font = QtGui.QFont("Courier New", 14)
        table_view.setFont(font)

        table_view.resizeColumnsToContents()

        table_view.setSortingEnabled(True)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(table_view)
        self.setLayout(layout)


class MyTableModel(QtCore.QAbstractTableModel):
    def __init__(self, parent, mylist, header, *args):
        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.header = header

    def rowCount(self, parent):
        return len(self.mylist)

    def columnCount(self, parent):
        return len(self.mylist[0])

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != QtCore.Qt.DisplayRole:
            return None
        return self.mylist[index.row()][index.column()]

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[col]
        return None

    def sort(self, col, order):

        self.emit(QtCore.SIGNAL("layoutAboutToBeChanged()"))
        self.mylist = sorted(self.mylist,
                             key=operator.itemgetter(col))
        if order == QtCore.Qt.DescendingOrder:
            self.mylist.reverse()
        self.emit(QtCore.SIGNAL("layoutChanged()"))


# utworzenie nagłówków z danymi do sortowania
header = ['ID', 'Nazwisko', 'Imię', 'Adres', 'Telefon', 'ID funkcji']
# pobranie danych z bazy
data_list = conn.execute("SELECT id, surname, name, address, phone, function_id FROM user").fetchall()

app = QtWidgets.QApplication([])
win = MyWindow(data_list, header)
win.show()
app.exec_()
