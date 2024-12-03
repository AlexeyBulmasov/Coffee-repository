import sqlite3
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.setFixedSize(800, 600)
        self.info.setReadOnly(True)
        self.con = sqlite3.connect('coffee.sqlite')
        self.all.clicked.connect(self.show_all)
        with open('main.css') as css:
            self.setStyleSheet(css.read())

    def show_any(self, positions: list):
        text = ''
        for i in positions:
            num, name, objarka, molotiy, opisanie, price, volume = i
            text += f'''Номер в каталоге - {num}
Название сорта - {name}
Степень обжарки - {objarka}
Молотый/Зерновой - {molotiy}
Описание вкуса - {opisanie}
Цена - {price}
Объем упаковки - {volume}'''
        self.info.setPlainText(text)

    def show_all(self):
        cur = self.con.cursor()
        data = cur.execute(f"""select * from main""").fetchall()
        print(data)
        self.show_any(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())
