import re
from PySide2.QtWidgets import QWidget, QMessageBox
from PySide2.QtCore import Qt
from views.login import LoginVentana
from db.PuntoVenta import IniciarSesion

class Login(QWidget,LoginVentana):
    def __init__(self,parent = None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.Login.clicked.connect(self.Iniciar)
        self.BotonRegistro.clicked.connect(self.RegistrarUsuario)
          
          
    def CheckInput(self):
        usuario = self.UsuarioLine.text()
        password = self.PasswordLine.text()
        if usuario == "" or password == "":
            QMessageBox.information(self, "ERROR", "DATOS VACIOS")
            return False
        else:
            return True
    
    def Iniciar(self):
        usuario = self.UsuarioLine.text()
        password = self.PasswordLine.text()
        REpassword = re.compile("^(?=.[A-Za-z])(?=.\d)[A-Za-z\d]{8,}$")
        REusuario = re.compile("^[\s\S]{6,12}$")
        matchUsuario = REusuario.match(usuario)
        matchPassword = REpassword.match(password)
        # if not matchUsuario:
        #     QMessageBox.information(self,"ERROR USUARIO","Debe ser de 6 a 12 caracteres")
        # if not matchPassword:
        #     QMessageBox.information(self,"ERROR PASSWORD","Mínimo ocho caracteres, al menos una letra mayúscula, una letra minúscula, un número y un carácter especial")
        # else:
        if self.CheckInput():
             data = (usuario,password)
        if IniciarSesion(data):              
                from controller.venta import VentaWindow
                window = VentaWindow(self)
                window.show()
        else:
            QMessageBox.information(self, "ERROR", "DATOS ERRONEOS")

    def RegistrarUsuario(self):
        from controller.registro import Registrar
        window = Registrar(self)
        window.show()
        