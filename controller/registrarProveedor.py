from PySide2.QtWidgets import QWidget,QMessageBox
from views.registro_proveedores import VentanaRegistroProveedores
from PySide2.QtCore import Qt
from db.PuntoVenta import InsertProveedor
import re

class registrarProveedor(QWidget, VentanaRegistroProveedores):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.Boton_confirmarRegistro.clicked.connect(self.addProveedor)

    def check(self):
        nombre = self.Field_nombreProveedor.text()
        producto = self.Field_nombreProducto.text()
        codigo = self.field_codigoProveedor.text()
        
        if nombre == "" or producto == "" or codigo =="":
            return False
        else:
            return True

    def addProveedor(self):
        REnombre = re.compile("^([a-zA-Z]{2,}\s[a-zA-z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{10,25})?)")
        nombre = self.Field_nombreProveedor.text()
        producto = self.Field_nombreProducto.text()
        codigo = self.field_codigoProveedor.text()
        matchNombre = REnombre.match(nombre)
        if not matchNombre:
            QMessageBox.information(self,"ERROR EN NOMBRE","Debe de ser de 10 a 25 caracteres")
        else:
            if self.check():
                data = (nombre,producto,codigo)
                if InsertProveedor(data):
                    print("Se registro chido")
                    QMessageBox.information(self,"Registro exitoso","La informacion fue correctamente agregada") 
                else:
                    print("hay pedos")
                    QMessageBox.information(self,"Problemas de registro","La informacion no se guardo")
            else:
                QMessageBox.information(self,"Campos vacios","Hay campos vacios que no fueron llenados.")




            
    

