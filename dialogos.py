from email.policy import default
import os
import sys
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QPushButton, QTabWidget, QLabel, QToolBar, QStatusBar,QCheckBox, QDialog, QDialogButtonBox, QMessageBox
from PySide6.QtGui import QPalette, QColor, QAction, QIcon
from PySide6.QtCore import Qt, QSize

# absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
# nuevo = os.path.join(absolute_folder_path, 'nuevo.png')
# acerca = os.path.join(absolute_folder_path, 'acerca.png')
# guardar = os.path.join(absolute_folder_path, 'guardar.png')

# class VentanaDialogo(QDialog):
#     def __init__(self, parent: None):
#         super().__init__(parent)
#         self.setWindowTitle('Ventana de Dialogo')
#         # Agregamos un boton de aceptar y otro de cancelar
#         botones = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
#         self.botones_dialogo = QDialogButtonBox(botones)
#         self.botones_dialogo.accepted.connect(self.accept)
#         self.botones_dialogo.rejected.connect(self.reject)
        
#         # Creamos un layout para publicar los botones
#         self.layout = QVBoxLayout()
#         mensaje = QLabel('Presiona alguno de los botones')
#         self.layout.addWidget(mensaje)
#         self.layout.addWidget(self.botones_dialogo)
#         self.setLayout(self.layout)



class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dialogos')
        # Agregamos un boton
        boton = QPushButton('Mostrar dialogo')
        boton.clicked.connect(self.click_boton)
        self.setCentralWidget(boton)
        
    def click_boton(self, s):
        print(f'Click sobre boton: {s}')
        # Creamos el dialogo
        dialogo = QMessageBox.warning(self, 'Problema critico','Ventana con problema critico', buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore, defaultButton=QMessageBox.Ignore)
        
        # Revisamos cual boton se presiono
        if dialogo == QMessageBox.Discard:
            print('Regreso el valor Discard')
        elif dialogo == QMessageBox.NoToAll:
            print('Regreso el valor de NoToAll')
        else:
            print('Regreso el valor de Ignore')
        
        
        # dialogo = QMessageBox.question(self, 'Pregunta', 'Ventana con pregunta')
        
        # if dialogo == QMessageBox.Yes:
        #     print('Regreso el valor Yes (Si)')
        # else:
        #     print('Regreso el valor de No')
        
        
        
        
        
        # dialogo = QMessageBox(self)
        # dialogo.setWindowTitle('Dialogo con pregunta')
        # dialogo.setText('Ventana de dialogo con Pregunta')
        # # Agregamos los botones de la respuesta a la pregunta
        # dialogo.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        # # Agtregamos un icono a la ventana de dialogo
        # dialogo.setIcon(QMessageBox.Question)
        # valor_retornado = dialogo.exec()
        # # IMprimir el valor retornado
        # print(f'Valor retornado: {valor_retornado}')
        # if valor_retornado == QMessageBox.Yes:
        #     print('Regreso el valor Yes (Si)')
        # else:
        #     print('Regreso el valor de No')        
        
        
        
        # dialogo = VentanaDialogo(self)
        # valor_retornado = dialogo.exec()
        # print(f'Valor retornad: {valor_retornado}')
        # if valor_retornado:
        #     print('Se presiono OK')
        # else:
        #     print('Se presiono Cancel')
        # Creamos el dialogo
        # dialogo = QDialog(self)
        # dialogo.setWindowTitle('Ayuda')
        # # Creamos un nuevo event loop
        # # Se bloquea la ventana principal( ventana modal)
        # # y solo podemos interactuar con la nueva ventana
        # # Para ejecutar la ventana modal
        # dialogo.exec()
        
if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()