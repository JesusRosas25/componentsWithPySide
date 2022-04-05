import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget


# class VentanaPrincipal(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Signals y Slots')
#         # Boton 
#         self.boton = QPushButton('Click aqui')        
#         # Asociamos la señal de click al slot evento_click
#         self.boton.clicked.connect(self.evento_click)
#         # Conectar a la señal de cambio de titulo
#         self.windowTitleChanged.connect(self.cambio_titulo_aplicacion)
#         # # conectamos el evento checado (por default es False)
#         # boton.setCheckable(True)
#         # # Conectamos el evento (signal) click con el slot (evento_check)
#         # boton.clicked.connect(self.evento_check)
#         # # Conectamos el evento (signal) click con el slot (evento_click)
#         # boton.clicked.connect(self.evento_click)
#         # Pulsamos el boton
#         self.setCentralWidget(self.boton)
#     def evento_click(self):
#     # Cambiar el texto del boton y el titulode ventana
#         self.boton.setText('Nuevo texto boton')
#         self.boton.setEnabled(False)
#         self.setWindowTitle('Nuevo titulo de la aplicacion')
#         print('evento_click')    
    
#     def cambio_titulo_aplicacion(self,nuevo_titulo):
#         print(f'Nuevo titulo aplicacion: {nuevo_titulo}')
        
#     # def evento_click(self):
#     #     print('Pulsaste el boton')
#     #     print('Presionaste el boton checkar?', self.boton_checkar)

#     # def evento_check(self, checkar):
#     #     self.boton_checkar = checkar
#     #     print('Checado?', self.boton_checkar)
            

        
# if __name__ == '__main__':
#     app = QApplication([])
#     # creamos un objeto de tipo ventana
#     ventan = VentanaPrincipal()
#     ventan.show()
#     # Ejecutamos la ventana
#     sys.exit(app.exec())


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals y Slots')
        self.setFixedSize(400, 200)
        # Definimos la etiqueta y linea de edicion
        self.etiqueta = QLabel()
        self.entrada_texto = QLineEdit()
        # Conectar el witget de entrada_texto con la etiqueta
        # La señal es textChanged, el slot es setText
        self.entrada_texto.textChanged.connect(self.etiqueta.setText)
        # Publicamos los componentes usando un layout
        layout = QVBoxLayout()
        layout.addWidget(self.entrada_texto)
        layout.addWidget(self.etiqueta)
        # Crear un contenedor
        contenedor = QWidget()
        contenedor.setLayout(layout)
        # Publicamos el contenedor, el cual ya incluye los demas elementos
        self.setCentralWidget(contenedor)
        
if __name__ == '__main__':
    app = QApplication([])
    # creamos un objeto de tipo ventana
    ventan = VentanaPrincipal()
    ventan.show()
    # Ejecutamos la ventana
    sys.exit(app.exec())