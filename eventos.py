import os
from random import randint
import sys
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QPushButton, QTabWidget, QLabel, QToolBar, QStatusBar,QCheckBox, QDialog, QDialogButtonBox, QMessageBox, QLineEdit, QMenu
from PySide6.QtGui import QPalette, QColor, QAction, QIcon
from PySide6.QtCore import Qt, QSize

absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
nuevo = os.path.join(absolute_folder_path, 'nuevo.png')
salir = os.path.join(absolute_folder_path, 'door-open-out.png')
guardar = os.path.join(absolute_folder_path, 'guardar.png')
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Eventos')
        self.etiqueta = QLabel('Da click en esta ventana')
        # self.setCentralWidget(self.etiqueta)
    
    def contextMenuEvent(self, evento):
        menu_contextual = QMenu(self)
        boton_nuevo = QAction(QIcon(nuevo), 'Nuevo', self)
        boton_guardar = QAction(QIcon(guardar),'Guardar', self)
        boton_salir = QAction(QIcon(salir),'Salir', self)
        # Recuperamos la posicion del cursor como posicion global de la ventana
        # y ejecutamos el menu contectual
        menu_contextual.addAction(boton_nuevo)
        menu_contextual.addAction(boton_guardar)
        menu_contextual.addAction(boton_salir)
        boton_nuevo.triggered.connect(self.click_nuevo)
        boton_guardar.triggered.connect(self.click_guardar)
        boton_salir.triggered.connect(self.click_salir)
        
        
        menu_contextual.exec(evento.globalPos())
    def click_nuevo(self, s):
        print(f'Se presionó el boton nuevo: {s}')
    def click_guardar(self, s):
        print(f'Se presionó el boton guardar: {s}')
    def click_salir(self, s):
        print(f'Saliendo... {s}')    
        sys.exit()
    
        
    # def mousePressEvent(self, evento):
    #     if evento.button() == Qt.LeftButton:
    #         self.etiqueta.setText('mousePressEvent Boton Izquierdo')
    #     elif evento.button() == Qt.MiddleButton:
    #         self.etiqueta.setText('mousePressEvent Boton Central')
    #     elif evento.button() == Qt.RightButton:
    #         self.etiqueta.setText('mousePressEvent Boton Derecho')
        
    # def mouseReleaseEvent(self, evento):
    #     if evento.button() == Qt.LeftButton:
    #         self.etiqueta.setText('mouseReleaseEvent boton Izquierdo')
    #     elif evento.button() == Qt.MiddleButton:
    #         self.etiqueta.setText('mouseReleaseEvent Boton Central')
    #     elif evento.button() == Qt.RightButton:
    #         self.etiqueta.setText('mouseReleaseEvent Boton Derecho')
                
    # def mouseDoubleClickEvent(self, evento):
    #     if evento.button() == Qt.LeftButton:
    #         self.etiqueta.setText('mouseDoubleClickEvent boton Izquierdo')
    #     elif evento.button() == Qt.MiddleButton:
    #         self.etiqueta.setText('mouseDoubleClickEvent Boton Central')
    #     elif evento.button() == Qt.RightButton:
    #         self.etiqueta.setText('mouseDoubleClickEvent Boton Derecho')
        
if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()