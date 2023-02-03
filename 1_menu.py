import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class Menu(QMainWindow):
    zakaz={}
    def __init__(self):
        QMainWindow.__init__(self)
        self.resize(1000, 900)
        self.setWindowTitle("Milliy taomlar restarani")
        self.setFont(QFont("Times new", 16))
        self.oyna=QWidget()
        lbl=QLabel("MENU", self)
        lbl.setGeometry(100, 0, 300,70)
        lbl.setAlignment(Qt.AlignCenter)
        lbl.setStyleSheet("""
            color:RED;
            background-color:Yellow;
            font-size:40px;
            """)
        #1-taomlar
        taom=QLabel("1-taomlar")
        self.taom1=QCheckBox("Mastava - 15000")
        self.taom2=QCheckBox("Moshxo'rda - 20000")
        self.taom3=QCheckBox("Sho'rva - 22000")
        taomlar=QVBoxLayout()
        taomlar.addWidget(taom)
        taomlar.addWidget(self.taom1)
        taomlar.addWidget(self.taom2)
        taomlar.addWidget(self.taom3)

        #2-taomlar
        meal=QLabel("2-taomlar")
        self.meal1=QCheckBox("Osh - 18000")
        self.meal2=QCheckBox("Dimlama - 30000")
        self.meal3=QCheckBox("Qovurma lag'mon - 26000")
        meals=QVBoxLayout()
        meals.addWidget(meal)
        meals.addWidget(self.meal1)
        meals.addWidget(self.meal2)
        meals.addWidget(self.meal3)

        #desertlar
        shirinlik=QLabel("Desertlar")
        self.desert1=QCheckBox("Avganskiy - 18000")
        self.desert2=QCheckBox("Pancake - 21000")
        self.desert3=QCheckBox("Negr - 15000")
        des=QVBoxLayout()
        des.addWidget(shirinlik)
        des.addWidget(self.desert1)
        des.addWidget(self.desert2)
        des.addWidget(self.desert3)

        #ichimliklar
        ichimlik=QLabel("Ichimliklar")
        self.drink1=QCheckBox("Choy - 4000")
        self.drink2=QCheckBox("Sok - 10000")
        self.drink3=QCheckBox("Gazli ichimliklar - 7000")
        drk=QVBoxLayout()
        drk.addWidget(ichimlik)
        drk.addWidget(self.drink1)
        drk.addWidget(self.drink2)
        drk.addWidget(self.drink3)

        btn=QPushButton("Buyurtma qilish", self)
        btn.clicked.connect(self.chek)
        #jami menyu
        # menu=QGridLayout()
        menu=QVBoxLayout()
        menu.addWidget(lbl)
        menu.addLayout(taomlar)
        menu.addLayout(meals)
        menu.addLayout(des)
        menu.addLayout(drk)
        menu.addWidget(btn)
        menu.addStretch()
        self.oyna.setLayout(menu)
        self.setCentralWidget(self.oyna)
    def chek(self):
        self.oyna=QWidget()
        if self.taom1.isChecked():
            Menu.zakaz["Mastava"]=15000
        if self.taom2.isChecked():
            Menu.zakaz["Moshxo'rda"]=20000
        if self.taom3.isChecked():
            Menu.zakaz["Sho'rva"]=22000
        if self.meal1.isChecked():
            Menu.zakaz["Osh"]=18000
        if self.meal1.isChecked():
            Menu.zakaz["Dimlama"]=30000
        if self.meal1.isChecked():
            Menu.zakaz["Lag'mon"]=26000
        if self.desert1.isChecked():
            Menu.zakaz["Avganskiy"]=18000
        if self.desert2.isChecked():
            Menu.zakaz["Pancake"]=21000
        if self.desert3.isChecked():
            Menu.zakaz["Negr"]=15000
        if self.drink1.isChecked():
            Menu.zakaz["Choy"]=4000
        if self.drink2.isChecked():
            Menu.zakaz["Sok"]=10000
        if self.drink3.isChecked():
            Menu.zakaz["Gazli ichimliklar"]=7000
        self.jami=0
        check=QVBoxLayout()
        check.addWidget(QLabel("Check"))
        for x in Menu.zakaz:
            check.addWidget(QLabel(f"{x}-{Menu.zakaz[x]}"))
            self.jami+=Menu.zakaz[x]
        total=QLabel(f"Jami: {self.jami}")
        check.addWidget(total)
        check.addStretch()
        
        self.oyna.setLayout(check)
        self.setCentralWidget(self.oyna)



app=QApplication(sys.argv)
dastur=Menu()
dastur.show()
sys.exit(app.exec_())