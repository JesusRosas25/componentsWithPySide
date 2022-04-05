import os
import sys
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QPushButton, QTabWidget, QLabel, QToolBar, QStatusBar,QCheckBox
from PySide6.QtGui import QPalette, QColor, QAction, QIcon
from PySide6.QtCore import Qt, QSize

absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
nuevo = os.path.join(absolute_folder_path, 'nuevo.png')
acerca = os.path.join(absolute_folder_path, 'acerca.png')
guardar = os.path.join(absolute_folder_path, 'guardar.png')


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Barra de herramientas en PySide')
        # Publicamos una etiqueta
        etiqueta = QLabel('Hola')
        etiqueta.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(etiqueta)
        # Creamos la barra de herramientas
        barra = QToolBar('Mi barra de herramientas')
        barra.setIconSize(QSize(16,16))
        # Configuracion para mostrar la barra de herramientas
        #barra.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        #barra.setToolButtonStyle(Qt.ToolButtonTextOnly)
        #barra.setToolButtonStyle(Qt.ToolButtonIconOnly)
        #barra.setToolButtonStyle(Qt.ToolButtonTextBesideIcon) *
        #barra.setToolButtonStyle(Qt.ToolButtonTextUnderIcon) *
        
        
        
        self.addToolBar(barra)
        
        # Agregamos un elemento a nuestra barra de herramientas
        boton_nuevo = QAction(QIcon(nuevo), 'Nuevo', self)
        # Agregamos el boton a la barra
        barra.addAction(boton_nuevo)
        
        #Agregamos el boton de guardar
        boton_guardar = QAction(QIcon(guardar), 'Guardar', self)
        # Agregamos el boton a la barra
        barra.addAction(boton_guardar)
        
        #Agregamos el boton acerca
        boton_acerca = QAction(QIcon(acerca), 'Acerca de...', self)
        # Agregamos el boton a la barra
        barra.addAction(boton_acerca)
        
        barra.addSeparator
        barra.addWidget(QCheckBox())
        
        
        menu = self.menuBar()
        menu_archivo = menu.addMenu('&Archivo')
        menu_archivo.addAction(boton_nuevo)
        menu_archivo.addAction(boton_guardar)
        boton_salir = QAction('Salir', self)
        menu_archivo.addSeparator()
        menu_archivo.addAction(boton_salir)
        # Agregamos un separador
        
        
        #submenu ayuda
        menu_ayuda = menu.addMenu('Ayuda')
        menu_ayuda.addAction(boton_acerca)
        # Barra de estado
        self.setStatusBar(QStatusBar(self))
        
        # Mostramos mensaje del boton accion
        boton_nuevo.setStatusTip('Nuevo archivo')
        boton_guardar.setStatusTip('Guardar archivo')
        boton_acerca.setStatusTip('Acerca de')
        boton_salir.setStatusTip('Salir')
        # Asociamos el evento click
        boton_nuevo.triggered.connect(self.click_boton_barra)
        boton_guardar.triggered.connect(self.click_boton_guardar)
        boton_acerca.triggered.connect(self.click_boton_acerca)
        boton_salir.triggered.connect(self.click_boton_salir)
        # Hacemos checkable el boton
        #boton_nuevo.setCheckable(True)
        
        # Agregamos un submenu
        menu_archivo.addMenu(menu_ayuda)
        
        # Creacion de atajos para nuestro menu
        # Ej. Combinación de teclas
        # boton_nuevo.setShortcut(QKeySequence('Ctrl+n'))
        boton_nuevo.setShortcut(Qt.CTRL + Qt.Key_N)
        # Atajo acerca de - Ctrl + 1
        boton_acerca.setShortcut(Qt.CTRL + Qt.Key_1)
        # Atajo guardar - Ctrl + g
        boton_guardar.setShortcut(Qt.CTRL + Qt.Key_G)
        boton_salir.setShortcut(Qt.Key_Escape)
        
    def click_boton_barra(self, s):
        print(f'Recibimos la señal: {s}')
        
    def click_boton_guardar(self, guardar):
        print(f'Guardando: {guardar}')
    
    def click_boton_acerca(self, acerca):
        print(f'Acerca de... {acerca}') 
    
    def click_boton_salir(self):
        print('Saliendo....')
        sys.exit() 
if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()