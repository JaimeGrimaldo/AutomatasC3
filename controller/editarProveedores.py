from PySide2.QtWidgets import QWidget,QMessageBox
from views.editar_proveedores import VentanaProveeores
from PySide2.QtCore import Qt
from db.PuntoVenta import BuscarProveedor, EditarProveedor
import re

class EditarProveedoress(QWidget, VentanaProveeores):
    def __init__(self, parent=None, _codigo=None):
        super().__init__(parent)
        self._codigo = _codigo
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.cargarDatos()
        self.Boton_Buscar.clicked.connect(self.buscarProveedor)
        self.Boton_Confirmar.clicked.connect(self.actualizarDatos)

    def buscarProveedor(self):
        print("Boton de buscar, funciona.")
    def confirmarCambios(self):
        print("Boton de cambios, funciona.")

    def cargarDatos(self):
        data = BuscarProveedor(self._codigo)
        print("Esto es:",data)
        print("Nombre:",data[0][0])
        print("Producto:",data[0][1])
        print("Codigo:",data[0][2])
        self.Field_CodigoProveedor.setText(data[0][2])
        self.Field_NombreProveedor.setText(data[0][0])
        self.Field_Producto.setText(data[0][1])

    def check(self):
        codigo= self.Field_CodigoProveedor.text()
        nombre = self.Field_NombreProveedor.text()
        producto = self.Field_Producto.text()
        if codigo ==""or nombre =="" or producto =="":
            QMessageBox.information(self,"Error en campos","Campos vacios.")
            return False
        else: 
            return True

    def actualizarDatos(self):
        REnombre = re.compile("^([a-zA-Z]{2,}\s[a-zA-z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{10,25})?)")
        nombre = self.Field_NombreProveedor.text()
        producto = self.Field_nombreProducto.text()
        codigo = self.field_codigoProveedor.text()
        matchNombre = REnombre.match(nombre)
        data = (nombre,producto)

        print(nombre, producto, codigo,"DATA: ",data)
        
        if not matchNombre:
            QMessageBox.information(self,"ERROR EN NOMBRE","Debe de ser de 10 a 25 caracteres")
            print("ERROR EN NOMBRE Debe de ser de 10 a 25 caracteres")
        else:
            if self.check():
                if EditarProveedor(self._codigo,data):
                    print("Se actualizo chido")
                    QMessageBox.information(self,"Actualizacion exitosa","La informacion fue correctamente actualizada") 
                else:
                    print("hay pedos")
                    QMessageBox.information(self,"Problemas de actualizacion","La informacion no se guardo")
            else:
                QMessageBox.information(self,"Campos vacios","Hay campos vacios que no fueron llenados.")
                print("Campos vacios")
            
